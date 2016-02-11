# Quini6-Crawler

Simple quini6 result crawler made in python. It is just a simple proof of concept about simple python commands.

## Simple parsing example with Apache Zeppelin

```
import sys.process._

val content = sc.textFile(<YOUR PATH HERE>"/output/out.csv")

case class Card(card:Integer, d:Integer,m:Integer,a:Integer, t : String, nro : Integer)

val cards = content.map(s=>s.split(";")).filter(s=>s(0)!="\"nro\"").map(
    s=>Card(s(0).toInt, 
            s(1).replaceAll("\"", "").split("/")(0).toInt,
            s(1).replaceAll("\"", "").split("/")(1).toInt,
            s(1).replaceAll("\"", "").split("/")(2).toInt,
            s(2).replaceAll("\"", ""),
            s(3).replaceAll("\"", "").toInt
        )
)

cards.toDF().registerTempTable("cards")
```
