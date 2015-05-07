import argparse
import csv
import os
from lxml import html

csvheader = ("nro", "date","type","nr1","nr2","nr3","nr4","nr5","nr6")
quini_type = {'4': 'T', '6': 'S', '8': 'R','10':'SS'}; 
 
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

            #d = tree.xpath('//*[@id="t_quini6"]/tbody/tr[2]/td/center/table/tbody/tr/td/font/font/text()')     

            #print d[0].strip()[24:]

            for i in [4,6,8,10]:         
                n = tree.xpath('//*[@id="t_quini6"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[2]/div/font/b/text()')
                n = n[0].replace(" ", "").split('-')
                line = nro,quini_type[str(i)],n[0],n[1],n[2],n[3],n[4],n[5]
                c.writerow(line)
     
if __name__ == "__main__":
    main()
