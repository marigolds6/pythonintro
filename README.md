# Introductory Geoprocessing with Python

This course will get you up and running with python in four sections. We still
start with installation, including installation with ArcGIS, integrated
development environments (IDEs) and where to find more help. Next, we will
cover basic syntax, import statements, writing functions, and adding
additional libraries and site packages to your installation. For the third
section of the class, we will dive into python programming basics: variables,
scopes, datatypes, flow control, debugging, and error handling. The class will
wrap up by covering common data structures and an introduction to libraries
with the widely used os and datetime modules. You should have a very basic
understanding of script writing, as we will be up and running with our own
scripts by the end of the class. Knowledge of basic flow control (if-then-
else, for loops, while loops) is recommended.

First [Download the course
materials](http://maptest.stlouisco.com/python/stlco.zip)

While you are downloading, do the [Python Intro
Survey](http://www.surveymonkey.com/s/HRY3YSK)

## Hour One - This new learning amazes me, Sir Bedevere.

Explain again how sheep's bladders may be employed to prevent earthquakes.

  * Installation demo
    * How to check for 64-bit
    * Where to get Python:
      * [Python.org](http://www.python.org/download/)
      * [IronPython](http://ironpython.codeplex.com/)
      * [ActivePython](http://www.activestate.com/activepython/downloads)
  * Installation Help
    * [Python on Windows](http://docs.python.org/2/using/windows.html)
    * Installs to: C:\Python27
    * Run: set path=%path%;C:\python27
    * Running scripts: python vs. pythonw
  * More Help
    * [Python Documentation](http://docs.python.org/2/contents.html)
    * [Python Tutorial](http://docs.python.org/2/tutorial/)
    * [Python Language Reference](http://docs.python.org/2/reference/index.html)
  * IDE introduction: We will use IDLE
    * [IDE List](http://wiki.python.org/moin/IntegratedDevelopmentEnvironments)
    * [Great advice](http://stackoverflow.com/questions/81584/what-ide-to-use-for-python)
    * [One Day of IDLE Toying](https://hkn.eecs.berkeley.edu/~dyoo/python/idle_intro/index.html)

## Hour Two - That's enough music for now, lads...
### Looks like there's dirty work afoot.  
  
  * [An Informal Introduction to Python](http://docs.python.org/2/tutorial/introduction.html)
  * [More on Lists](http://docs.python.org/2/tutorial/datastructures.html#more-on-lists)
  * [More Control Flow Tools](http://docs.python.org/2/tutorial/controlflow.html) (through 4.5)

## Hour Five! Three sir. Three! - We write a module and get some practice

  * The import Statement
  * [arcpy](http://resources.arcgis.com/en/help/main/10.1/index.html#//000v00000001000000)
  * [Defining Functions](http://docs.python.org/2/tutorial/controlflow.html#defining-functions) (4.6-4.7.3)
  * [Scope](http://docs.python.org/2/tutorial/classes.html) (9.2 only)
  * standard library, modules, and packages (and how to add them)
    * [Start Here](http://docs.python.org/2/tutorial/modules.html)
  * More arcpy Examples
  * [Syntax Errors](http://docs.python.org/2/tutorial/errors.html#syntax-errors)
  * [Exceptions](http://docs.python.org/2/tutorial/errors.html#exceptions)
  * [Handling Exceptions](http://docs.python.org/2/tutorial/errors.html#handling-exceptions)

## Hour Four - It's only a model.

  * [Data Structures](http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences) (5.3-5.5)
  * [os](http://docs.python.org/2/tutorial/stdlib.html#operating-system-interface) module (10.1)
  * [datetime](http://docs.python.org/2/tutorial/stdlib.html#dates-and-times) module (10.8)
  * [Executing Scripts](http://docs.python.org/2/tutorial/interpreter.html#executable-python-scripts) (2.2.2)
Examples:

  * Select Address Points using attributes
  * Select parcels using location
  * Run a buffer analysis against streets
    * Find parcels adjacent to centerlines
    * Find address points in parcels
  * Create geocoder from source files
    * Subset using attributes
    * Subset using location
  * os: Copy around file geodatabase
  * synchronize replicas

