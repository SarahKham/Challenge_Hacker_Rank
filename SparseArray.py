
from collections import Counter

class SparseArray:
#constructor of the class SparseArray
    def __init__(self, strings, queries):
        self.strings = strings
        self.queries = queries
#function that count the occurence of querries on strings using counter ( Counter dict subclass for counting hashable objects)
    def matchingStrings(self,SparseArray):
        c = Counter(SparseArray.strings)
        dic = {}
        for i in SparseArray.queries:
            dic[i] = c[i]           
        return (dic)