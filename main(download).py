# -*- coding: utf-8 -*- 
# Copyright (c) 2014 - Yuxiang Zhang <rico.zhang9318@gmail.com> 
# I got all the resources from http://www.dancinghenryalmanac
#.com/world-cup-folding-arms/random-player.html
# In honour of world-wide football fans, I give my thanks to their fabulous job.

import urllib.request,csv,os

#Change Current Path as Working Path
path=os.getcwd()
os.chdir(path)

reader=csv.reader(open('Resources.for.WCAF.01.txt','r'),delimiter=',')
url0="http://www.dancinghenryalmanac.com/world-cup-folding-arms/gifs/"


rows_so_far=0
for row in reader:

    rows_so_far+=1
    if rows_so_far<266:
        url=url0+str(row[2])
        now=str(rows_so_far)+'.'+str(row[2])
        #Download "gif/1.Algeria-Carl_Medjani.gif"
        local=os.path.join(r"gif",now)
        urllib.request.urlretrieve(url,local)
    
