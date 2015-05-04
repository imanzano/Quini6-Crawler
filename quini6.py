import argparse
import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
import datetime
import urllib2
import json
import csv

parser = argparse.ArgumentParser(description='Process year and last lotery nro')
parser.add_argument("apikey")
parser.add_argument("year",type=int)
parser.add_argument("nro",type=int)
args = parser.parse_args()

year=args.year
nro=args.nro
apikey=args.apikey

myfile = open("%s.csv" % year, 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

before=datetime.datetime(year,1,1)
after=datetime.datetime(year,12,31)
rr = rrule.rrule(rrule.WEEKLY,byweekday=(relativedelta.SU,relativedelta.WE),dtstart=before)

for d in  reversed(rr.between(before,after,inc=True)):	
   date = d.strftime("%d-%m-%Y")
   url = "https://www.kimonolabs.com/api/ondemand/a1cxw7t6?apikey={}&kimpath2=sorteo-{}-del-dia-{}.htm".format(apikey,nro,date)
   print url
   try:
      res= urllib2.urlopen(url)
      j = json.load(res)
      for item in j["results"]["collection1"]:
         row = [ nro, date, item["tipo"].encode('utf-8')]
         for n in item["numeros"].split("-"):
	   row.append(n)
         wr.writerow(row)
      nro=nro-1   
   except Exception:
      print "Error processing url. Skipped"
