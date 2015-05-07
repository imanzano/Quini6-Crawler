import argparse
import csv
import os
from lxml import html
import time
import re 
from datetime import date, timedelta,datetime


csvheader = ("nro", "date","type","nr1","nr2","nr3","nr4","nr5","nr6")
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
    parser.add_argument('-f', '--filename', help='File to parse.', required = True)
    parser.add_argument('-o', '--output', help='CSV file containing nro,date,type,nr1,nr2,nr3,nr4,nr5,nr6.', required = True)
    args = vars(parser.parse_args())
    f = open( args['output'], 'wb')
    c = csv.writer(f, delimiter = ';', quotechar = '"')
    
    c.writerow(csvheader)
    	
    for f in os.listdir(args['filename']):    
        print args['filename'] + '/'+ f
        tree = html.parse(open(args['filename'] + '/'+ f, 'rb'))
        nro = tree.xpath('//*[@id="t_quini6"]/tbody/tr[2]/td/center/table/tbody/tr/td/font/b/text()')
        
        print nro
        if len(nro):
           
            nro = nro[0].split(" ")[2].encode("utf-8")

            d = tree.xpath('//*[@id="t_quini6"]/tbody/tr[14]/td/font[2]/text()')     
            print d[0]

            date = datetime.strptime(d[0],'%d/%m/%Y') - timedelta(days=15)
            date_str = '{0.day}/{0.month}/{0.year}'.format(date)
             
            for i in [4,6,8,10]:         
                n = tree.xpath('//*[@id="t_quini6"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[2]/div/font/b/text()')
                n = n[0].replace(" ", "").split('-')
                line = nro,date_str,quini_type[str(i)],n[0],n[1],n[2],n[3],n[4],n[5]
                c.writerow(line)
     
def test():
    d0 = date(2007, 8, 18)
    d1 = date(2006, 9, 26)
    delta = d0 - d1
    print time.strptime("15/01/2007",'%d/%m/%Y')
    print date(2007,1,15)-timedelta(days=15)
    '{0.day}/{0.month}/{0.year}'.format(date(2007,1,15)-timedelta(days=15))

if __name__ == "__main__":
    main()
    #test()
