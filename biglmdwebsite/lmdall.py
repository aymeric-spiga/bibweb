#! /usr/bin/env python
#-*- coding: utf8 -*-
import ads
import numpy as np
import os

##########################################
# Aymeric SPIGA
# Laboratoire de Météorologie Dynamique
# 15-20/12/2013
##########################################

#### SETTINGS
titpre = "<CENTER><H2><EM><font color='#B8860B;'>" # title prefix
titsuf = "</font></EM></H2></CENTER>" # title suffix
anneec = 2014 # last year to include
####

#cc = ''' -c ' '''
#cc = cc+' author:"Forget"'
#cc = cc+' or author:"Lebonnois"'
#cc = cc+' or author:"Spiga"'
#cc = cc+' or author:"Madeleine"'
#cc = cc+''' ' '''
#eq = 'PLANETO'
#ads.makepage('pub'+eq,retrieve=True,listyear=years,linkads=link,customcond = cc,\
#title = "<CENTER><H2><EM><font color='#B8860B;'>EQUIPE "+eq+"</font></EM></H2></CENTER>")







### CLEAN
os.system('rm -rf lmdall')

### GET TEAM LIST and SIZE
nom,prenom,initiales,equipe,anneedeb,anneefin,altnom = np.loadtxt("listpeople.txt",delimiter=";",dtype='string',unpack=True,skiprows=3,comments="#")
ntot = nom.size

### PREPARE ADS LINK
# 1. generic parts
adslink1="http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PHY&db_key=PRE&qform=PHY&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&aut_xct=YES&aut_logic=OR&author="
adslink2="+&ned_query=YES&sim_query=YES&start_mon=&start_year=&end_mon=&end_year=&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=999&start_nr=1&jou_pick=NO&ref_stems="
adslink3="&data_and=ALL&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&data_type=BIBTEXPLUS&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1"
# 2. author list
st=adslink1 ; st2 = ""
tf = open("lmdall.testauthor", 'w') # this is just for testing ADS
for iii in range(ntot):
  st = st + nom[iii].split()[0].replace('é',"%C3%A9")\
          +"++%2C++"\
          + prenom[iii].split()[0].replace('é',"%C3%A9")\
          +"++%3B++"\
          + nom[iii].split()[0].replace('é',"%C3%A9")\
          +"++%2C++"\
          + initiales[iii].split()[0].replace('é',"%C3%A9")\
          +"++%3B++"
  st2 = st2 + nom[iii] + " , " + prenom[iii] + " ; " + nom[iii] + " , " + initiales[iii] + " ; "
  if altnom[iii].split()[0] != "-":
    st = st + altnom[iii].split()[0].replace('é',"%C3%A9")\
            +"++%2C++"\
            + prenom[iii].split()[0].replace('é',"%C3%A9")\
            +"++%3B++"\
            + altnom[iii].split()[0].replace('é',"%C3%A9")\
            +"++%2C++"\
            + initiales[iii].split()[0].replace('é',"%C3%A9")\
            +"++%3B++"
    st2 = st2 + altnom[iii] + " , " + prenom[iii] + " ; " + altnom[iii] + " , " + initiales[iii] + " ; "    
st=st+adslink2
tf.write(st2)
tf.close()
# 3. journal list
jn = ""
f = open("listjournals.txt", 'r')
for line in f:
  jj = line.strip().replace("&","%26")
  jn = jn + jj + "+"
st=st+jn+adslink3
# 4. write final result
dalink = "lmdall.link"
os.system('rm -rf '+dalink)
daf = open(dalink, 'w')
daf.write(st)
daf.close()

### RETRIEVE COMPLETE BIBTEX FILE
ads.makepage('lmd_dummy',retrieve=True,linkads=dalink,listyear=[1950])

### LOOP ON NAMES
miny = 9999 ; maxy = -9999 ; lk = "<br>Author:"
for iii in range(ntot):
  # 1. get and prepare various components
  danom = nom[iii].split()[0] ; daprenom = prenom[iii].split()[0]
  dayears = int(anneedeb[iii]) ; dayeare = int(anneefin[iii])
  daini = initiales[iii].split()[0]
  cc = ''' -c ' '''
  cc = cc + ''' author:"'''+danom+'''" '''
  if altnom[iii].split()[0] != "-": 
     danomalt = altnom[iii].split()[0]
     cc = cc + ''' or author:"'''+danomalt+'''" '''
  cc = cc+''' ' '''
  # -- if year start 0000 and year end 0000 do not do anything
  if dayears + dayeare != 0:
    if dayears == 0: dayears = anneec
    if dayeare == 0: dayeare = anneec
    # 2. info
    print danom+"-"+daprenom+"-"+str(dayears)+"-"+str(dayeare)
    # 3. make page
    ads.makepage('lmd_'+danom,\
               retrieve=False,\
               customcond=cc,\
               listyear=range(dayeare,dayears-1,-1),\
               linkads=dalink,\
               title = titpre+daprenom+" "+danom+titsuf)
    # 4. get intervals of years for the whole lab
    if dayears < miny: miny = dayears
    if dayeare > maxy: maxy = dayeare  
    # 5. get authors link list
    lk = lk + ''' <a href="lmd_'''+danom+'''.html">'''+daini+" "+danom.replace('é',"&eacute;")+"</a> /"

### MAKE FINAL PAGE
ads.makepage('lmd_',\
             retrieve = False,\
             listyear = range(maxy,miny-1,-1),\
             linkads=dalink,\
             title = "<CENTER><H2><EM><font color='#B8860B;'>Peer-reviewed publications for LMD</font></EM></H2></CENTER>",\
	     addlink = lk,\
             target = "lmdall")
