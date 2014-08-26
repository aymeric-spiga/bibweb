#! /usr/bin/env python
import ads

lk="demo.link"

#marche pas
#ads.makelink(n="Feynman",fn="Richard",ini="R.",name=lk)

ads.makepage('feynman',\
             retrieve = True,\
             listyear = range(1990,1938,-1),\
             linkads = lk,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Richard Feynman's publications</font></EM></H2></CENTER>",
             target = 'demo')
