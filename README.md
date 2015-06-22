# Quini6-Crawler

Simple quini6 result crawler made in python. It is just a simple proof of concept about simple python commands.

## Simple parsing example with Apache Zeppelin

```
import sys.process._

val content = sc.textFile(<YOUR PATH HERE>"/output/out.csv")

case class Card(card:Integer, d:String, t : String, nro : Integer)

val cards = content.map(s=>s.split(";")).filter(s=>s(0)!="\"nro\"").map(
    s=>Card(s(0).toInt, 
            s(1).replaceAll("\"", ""),
            s(2).replaceAll("\"", ""),
            s(3).replaceAll("\"", "").toInt
        )
)

cards.toDF().registerTempTable("cards")
```
