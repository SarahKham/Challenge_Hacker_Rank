import sys
import os
from SparseArray import SparseArray
from collections import Counter
from flask import Flask
from flask import request
  

server = Flask(__name__)

# INPUT_PATH is the  environment variable wich is a text file
os.environ['INPUT_PATH'] = 'filename.txt'
# read the environment variable
string_input = open(os.environ['INPUT_PATH'], 'r')
#split the lines at line boundaries
strings = string_input.read().splitlines()

@server.route("/", methods = ["POST"])
def hello():
    global SparseArray
    data=request.get_json()
    v1=data.get('v1','')
    v2=data.get('v2','')
    v3=data.get('v3','')
    print('*****')
#the use of the constructor of the class SparseArray on SparseArray.py 
    SparseArray = SparseArray(strings,[v1,v2,v3])
#the use of the function matchingStrings denined on the class SparseArray on SparseArray.py 
    res = SparseArray.matchingStrings(SparseArray)
    print(res)
    return 'This is our result'


if __name__ =="__main__":
   server.run(host='0.0.0.0')
