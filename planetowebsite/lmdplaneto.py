#! /usr/bin/env python
import ads
import os

#######
lk = "lmdplaneto.link"
anneec = 2014
gencond = ''' -c 'not journal:"Discussions"' ''' # to solve EGU journal duplication
#######

os.chdir("/home/marshttp/bibweb/planetowebsite/") ## for crontab

ads.makepage('pubmars',\
             retrieve = True,\
             customcond = gencond + ''' -c 'title:"Mars" or title:"martian"' ''',\
             linkads = lk,\
             printnum = True,\
             includebook = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Mars peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubtitan',\
             retrieve = False,\
             customcond = gencond + ''' -c 'title:"Titan"' ''',\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Titan peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubvenus',\
             retrieve = False,\
             customcond = gencond + ''' -c 'title:"Venus" or title:"venusian"' ''',\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Venus peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubexo',\
             retrieve = False,\
             customcond = gencond + ''' -c 'abstract:"exoplanet" or title:"habitable" or title:"habitability"' ''',\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Exoplanets peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubsaturn',\
             retrieve = False,\
             customcond = gencond + ''' -c 'title:"Saturn"' ''',\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Saturn peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubforget',\
             retrieve = False,\
             customcond = gencond + ''' -c 'author:"Forget"' ''',\
             listyear = range(anneec,1993-1,-1),\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Francois Forget's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('publebonnois',\
             retrieve = False,\
             customcond = gencond + ''' -c 'author:"Lebonnois"' ''',\
             listyear = range(anneec,1999-1,-1),\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Sebastien Lebonnois's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pubspiga',\
             retrieve = False,\
             customcond = gencond + ''' -c 'author:"Spiga"' ''',\
             listyear = range(anneec,2007-1,-1),\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Aymeric Spiga's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pubmillour',\
             retrieve = False,\
             customcond = gencond + ''' -c 'author:"Millour"' ''',\
             listyear = range(anneec,2003-1,-1),\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Ehouarn Millour's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pubmadeleine',\
             retrieve = False,\
             customcond = gencond + ''' -c 'author:"Madeleine"' ''',\
             listyear = range(anneec,2009-1,-1),\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Jean-Baptiste Madeleine's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pubguerlet',\
             retrieve = False,\
             customcond = gencond + ''' -c 'author:"Guerlet"' ''',\
             listyear = range(anneec,2008-1,-1),\
             linkads = lk,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Sandrine Guerlet's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pub',\
             retrieve = False,\
             listyear = range(anneec,1993-1,-1),\
             linkads = lk,\
             customcond = gencond,\
             printnum = True,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>",\
addlink = '''
<br>
Planet:
<a href="pubmars.html">Mars</a> /
<a href="pubvenus.html">Venus</a> /
<a href="pubtitan.html">Titan</a> /
<a href="pubsaturn.html">Saturn</a> /
<a href="pubexo.html">Exoplanets</a><br>
<br>
Author:
<a href="pubforget.html">F. Forget</a> /
<a href="publebonnois.html">S. Lebonnois</a> /
<a href="pubmillour.html">E. Millour</a> /
<a href="pubspiga.html">A. Spiga</a> /
<a href="pubmadeleine.html">J.-B. Madeleine</a> /
<a href="pubguerlet.html">S. Guerlet</a>
<br>
<hr>
''',\
target="/home/marshttp/www-mars/pubplaneto")
