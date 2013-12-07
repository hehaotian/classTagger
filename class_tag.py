# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:46:25 2013

@author: haotianhe
"""

class List():
    
    def __init__(self):
        self.List = dict()
        name = set(["jack", "jill"])
        num = set(["one", "two", "three", "four", "five", "six", "seven",
                   "eight", "nine"])
        self.List = {"NAME" : name, "NUM" : num}

    def addNewSet(self, name, s):
        self.List[name] = s

    def updateNewItem(self, name, v):
        self.List[name].add(v)

    def returnList(self):
        return self.List

class classtagger():
    
    untagged = []
    tagged = []
    classTagged = []
    
    def __init__(self, sent):
        self.sent = sent  
        self.sentlow = sent.lower()
    
    def mapping(self, List):   
        for word in self.sent.lower().split(" "):
            tag = False
            for k, v in List.iteritems():
                for item in list(v):
                    if word == item:
                        self.__class__.tagged.append(word)
                        self.__class__.classTagged.append(k)
                        tag = True
            if tag == False:
                self.__class__.untagged.append(word)
                self.__class__.classTagged.append(word)

    def printResults(self):
        print "The answers should be:"
        print "input:\t" + sent
        print "untagged:\t" + ' '.join(self.__class__.untagged)
        print "tagged:\t" + ' '.join(self.__class__.tagged)
        print "class tagged:\t" + ' '.join(self.__class__.classTagged)
        

newdef = List()
newdef.addNewSet("HOBBY", set(["football"]))
newdef.updateNewItem("HOBBY", "soccer")
newdef.addNewSet("VOCATION", set(["students"]))
newdef.updateNewItem("NAME", "haotian")
newdef.addNewSet("SEX", set(["male", "female"]))
# The List name should always define as List here
List = newdef.returnList()

sent = raw_input()
test = classtagger(sent)
test.mapping(List)
test.printResults()