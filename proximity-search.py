##Author: Rishabh Dalal
##Description: Processing phrase queries using proximity search

import sys
import os
import os.path
from linkedList import LinkedList

def main():
    
    dictionary = {}
    print("Creating the posting lists...")
    docID = {}
    docInt = 1
    true_dict = {}

    directoryList = os.listdir('.')
    for dirItem in directoryList:
        if dirItem[-4:] == ".txt":
            docID[dirItem.replace(".txt", '').strip()] = docInt
            createIndex(dirItem, docInt, dictionary)
            docInt += 1

    """
    ##Printing following data of all docs: word, occuring in doc : indices in doc
    for i in dictionary.keys():
        print(i)
        for j in dictionary[i]:
            print(j[0], ":", end=" ")
            printll(j[1])
        print()
    """
    
    phrase = input("Enter the phrase: ")
    query = phrase.lower().split()
    queryDict = {}
    for i in range(len(query)):
        queryDict[query[i]] = i

    docIdToProcess = getIntersectingDocIds(dictionary, query)

    askedDict = {}
    for ids in docIdToProcess:
        for k in dictionary[query[0]]:
            if k[0] == ids:
                askedDict[ids] = k[1]
    
    for cin in query[1:]:
        for ids in docIdToProcess:
            for k in dictionary[cin]:
                if k[0] == ids:
                    askedDict[ids] = combineLists(askedDict[ids], k[1], queryDict[cin])

    keys = askedDict.keys()
    queriedDocs = []
    for i in keys:
        if not askedDict[i].isEmpty():
            queriedDocs.append(i)

    print("The phrase occurs in following documents:", queriedDocs)

def getIntersectingDocIds(dyct, cin):
    ## Getting docs ids of all the documents in which all the words
    ## of the phrase occurs

    docId = set()
    if cin[0] in dyct:
        for doc in dyct[cin[0]]:
            docId.add(doc[0])
    else:
        print("No intersection")
        sys.exit()
    
    for query in cin[1:]:
        if not query in dyct:
            print("No intersection")
            sys.exit()
            
        docIdTemp = set()
        for doc in dyct[query]:
            docIdTemp.add(doc[0])
        docId = docId & docIdTemp

    print("All individual word of phrase occurs in docs:", list(docId))
    return docId

def combineLists(a, b, off):
    ##Combining two linked lists to find if they contain consecutive indices
    
    temp = LinkedList()
    p1 = a._head
    p2 = b._head

    while p1 and p2:

        if p1.getData() + off == p2.getData():
            temp.add(p1.getData())
            p1 = p1.getNext()
            p2 = p2.getNext()

        elif p1.getData() < p2.getData():
            p1 = p1.getNext()

        elif p2.getData() < p1.getData():
            p2 = p2.getNext()

    return temp

def printll(lyst):
    ##Printing a linked list
    
    head = lyst._head
    while head:
        print(head.getData(), end=" ")
        head = head.getNext()
    print()
                  
def processWord(word):
    ##Normalising a token

    word = word.strip()
    while word[-1] in ".,:;'/@$":
        word = word[:-1]

    while word[0] in ".,:;'/@$":
        word = word[1:]
    return word.lower()

def createIndex(filename, doc_id, dictionary):
    ##Creating a dictionary and postings

    file = open(filename, 'r')
    wordCount = 0
    for line in file:
        line = line.strip().split()
        for word in line:
            word = processWord(word)
            if word in dictionary:
                flag = False
                count = 0
                for j in dictionary[word]:
                    if j[0] == doc_id:
                        flag = True
                        dictionary[word][count][1].add(wordCount)
                    count += 1
                if not flag:
                    newLinkedList = LinkedList()
                    newLinkedList.add(wordCount)
                    dictionary[word].append([doc_id, newLinkedList])
            else:
                newLinkedList = LinkedList()
                newLinkedList.add(wordCount)
                dictionary[word] = [[doc_id, newLinkedList]]
            wordCount += 1

    file.close()

main()
