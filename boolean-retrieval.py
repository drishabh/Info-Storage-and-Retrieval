##Author: Rishabh Dalal
##Description: Processing boolean queries

import sys
import os
import os.path
from linkedList import LinkedList
from operator import itemgetter

"""
    1 ... process not of boolean
    2 ... process as it is
"""
def main():
    
    dictionary = {}
    notDict = {}
    print("Creating the posting lists...")
    docID = {}
    docInt = 1
    true_dict = {}

    totalDocs = 0
    directoryList = os.listdir('.')
    for dirItem in directoryList:
        if dirItem[-4:] == ".txt":
            totalDocs += 1


    for dirItem in directoryList:
        if dirItem[-4:] == ".txt":
            docID[dirItem.replace(".txt", '').strip()] = docInt
            createIndex(dirItem, docInt, dictionary)
            docInt += 1

    query = input("Enter a conjective boolean query (NOT A AND B AND C): ")
    query = query.lower().split("and")

    if len(query) == 1:
        answer = oneQuery(query, dictionary, totalDocs)
    
    else:
        for i in query:
            i = i.strip().split()
            if len(i) > 1:
                notDict[i[1].strip()] = 1
            else:
                notDict[i[0].strip()] = 0
        
        processing_order = processQuery(query, dictionary)
        answer = intersect(processing_order, dictionary, query, notDict, totalDocs)

    print("Requested query matches to following docIds: ", end="")
    if answer.length() == 0:
        print(0)
    else:
        for i in answer:
            print(i, end=" ")

def oneQuery(query, dict1, total):
    ##Processing a single query

    temp = LinkedList()
    query = query[0].split()
    for i in query:
        i == i.strip()

    if len(query) == 1:
        temp = dict1[query[0]]
    else:
        temp = dict1[query[1]]
        for i in range(1, total+1):
            if temp.search(i):
                temp.remove(i)
            else:
                temp.add(i)
    return temp
        
          
def processQuery(que, dictionary):
    ##Processing a query to understand it
    
    frequencyList = []
    flag = True
    for i in que:
        sub_query = i.strip().split()
        if sub_query[0] == "not":
            if not sub_query[1] in dictionary:
                frequencyList.append(0)
                flag = False
                print("No match")
                sys.exit()
            else:
                i = i.strip().split()
                if len(i) > 1:
                    i = i[1]
                frequencyList.append([dictionary[sub_query[1]].length(), i.strip()])
        else:
            if not sub_query[0] in dictionary:
                frequencyList.append(0)
                flag = False
                print("No match")
                sys.exit()
            else:
                frequencyList.append([dictionary[sub_query[0]].length(), i.strip()])
  
    frequencyList = sorted(frequencyList, key=itemgetter(0))
    return frequencyList

def intersect(order, dic, cin, notDict, total):
    ##Performing two smallest queries at a time
    ##not .. flag1 == 1
    
    flag1 = 0
    flag2 = 0
    if notDict[order[0][1]] == 1:
        flag1 = 1
    temp = dic[order[0][1]]
    p1 = 1
    while p1 < len(cin):
        current = order[p1][1]
        curr_list = dic[current]
        if notDict[current] == 1:
            flag2 = 1
        if flag1 == 0 and flag2 == 0:
            temp = combineListsConj(temp, curr_list)
        else:
            temp = combineListsNot(temp, curr_list, flag1, flag2, total)
        p1 += 1
        flag1 = 0
    return temp

def combineListsNot(a, b, f1, f2, total):
    ##Combining two linked lists to find intersect if there is atleast one not

    temp = LinkedList()
    p1 = a._head
    p2 = b._head

    while p1 and p2:

        if p1.getData() == p2.getData():
            if f1 == 1 and f2 == 1:
                temp.add(p1.getData())
            p1 = p1.getNext()
            p2 = p2.getNext()

        elif p1.getData() < p2.getData():
            if f1 == 0 and f2 == 1:
                temp.add(p1.getData())
            if f1 == 1 and f2 == 1:
                temp.add(p1.getData())
            p1 = p1.getNext()

        elif p2.getData() < p1.getData():
            if f1 == 1 and f2 == 0:
                temp.add(p2.getData())
            if f1 == 1 and f2 == 1:
                temp.add(p2.getData())
            p2 = p2.getNext()
            
    if (f1 == 1 and f2 == 0) or (f1 == 1 and f2 == 1):
       while p2 != None:
           temp.add(p2.getData())
           p2 = p2.getNext()

    if (f1 == 0 and f2 == 1) or (f1 == 1 and f2 == 1):
       while p1 != None:
           temp.add(p1.getData())
           p1 = p1.getNext()
    
    if f1 == 1 and f2 == 1:
        for i in range(1, total+1):
            if temp.search(i):
                temp.remove(i)
            else:
                temp.add(i)
    return temp
    
def combineListsConj(a, b):
    ##Combining two linked lists to find intersect
    
    temp = LinkedList()
    p1 = a._head
    p2 = b._head

    while p1 and p2:
        if p1.getData() == p2.getData():
            temp.add(p1.getData())
            p1 = p1.getNext()
            p2 = p2.getNext()
        elif p1.getData() < p2.getData():
            p1 = p1.getNext()
        else:
            p2 = p2.getNext()
    return temp

def processWord(word):
    ##Normilising a token

    word = word.strip()
    while word[-1] in ".,:;'/@$":
        word = word[:-1]

    while word[0] in ".,:;'/@$":
        word = word[1:]
    return word.lower()

def createIndex(filename, doc_id, dictionary):
    ##Creating a dictionary and postings

    file = open(filename, 'r')
    for line in file:
        line = line.strip().split()
        for word in line:
            word = processWord(word)
            if word in dictionary:
                if not dictionary[word].search(doc_id):
                    dictionary[word].append(doc_id)
            else:
                dictionary[word] = LinkedList()
                dictionary[word].add(doc_id)
            
    file.close()

main()
