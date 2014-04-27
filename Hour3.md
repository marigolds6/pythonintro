### [More on Lists](http://docs.python.org/2/tutorial/datastructures.html#more-on-lists)  
* Concatenation (+) versus append() versus extend()  
* pop()  
* index() and ```in```  
* reverse() and sort()  
* Comprehensions
```
heartylaugh = [x for x in 'abracadabra' if x not in 'abc']
```
  
### [Flow Control](http://docs.python.org/2/tutorial/controlflow.html) (through 4.5)
* if and else
* while
* for
* range() (Another Python 3 note)


### Useful tools
#### setuptools (easy_install)  
setuptools -> distribute -> setuptools  
[What is the difference?](http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2/6522905#6522905)  
  
#### easy_install (part of setuptools)-> pip  
[How to install pip on Windows](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows)  
[An Easy Guide to Install Python or Pip on Windows](http://arunrocks.com/guide-to-install-python-or-pip-on-windows/)  
pip can uninstall  
But... easy_install works better on windows because it handles binaries.  
  
### Another option  
[pip for windows](https://sites.google.com/site/pydatalog/python/pip-for-windows)  
What does it do?  
Why use other options?  
  
##Scope  
Namespace, including __main__  
  
###[Scope Hierarchy](https://docs.python.org/2/tutorial/classes.html) (9.2 Only)  
1.the innermost scope, which is searched first, contains the local names
2. the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
3. the next-to-last scope contains the current module’s global names
4. the outermost scope (searched last) is the namespace containing built-in namesthe innermost scope, which is searched first, contains the local names

###The namespace script
```
a = 0
def myName():
    print "When called by a function in my namespace, my name is", __name__
def whatisa():
    a = 1
    print a
def whatisglobala():
    global a
    print a
print "Right now, my name is:", __name__
```
