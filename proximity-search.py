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

    for i in dictionary.keys():
        print(i)
        for j in dictionary[i]:
            print(j[0], ":", end=" ")
            printll(j[1])
        print()

    phrase = input("Enter the phrase: ")
    query = phrase.lower().split()

    intersectId = []
    for i in query:
        if not i in dictionary:
            print("No intesection")
            sys.exit()
        else:
            for j in dictionary[i]:
                lyst = getList(j[1])
                lyst.insert(0, j[0])
                intersectId.append(j[0])

def getList(lyst):
    ##Converting a linked list to python list
    
    l = []
    head = lyst._head
    if head:
        while head:
            l.append(head.getData())
            head = head.getNext()
    return l

def combineListsNot(a, b, f1, f2, total):
    ##Combining two linked lists to find intersect if there is

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
