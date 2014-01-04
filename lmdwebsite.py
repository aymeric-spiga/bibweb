#! /usr/bin/env python
import ads

ads.makepage('pubtitan',\
             retrieve = True,\
             customcond = ''' -c 'title:"Titan"' ''',\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Titan peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubmars',\
             retrieve = False,\
             customcond = ''' -c 'title:"Mars" or title:"martian"' ''',\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Mars peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubvenus',\
             retrieve = False,\
             customcond = ''' -c 'title:"Venus" or title:"venusian"' ''',\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Venus peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubexo',\
             retrieve = False,\
             customcond = ''' -c 'abstract:"exoplanet" or title:"habitable" or title:"habitability"' ''',\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Exoplanets peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>")

ads.makepage('pubforget',\
             retrieve = False,\
             customcond = ''' -c 'author:"Forget"' ''',\
             listyear = range(2014,1992,-1),\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Francois Forget's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('publebonnois',\
             retrieve = False,\
             customcond = ''' -c 'author:"Lebonnois"' ''',\
             listyear = range(2014,1998,-1),\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Sebastien Lebonnois's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pubspiga',\
             retrieve = False,\
             customcond = ''' -c 'author:"Spiga"' ''',\
             listyear = range(2014,2006,-1),\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Aymeric Spiga's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pubmillour',\
             retrieve = False,\
             customcond = ''' -c 'author:"Millour"' ''',\
             listyear = range(2014,2007,-1),\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Ehouarn Millour's peer-reviewed publications</font></EM></H2></CENTER>")

ads.makepage('pub',\
             retrieve = False,\
             listyear = range(2014,1992,-1),\
             linkads = "link.LMD_planeto",\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Peer-reviewed publications of the LMD 'Planetary Atmospheres' team</font></EM></H2></CENTER>",\
addlink = '''
<br>
Planet:
<a href="pubmars.html">Mars</a> /
<a href="pubvenus.html">Venus</a> /
<a href="pubtitan.html">Titan</a> /
<a href="pubexo.html">Exoplanets</a><br>
<br>
Author:
<a href="pubforget.html">F. Forget</a> /
<a href="publebonnois.html">S. Lebonnois</a> /
<a href="pubspiga.html">A. Spiga</a> /
<a href="pubmillour.html">E. Millour</a><br>
<br>
<hr>
''')
