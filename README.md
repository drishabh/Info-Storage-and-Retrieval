# Info-Storage-and-Retrieval

1. boolean-retrieval ... Implementation of boolean retrieval system using inverted indexing. The system only supports conjunctive queries,
                         although it also contains the code for disjunctive queries for text file. There are three other documents attached
                         to test it upon namely document1.txt, document2.txt, document3.txt. Posting lists are saved as linked lists, which
                         in themselves are values whose keys are tokens hashed using a dictionary. It does multiple conjuctions in a
                         way to minimize run-time by processing the boolean queries in increasing order of frequencies of the tokens.
                         
2. linkedList ... Contains the Node class, Skipped Node class that inherits from Node class and Linked list class to facilitate in making                     posting lists. Skipped Node class facilitates in creating posting lists that contains skip pointer for finding faster 
                  posting lists intersection.
                
3. skippedList.py ... Contains the implementation of posting lists containing skip pointers and class SkippedList, which inherits from linked list and gives each node the extra skip pointer for finding posting list intersection faster. For a posting list of length P, √P evenly spaced skip pointers are used. It also contains various other functions for finding the intersection of posting lists using skip pointers and for changing a simple posting list to have skip pointers. 

4. Edit_Distance.java ... Levenshtein's algorithm to quantify how different two strings are. Replacement, Insertion and deletion of character are considered as basic operations each having the same overhead. The algorithm uses dynamic programming and it has run-time of O(n.m). It asks for two input strings from console and returns the edit distance. It can also print the steps to change one string into another and the intermediate table formed while solving.

5. proximity-search.py ... Implementation of phrase queries using posting lists having positional indexes. Preprocessing includes creating the posting lists containing key and its index in different (text) documents.
