import os, re, urllib

## -----------------------------------------------------------------
## Purpose: make a nice publication page with an ADS database link
## Author: Aymeric Spiga 19/05/2013 improvements 10-12/2013
## -----------------------------------------------------------------
## NB: uses BIBTEX2HTML https://www.lri.fr/~filliatr/bibtex2html/doc/manual.html
## ... and of course NASA ADS http://adsabs.harvard.edu/
## -----------------------------------------------------------------

def makepage(authorref,
             bibstyle = "-s custom -nokeys",
             listyear = [0],
             customcond = None,
             embedded = False,
             linkads = None,
             title = None,
             retrieve = True,
             addpdf = None,
             addlink = None,
             target=None):

    htmlcontent = ""
    
    ### HEADER
    if embedded:
     htmlfile = open('header.html','r')
     htmlcontent = htmlfile.read()
     htmlfile.close()
    #else:
    if title is None:
      htmlcontent = htmlcontent + "<h2>"+authorref+"'s publications</h2>"
    elif title == "":
      pass
    else:
      htmlcontent = htmlcontent + title
    
    ### if linkads is None, we set it to "link.authorref"
    if linkads is None: 
      linkads = authorref+'.link'

    ### GET INFO FROM ADS
    if retrieve:
      print "retrieving info from ADS"
      linkfile = open(linkads,'r')
      url = linkfile.read()
      linkfile.close()
      html = urllib.urlopen(url).read()
      bibfile = open(linkads+'.bib','w')
      print >> bibfile,html
      bibfile.close()
    
    ### if only one year and no customcond, make it useful. ask for years >= this value
    if len(listyear) == 1 and customcond is None:
        customcond = "-c 'year>=%s'" % (listyear[0])
        listyear[0] = 99
    
    ### ADD LINK WITH YEARS IN HEADER
    if customcond is None or len(listyear) > 1:
        htmlcontent += "Year: "
        for year in listyear:
          htmlcontent += "<a href='#"+str(year)+"'>"+str(year)+"</a>.  "
        if addlink is not None: htmlcontent += "<br>"+addlink
    
    ### YEAR LOOP
    for year in listyear:
    
        author = authorref+str(year)
        print author
    
        # 0. define condition
        #    if not user-defined, make it simply year in each listyear instance
        #    if user-defined, then customcond will be the condition (possibly several)
        if customcond is None and len(listyear) > 1: cond = "-c 'year=%s'" % (year)
        elif len(listyear) > 1: cond = customcond + " -c 'year=%s'" % (year)
        else: cond = customcond
    
        # 1. select items ARTICLE in the big bib file
        #    put those in a dedicated author.bib file
        arg = \
              cond,\
              '"ARTICLE"',\
              author+'.txt',\
              author+'.bib',\
              linkads+'.bib'
        cmd = "bib2bib --quiet %s -c '$type=%s' -oc %s -ob %s %s" % (arg)
        os.system(cmd)

        # modify the bib file to insert pdf links
        # the trick is to use the line adsurl and expect pdf to have the same name as ADS reference       
        #        ... then besides this, it is necessary to link pdfs or rename those
        #        ... the online repository is indicated by addpdf
        if retrieve:
         if addpdf is not None:
            bibcontent = ''
            for line in open(linkads+'.bib'):
                bibcontent += line
                if 'adsurl' in line:
                    line = line.replace('adsurl','localpdf')
                    line = line.replace('http://cdsads.u-strasbg.fr/abs/',addpdf)
                    line = line.replace('},','.pdf},')
                    line = line.replace('%','_')
                    bibcontent += line
            bibfile2 = open('temp','w')
            print >> bibfile2,bibcontent
            bibfile2.close()
            os.system('mv temp '+linkads+'.bib')

        # 2. make the html page from the author.bib file
        if customcond is None or len(listyear) > 1:
           header = '<a name="%.0f"></a>' % (year)
           header += "<h3>%.0f <a href=''>.</a> </h3>" % (year)
           if embedded: header += '<br>'
        else:
           header = ''
    
        header = '"'+header+'"'
        arg = \
              bibstyle,\
              header,\
              author+'.bib'
        cmd = "bibtex2html -q \
              --both \
              -m ads.tex \
              %s \
              -nf adsurl 'ADS link' \
              -nf localpdf 'PDF version' \
              -r -d --revkeys \
              -nofooter --nodoc \
              --header %s -nokeywords \
              %s" % (arg)
        os.system(cmd)

        # 3. load page content and delete intermediate HTML file
        htmlfile = open(author+'.html','r')
        htmlcontent = htmlcontent + htmlfile.read()
        htmlfile.close()
        os.system("rm -rf "+author+'.html')
    
    ## make a few corrections
    ##     bibcontent = open(author+'.bib','r').read()
    ##     bibcontent.replace('\grl','Yeah')
    
    find = re.compile(r'bib')
    htmlcontent = find.sub('Bibtex entry',htmlcontent)
    find = re.compile(r'Bibtex entry.html')
    htmlcontent = find.sub('bib.html',htmlcontent)
    
    find = re.compile(r'DOI')
    htmlcontent = find.sub('Journal website',htmlcontent)

    #find = re.compile(r'.pdf')
    #htmlcontent = find.sub('PDF version',htmlcontent)
    
    find = re.compile(r'<table>')
    htmlcontent = find.sub('<table border="0" cellspacing="15">',htmlcontent)
    find = re.compile(r'<td align="right">')
    htmlcontent = find.sub('<td align="center" width=17% style="font-size: 75%;">',htmlcontent)

    htmlcontent += '''<hr><p>Generated with 
    <a href='https://www.lri.fr/~filliatr/bibtex2html/doc/manual.html'>BibTeX2HTML</a> 
    and <a href='http://adsabs.harvard.edu/'>NASA ADS</a>
    and a bit of <a href='http://www.python.org/'>Python</a></p>'''
    if embedded:
      htmlfile = open('footer.html','r')
      htmlcontent += htmlfile.read()
      htmlfile.close()
      
    htmlmain = open(authorref+'.html','w')
    print >> htmlmain, htmlcontent
    htmlmain.close()

    ## move results to target directory and remove txt files
    if target is not None:
      target=target+"/"
      arg = target,\
          authorref+"*.html",\
          authorref+"*.bib",\
          authorref+"*.txt",\
          target,\
          target+linkads+".bib",\
          "*.css",\
          target
      os.system( "mkdir -p %s ; mv %s %s %s %s ; mv %s ./ 2> /dev/null ; cp %s %s 2> /dev/null" % (arg) )