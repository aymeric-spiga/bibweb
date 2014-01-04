#! /usr/bin/env python
import ads

ads.makepage('feynman',\
             retrieve = True,\
             listyear = range(1990,1938,-1),\
             linkads = "feynman.link",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Richard Feynman's publications</font></EM></H2></CENTER>")
