#! /usr/bin/env python
#-*- coding: utf8 -*-
import ads
import numpy as np
import os

##########################################
# Aymeric SPIGA
# Laboratoire de Météorologie Dynamique
# 15-20/12/2013. teams 01/2014.
##########################################

#### SETTINGS
titpre = "<CENTER><H2><EM><font color='#B8860B;'>" # title prefix
titsuf = "</font></EM></H2></CENTER>" # title suffix
anneec = 2014 # last year to include
oneyear = None
oneyear = 2013
usercond = None
usercond = ''' -c 'not journal:"Discussions"' ''' # fixes the EGU Discussions journals problem
usercond = usercond + ''' -c 'not journal:"Polymer Science"' ''' # strange inclusions
perso = True
####

### FOLDER
folder = "/home/marshttp/www-mars/publmdall"
#folder = "/home/marshttp/www-mars/publmdallexp" # for tests
#folder = "/home/marshttp/www-mars/publmd/INTRO"
if oneyear is not None: folder = folder + str(oneyear)

### USEFUL FUNCTION
def addhtmlref(st,st2,nom,prenom,initiales):
    nnom = len(nom.split())
    nprenom = len(prenom.split())
    for iii in range(nnom):
     for jjj in range(nprenom):
      st = st + nom.split()[iii].replace('é',"%C3%A9")+"++%2C++"\
            + prenom.split()[jjj].replace('é',"%C3%A9")+"++%3B++"\
            + nom.split()[iii].replace('é',"%C3%A9")+"++%2C++"\
            + initiales.split()[0].replace('é',"%C3%A9")\
            +"++%3B++"
      st2 = st2 + nom.split()[iii] + " , " + prenom.split()[jjj] + " ; " + nom.split()[iii] + " , " + initiales.split()[0] + " ; "
    return st,st2

### CLEAN
os.system('rm -rf '+folder)

### GET TEAM LIST and SIZE
tnom,tprenom,tinitiales,tequipe,tanneedeb,tanneefin = np.loadtxt("listpeople.txt",delimiter=";",dtype='string',unpack=True,skiprows=3,comments="#")

### LOOP on EACH TEAM (and add a combined list for all TEAMS)
ll = list(set(tequipe)) ; ll.append('all') ; ll = ll[::-1]
#ll = list(set(tequipe)) ; ll = ll[::-1]
for eqeq in ll:

  ### GET ONLY MEMBERS OF THE TEAM
  if eqeq != 'all':
    w = np.where(tequipe==eqeq)
    nom = tnom[w] ; prenom = tprenom[w] ; initiales = tinitiales[w] ; equipe = tequipe[w] 
    anneedeb = tanneedeb[w] ; anneefin = tanneefin[w]
  else:
    nom = tnom ; prenom = tprenom ; initiales = tinitiales ; equipe = tequipe
    anneedeb = tanneedeb ; anneefin = tanneefin
  ntot = nom.size

  ### PREPARE ADS LINK
  # 1. generic parts
  adslink1="http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PHY&db_key=PRE&qform=PHY&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&aut_xct=YES&aut_logic=OR&author="
  adslink2="+&ned_query=YES&sim_query=YES&start_mon=&start_year=&end_mon=&end_year=&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=1999&start_nr=1&jou_pick=YES&ref_stems="
  if oneyear is not None:
     adslink2="+&ned_query=YES&sim_query=YES&start_mon=&start_year="+str(oneyear)+"&end_mon=&end_year="+str(oneyear)+"&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=1999&start_nr=1&jou_pick=NO&ref_stems="
  adslink3="&data_and=ALL&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&data_type=BIBTEXPLUS&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1"
  # 2. author list
  st=adslink1 ; st2 = ""
  tf = open("ads.testauthor", 'w') # this is just for testing ADS outside the script
  for iii in range(ntot):
     st,st2 = addhtmlref(st,st2,nom[iii],prenom[iii],initiales[iii])
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
  dalink = folder+eqeq.strip()+".link"
  os.system('rm -rf '+dalink)
  daf = open(dalink, 'w')
  daf.write(st)
  daf.close()
     
  ### RETRIEVE COMPLETE BIBTEX FILE (NB: does not seem to work without month)
  ads.makepage('lmd_dummy',retrieve=True,linkads=dalink,customcond=usercond,verbose=False,includemonth=True)

  ### LOOP ON NAMES
  miny = 9999 ; maxy = -9999 ; lk = "<br>Author:"
  for iii in range(ntot):
    # 1. get and prepare various components
    danom = nom[iii].strip().split()[0] ; daprenom = prenom[iii].strip().split()[0]
    dayears = int(anneedeb[iii]) ; dayeare = int(anneefin[iii])
    daini = initiales[iii].split()[0]
    if usercond is None: cc = ''' -c ' '''
    else: cc = usercond + ''' -c ' '''
    nomarr = nom[iii].split()
    cc = cc + ''' author:"'''+nomarr[0]+'''" '''
    if len(nomarr) > 1:
     for zenom in nomarr[1:]:
       cc = cc + ''' or author:"'''+zenom+'''" '''
    cc = cc+''' ' '''
    # -- if year start 0000 and year end 0000 do not do anything
    if dayears + dayeare != 0:
      if dayears == 0: dayears = anneec
      if dayeare == 0: dayeare = anneec
      # 2. info
      print danom+"-"+daprenom+"-"+str(dayears)+"-"+str(dayeare)
      # 3. make page
      if oneyear is None: ly = range(dayeare,dayears-1,-1)
      else: ly = [oneyear]
      if (perso and (eqeq != 'all')):
        ads.makepage('lmd_'+danom.replace(" ", ""),\
                 retrieve = False,\
                 customcond = cc,\
                 listyear = ly,\
                 linkads = dalink,\
                 title = titpre+daprenom+" "+danom+titsuf,\
                 printnum = True,\
                 verbose = False,\
                 includemonth=True,\
                 target = folder)
      # 4. get intervals of years for the whole lab
      if oneyear is None:
        if dayears < miny: miny = dayears
        if dayeare > maxy: maxy = dayeare  
      # 5. get authors link list
      lk = lk + ''' <a href="lmd_'''+danom.replace(" ", "")+'''.html">'''+daini+" "+danom.replace('é',"&eacute;")+"</a> /"
 
  ### MAKE FINAL PAGE
  if oneyear is None: ly = range(maxy,miny-1,-1)
  else: ly = [oneyear]
  ads.makepage('lmd_'+eqeq.strip(),\
               retrieve = False,\
               listyear = ly,\
               linkads = dalink,\
               title = "<CENTER><H2><EM><font color='#B8860B;'>Peer-reviewed publications for team "+eqeq.strip()+"</font></EM></H2></CENTER>",\
  	       addlink = lk,\
               customcond = usercond,\
               printnum = True,\
               includemonth=True,\
               verbose=False,\
               target = folder)

### CLEAN 
os.system('rm -rf *dummy*')
#os.system('rm -rf '+folder+'*.link*')

