import urllib

#parser = argparse.ArgumentParser(description='Process year and last lotery nro')
#parser.add_argument("from",type=int)
#parser.add_argument("to",type=int)

#args = parser.parse_args()

for num in range(1279,2250):
   url = "http://www.resultadosdelquini6.com/quini6/resultado-quini-6-{}".format(num)
   print url
   filename = "quini6-{}.html".format(num)
   
   urllib.urlretrieve (url, filename)
