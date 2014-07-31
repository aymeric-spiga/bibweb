#! /usr/bin/env python
import ads

######
lk="spiga.link"
######

ads.makepage('pubdd',\
             embedded = True,\
             retrieve = True,\
             customcond = ''' -c 'title:"dust storm" or title:"dust devil"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Dust storms and dust devils</h2>")

ads.makepage('pubsurf',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"geological" or title:"surface" or abstract:"deposit"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Surface-atmosphere interactions</h2>")

ads.makepage('pubcloud',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"cloud"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Clouds</h2>")

ads.makepage('pubgw',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"gravity wave"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Gravity waves</h2>")

ads.makepage('pubbl',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"turbulent" or abstract:"large-eddy"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Turbulence</h2>")

ads.makepage('pubkata',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"katabatic"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Katabatic winds</h2>")

ads.makepage('pubearth',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"Earth" or title:"terrestrial" or title:"Andes"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>the Earth</h2>")

ads.makepage('pubmars',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"Mars" or title:"martian"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Mars</h2>")

ads.makepage('pubsaturn',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"Saturn"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Saturn</h2>")

ads.makepage('pubremote',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"spectrometer"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Remote sensing</h2>")

ads.makepage('pubgcm',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"global climate model" or abstract:"GCM"' ''',\
             linkads = lk,\
             addpdf = "REF/",\
             title = "<h2>Global Climate</h2>")

ads.makepage('pub',\
             embedded = True,\
             retrieve = False,\
             listyear = [2014,2013,2012,2011,2010,2009,2008,2007],\
             linkads = lk,\
             addpdf = "REF/",\
             title = "",\
addlink = '''
Planet:
<a href="pubmars.html">Mars</a> /
<a href="pubearth.html">the Earth</a> /
<a href="pubsaturn.html">Saturn</a><br>
Selected topics:
<a href="pubdd.html">Dust storms and devils</a> /
<a href="pubcloud.html">Clouds</a> /
<a href="pubbl.html">Turbulence</a><br>
<a href="pubgw.html">Gravity waves</a> /
<a href="pubkata.html">Katabatic winds</a> /
<a href="pubsurf.html">Surface &harr; Atmosphere</a><br>
<a href="pubremote.html">Remote sensing</a> /
<a href="pubgcm.html">Global Climate</a>
'''+"<br><br /><hr><br>"+open('inpress.html').read(),\
             target = "spiga")
