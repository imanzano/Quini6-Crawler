import argparse
import csv
import os
from lxml import html
import time
import re 
from datetime import date, timedelta,datetime


csvheader = ("nro", "date","type","nro")
quini_type = {'4': 'T', '6': 'S', '8': 'R','10':'SS'}; 
 
spanish_months = {
    "Enero" : "January",
    "Febrero" : "Febrary",
    "Marzo" : "March",
    "Abril" : "April",
    "Mayo" : "May",
    "Junio" : "June",
    "Julio" : "July",
    "Agosto" : "August",
    "Septiembre" : "September",
    "Octubre" : "October",
    "Noviembre" : "November",
    "Diciembre" : "December",
  } 

 ## From Stackoverflow (http://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex-in-python)
def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 


def main():
    parser = argparse.ArgumentParser(description = 'Export Quini6 numbers to CSV.')
    parser.add_argument('-p', '--path', help='Path with raw data files.', required = True)
    parser.add_argument('-o', '--output', help='CSV file containing card nro,date,type,number.', required = True)
    args = vars(parser.parse_args())
    f = open( args['output'], 'w')
    f2 = open( "all.csv", 'w')
    

    c = csv.writer(f, delimiter = ',', quotechar = '"')

    c2 = csv.writer(f2, delimiter = ',', quotechar = '"')
    
    #c.writerow(csvheader)
    	
    for f in os.listdir(args['path']):    
        
        tree = html.parse(open(args['path'] + '/'+ f, 'rb'))
        nro = tree.xpath('//*[@id="t_quini6"]/tbody/tr[2]/td/center/table/tbody/tr/td/font/b/text()')
        
        if len(nro):
           
            nro = nro[0].split(" ")[2].encode("utf-8")

            d = tree.xpath('//*[@id="t_quini6"]/tbody/tr[14]/td/font[2]/text()')     
        

            date = datetime.strptime(d[0],'%d/%m/%Y') - timedelta(days=15)
            date_str = '{0.day}/{0.month}/{0.year}'.format(date)
             
            for i in [4,6,8,10]:         
                n = tree.xpath('//*[@id="t_quini6"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[2]/div/font/b/text()')
                n = n[0].replace(" ", "").split('-')
                
                odd =0
                even =0
                par = 0
                for j in range(0,6):     
                    line = nro,date_str,quini_type[str(i)],n[j]
                    c2.writerow(line)    

                    if ( int(n[j]) % 2 == 0):                        
                        even=even+1
                    else:
                        odd=odd+1
                    
                    if (j<5) and (int(n[j])+1 == int(n[j+1])): 
                        par = par+1

                line = nro,date_str,quini_type[str(i)], n[0],n[1],n[2],n[3],n[4],n[5],odd,even,par
                c.writerow(line)
                    
     
if __name__ == "__main__":
    main()
