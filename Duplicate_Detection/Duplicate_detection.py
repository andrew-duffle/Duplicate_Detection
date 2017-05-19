#-*- coding: utf-8 -*-
#!/bin/bash

import sqlite3
import os 
import re


conn = sqlite3.connect('frequentcomments.db')
c = conn.cursor()

c.execute(''' Create Table frequentcomments (
                    Comment1Comment2 Text,
                    likeness real)''')

comment=[]

with open('discussions.thorn') as fp:
    contents=fp.read().lower()
    contents=re.sub(r'[^\w\s]','',contents)
    for entry in contents.split('þ'):
        comment.append(entry)
 

     
comp1=0
comp2=1    

while comp1 < len(comment):    
        
    while comp2 < len(comment):        
           
        testingfile1=open("Test3.txt",'w')
        testingfile1.write(comment[comp1])
        testingfile1.close()
        
        wordlist1=open("wordlist1.txt",'w')
        
        with open("Test3.txt") as infile:
            xo=sorted(set(infile.read().split()))
            for word in xo:
                wordlist1.write(word + '\n')
        wordlist1.close()        
        
        
        
        testingfile2=open("Test4.txt",'w')
        testingfile2.write(comment[comp2])
        testingfile2.close()
        
        wordlist2=open("wordlist2.txt",'w')
        
        with open("Test4.txt") as infile2:
            xo2=sorted(set(infile2.read().split()))
            for word2 in xo2:
                wordlist2.write(word2 + '\n')
        wordlist2.close()   
        
        #############################Linux compare and diff
        
        x = 'wordlist1.txt'
        y = 'wordlist2.txt'
        compare='diff ' + x +' '+ y +' > tmp'
        os.system(compare)
        results = open('tmp','r').read()
        differntlines= (results.count('>') + results.count('<'))
        with open (x) as file1:
            linesin1= (sum(1 for _ in file1))
        with open (y) as file2:
            linesin2= (sum(1 for _ in file2))
        
        matching='comm -12 ' + x + ' ' + y +'>tmp2'
        os.system(matching)
        matches=open('tmp2','r').read()
        matchingwords=(matches.count('\n'))
        
        
        likeness = (((matchingwords/(linesin1 + linesin2 -matchingwords))*.6)+
                ((1-(differntlines/(linesin1 + linesin2)))*.4))
        comp2=comp2 + 1
        C1C2=(str(comp1 +1) + ' ' + str(comp2) )

        c.execute("Insert Into frequentcomments (Comment1Comment2,likeness) values (?,?)",
                                (C1C2, likeness))
        conn.commit()
        
    comp2=comp1+2
    comp1=comp1+1

for row in c.execute('Select Comment1Comment2 from frequentcomments order by likeness desc' ):
    print(row)

conn.execute(''' Drop Table frequentcomments''')    
conn.close() 
 