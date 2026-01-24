# Tuple
"""
- build in data type  (stores int,str,float etc)
- Imutable seq of values, can NOT be change.
- tuple can not access as well as not change.
- index start from Zero.
"""
tup=(1,2,3,4,5)
print(tup)
print(type(tup))        #type
print(len(tup))         #length
print(tup[0])           #print 1st  
print("\n")

tuple=()                #zero value tuple
print(tuple)
print(type(tuple))
print(len(tuple))
print("\n")

tuple=(20,)         #right way of writting single value tuple
print(tuple)
print(len(tuple))
print(type(tuple))

tuple=(20)               #if we write single tuple without (,) then it is int type
print(type(tuple))
print("\n")

#  TUPLE SLICING:
"""- similar to list slicing
   - slicing is subset of tuple
"""
print(tup[:2])           
print(tup[1:])            
print(tup[1:3])          
print(tup[-3:-1]) 
print("\n")

#  TUPLE METHODS

tup=(1,2,3,4,5,2)
print(tup.index(1))
print(tup.index(5))           #index: used to find that value located at which index
print(tup.count(2))           #count: used to check how many times a value appears

#  EXAMPLES of list
Movies=[]
a=input("Enter 1 movies name:")
b=input("Enter 2 movie name: ")
c=input("Enter 3 movie name: ")
Movies.append(a)
Movies.append(b)
Movies.append(c)
print(Movies)
print(type(Movies))

a=[1,2,3]                                  #check Palindrom
b=[3,2,1]
a.reverse()
print(a)
if(a==b):
   print("Palindrome")
else:
    print("No") 
    
    
b=["c","d","a","a","b","b","b"]   
print(b.count("a"))                        #count of a

b.sort()                                   #sort a alphabetically
print(b)
b.reverse()                                #reverse order
print(b) 