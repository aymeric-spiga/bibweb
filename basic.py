#! /usr/bin/env python
import ads

ads.makepage('pub',\
             retrieve = True,\
             listyear = range(1990,1938,-1),\
             linkads = "link.feynman",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Richard Feynman's publications</font></EM></H2></CENTER>")
