#! /usr/bin/env python
import ads

lk="demo.link"

ads.makelink(n="Feynman",fn="Richard",ini="R.P.",name=lk)

ads.makepage('feynman',\
             retrieve = True,\
             linkads = lk,\
             listyear = range(2015,1900,-1),\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Richard Feynman's publications</font></EM></H2></CENTER>",
             target = 'demo')

