# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 22:37:16 2016

@author: wsdula
"""
def AreaCoord(n, someset):
    AllPaths = someset
    g = n
    if g>6:
        x = len(AllPaths)
        i = 0
        while i < x:
            q = someset[i][0]
            r = someset[i][1]
            s = someset[i][2]
            if [q,r,s+1] not in someset and s+1 < g: 
                AllPaths.append([q,r,s+1])
                i += 1
            else:
                i += 1
            
        AllPaths.append([g-2,g-1,g-1])
        
        j = 1
        while j <= (g-4):
            AllPaths.append([g-3-j,g-2,g-1])
            j += 1
    else:
        return AllPaths
        
    AreaCoord(g-1, AllPaths)
    return AllPaths
    
def Transform(n, someset):
    ans = int(input("Would you like to get the area 4 vectors? "))
    if ans == 4:
        i = 0
        x = len(someset)
        while i < x:
            q = someset[i][0]
            r = someset[i][1]
            s = someset[i][2]
            if r == s:
                j = s + 1
                while j < n:
                    if [q,r,s,j] not in someset:
                        someset.append([q,r,s,j])
                        
                    j += 1
                    
            if r == s - 1:
                j = s
                while j < n:
                    if [q,r,s,j] not in someset:
                        someset.append([q,r,s,j])
                        
                    j += 1
            
            someset.remove(someset[0])
            i += 1
    else:
        return someset
    return someset

'''SORTING ALGORITHM'''
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

''' THIS IS WHERE THE MAIN PROGRAM BEGINS '''
n = int(input("How long are the paths? "))
BaseCase = [[1,2,2], [2,3,3], [3,4,4], [4,5,5],
            [1,2,3], [2,3,4], [3,4,5], [1,2,4],
            [1,2,5], [1,3,5], [1,3,4], [1,4,5],
            [2,3,5], [2,4,5]]  #Makes base case unordered

quickSort(BaseCase)
NewCase = AreaCoord(n, BaseCase)
quickSort(NewCase)
Case = Transform(n, NewCase)
quickSort(Case)   

i = 0
while i < len(Case):
    print(Case[i])
    i += 1

