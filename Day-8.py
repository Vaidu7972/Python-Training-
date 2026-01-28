""" 
SET
collection of unorder items
items are unique ,sets are mutable but values/elements are immutable
dublicate values  allow but set ignores(i.e consider as one)
"""

set={1,2,3,4,"vaidehi","doke",True,98.0,5}
print(set)
print(type(set))
print(len(set))

#  EMPTY SET
null_set=()             # wrong. this is tuple 
null=set;{}             #correct way to create empty set
print(type(null_set))
print(type(null))
print("\n")

#  METHODS IN SET 
set={10,20,50}
set.add(30)
print(set)
print(len(set))

set.remove(20)
print(set)

set.pop()
print(set)

set.clear()
print(set,"\n")


set.discard(100)          #if element not found no error
print(set)

#  UNION & INTERSECTION of SETS

set1={1,2,3}
set2={3,4,5}
set3=set1.union(set2)          #union
print(set3)

set4=set1.intersection(set2)   #intersection
print(set4,"\n")    

#  Examples ( LIST, SET, TUPLE, DICTIONARY)

#LIST
"""- ordered collection of items
   - mutable (can change)
   - allow duplicate values
""" 

#  SET
"""- collection of unorder items
   - items are unique ,sets are mutable but values/elements are immutable
   - dublicate values  allow but set ignores(i.e consider as one)
"""

# TUPLE
"""- ordered collection of items
   - immutable (can NOT change)
   - allow duplicate values
"""

# DICTIONARY
"""- collection of key:value pairs  (unorder, mutable, don't allow duplicate keys.)
""" 


"""EX 1: Two stu are follow diff subject are there find how much classes required to complete all subject
A=java c++ python js
B=java python java c++ c"""

sub={
    "java","c++","python","js",
    "java","python","java","c++","c"
    }
print(sub)
print(len(sub))


"""EX 2 : enter marks of 3 sub from user and store in dic.
start with empty dic and add one by one .
use sub name as key and marks as value."""

marks={}
sub1=input("enter 1 subject name: ")
mark1=int(input("enter marks: "))

sub2=input("enter 2 subject name: ")
mark2=int(input("enter marks: "))   

sub3=input("enter 3 subject name: ")
mark3=int(input("enter marks: "))

marks[sub1]=mark1
marks[sub2]=mark2
marks[sub3]=mark3
print(marks)
print("\n")
