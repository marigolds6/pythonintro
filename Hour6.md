# [Data Structures are not funny](http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences) (5.3-5.5)
##Tuples
* Immutability! (Lists are not)  
* Usually heterogeneous (Lists are normally homogeneous)  
* Can be unpacked: ```x,y,z = (-90.4, 38.1, 630.0)```  
* Empty: ```t = ()```  
* Singleton: ```t = (u'Lonely',)```  
  
##Sets
Answers, "What is unique?"  
```
fruit = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print fruit
#Comprehensions too
a = {x for x in 'abracadabra' if x not in 'abc'}
```
  
##Dictionaries  
key:value pairs  
(Think like coded domains)  
```
#Sequence of key-value pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#Comprehensions
{x: x**2 for x in (2, 4, 6)}
#Simple
dict(sape=4139, guido=4127, jack=4098)
```
  
##Looping sequences  
* ```enumerate()``` creates index, value pairs from sequences to loop over  
* ```zip()``` zips two sequences together to loop over both at the same time  
* ```set.iteritems()``` gives you key:value pairs to loop over  

