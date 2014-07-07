# -*- coding: utf-8 -*- 
# Copyright (c) 2014 - Yuxiang Zhang <rico.zhang9318@gmail.com> 
# I got Resources.for.WCAF.txt from http://www.dancinghenryalmanac
#.com/world-cup-folding-arms/random-player.html
# In honour of world-wide football fans, I give my thanks to their fabulous job.

import csv,os

#Change Current Path as Working Path
path=os.getcwd()
os.chdir(path)

reader=csv.reader(open('Resources.for.WCAF.txt','r'),delimiter='@')
f=open('Resources.for.WCAF.01.txt','w+')

##Clean&Reorganize the data 
rows_so_far=0   
for row in reader:
    rows_so_far+=1    
    if rows_so_far<266:
        f.write(str(row[1])+','+str(row[3])+','+str(row[5])+',\n')
    else:
        f.write(str(row[1])+',\n')

f.close        
