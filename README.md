# Challenge_Hacker_Rank

It is a test using python, Docker, Flask and SWAGGER.

# 1) Python 

# The Topic: 
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. 
Return an array of the results.

# Example

Strings= ['ab', 'ab' , 'abc']
querries = ['ab', 'abc' , 'bc']
resultat = [2,1,0]

# The suggestion: 
cleanning up the code a bit and put it in a class which will be in a separate python module (another file) and making a "main" which uses this class. Indeed, we will have:
SparseArray.py  as a class that contains the function to calculate the occurence
main.py as the main where we will use this function

# The solution:
SparseArray.py 
Class that contains: Simple constructor
The function matchingStrings function: count the occurence of querries on strings using counter 
This function take in parameters strings that will be taken from the textfile.
The function must return an array of integers representing the frequency of occurrence of each query string in strings.
main.py 
it contains the INPUT_PATH that is the  environment variable as a text file
querries are taken from the command  that we will launch to execute the main
The count the queries
the use of the function matchingStrings denined on the class SparseArray on SparseArray.py 

# Execution of main.py
When we Launch python -m main ab,abc,bc we have the result that we want to have 

# Docker:

In order to run our program on Docker is an open platform for developing  and running applications. 
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. 
So we must 
a) install Docker 
b) Creation of a Docker file, in this file we must write all the requirements that we had used:
Python 3.7
requirements.txt ( it contains all the package that we need to install on Docker to run easaly our program
Entrypoint ( here we must put python and the script that we want to run which is main.py )
c) Docker build -t 
d) Docker run -- name test main.py ab abc bc ( It's the same CMD that we had launched to run our main.py but on Docker :) ) 

If we use all these steps we will have the result on Docker.

# Flask: 

Flask is a web micro framework that allow you to build a web application.
We retun on our main.py and we add the instructions that activate Flask on our program:
we instantiate Flask using app = Flask(__name__), we created a new route - / which renders an index.html file from the templates folder.









