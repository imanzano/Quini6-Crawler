import urllib
import argparse

parser = argparse.ArgumentParser(description='Download raw data')
parser.add_argument("f",type=int)
parser.add_argument("t",type=int)

args = parser.parse_args()
f=args.f
t=args.t
for num in range(f,t):
   url = "http://www.resultadosdelquini6.com/quini6/resultado-quini-6-{}".format(num)
   print url
   filename = "quini6-{}.html".format(num)
   
   urllib.urlretrieve (url, filename)
