#! /usr/bin/env python
import ads

ads.makepage('pubdd',\
             embedded = True,\
             retrieve = True,\
             customcond = ''' -c 'abstract:"devil"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about dust devils</h2>")

ads.makepage('pubgw',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"gravity wave"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about gravity waves</h2>")

ads.makepage('pubmeso',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'abstract:"mesoscale"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about mesoscale meteorology</h2>")

ads.makepage('pubcloud',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"cloud"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about clouds</h2>")

ads.makepage('pubearth',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"Earth" or title:"terrestrial" or title:"Andes"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about the Earth</h2>")

ads.makepage('pubmars',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"Mars" or title:"martian"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about Mars</h2>")

ads.makepage('pubbl',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"boundary layer" or title:"microscale" or title:"large-eddy simulations"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about planetary boundary layer</h2>")

ads.makepage('pubremote',\
             embedded = True,\
             retrieve = False,\
             customcond = ''' -c 'title:"spectrometer"' ''',\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "<h2>Publications about remote sensing</h2>")

ads.makepage('pub',\
             embedded = True,\
             retrieve = False,\
             listyear = [2013,2012,2011,2010,2009,2008,2007],\
             linkads = "link.spiga",\
             addpdf = "http://dl.dropbox.com/u/11078310/my_papers/ref/",\
             title = "",\
addlink = '''
Planet:
<a href="pubmars.html">Mars</a> /
<a href="pubearth.html">the Earth</a><br>
Topic:
<a href="pubmeso.html">Mesoscale meteorology</a> /
<a href="pubremote.html">Remote sensing</a> / 
<a href="pubbl.html">Planetary Boundary layer</a> /
<a href="pubcloud.html">Clouds</a> /
<a href="pubdd.html">Dust devils</a> /
<a href="pubgw.html">Gravity waves</a>
'''+"<br><br /><hr><br>"+open('inpress.html').read())
