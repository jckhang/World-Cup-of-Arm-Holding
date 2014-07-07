# -*- coding: utf-8 -*- 
# Copyright (c) 2014 - Yuxiang Zhang <rico.zhang9318@gmail.com> 
# I got all the resources from http://www.dancinghenryalmanac
#.com/world-cup-folding-arms/random-player.html
# In honour of world-wide football fans, I give my thanks to their fabulous job.

import csv,os,random

#Change Current Path as Working Path
path=os.getcwd()
os.chdir(path)

reader=csv.reader(open('Resources.for.WCAF.01.txt','r'),delimiter=',')
f=open('Words.for.players.txt','w+')

name=['' for i in range (266)]
mood=['' for i in range (22)]
reason=['' for i in range (81)]

rows_so_far=0
for row in reader:

    rows_so_far+=1
    if rows_so_far<266:
        name[rows_so_far]=str(row[0])
    else:
        if rows_so_far<287:
            mood[rows_so_far-265]=str(row[0])
        else:
            reason[rows_so_far-286]=str(row[0])
            
#Use Random to simulate the discription for each player
            
for i in range(1,265):

    name_now=name[i]

    a=random.randint(1,21)
    mood_now=mood[a]
    
    b=random.randint(1,80)
    reason_now=reason[b]

    f.write(name_now+' is '+mood_now+' because '+reason_now+'.'+'\n')

f.close
