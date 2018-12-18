# PROJECT ASSIGNMENT 2
# CS-111 GREEN
# UIC, NOVEMBER 2016

import random

# QUESTION 1:

def makeFounders(red, purple, blue):
    """This function creates a random list that corresponds to a population with the given number of organisms of each type."""
    myList_r = []
    myList_p = []
    myList_b = []
    for x in range(red):
        myList_r.append("r")
    for y in range(purple):
        myList_p.append("p")
    for z in range(blue):
        myList_b.append("b")
    myList = myList_r + myList_p + myList_b
    random.shuffle(myList)
    return myList
	
# QUESTION 2:

def matePairOnce(x,y):
    """This function chooses one of the alleles that correspond to the type of each parent and creates an offspring (child) of the type that corresponds to that allele pair."""
    myList = []
    if x == "r" and y == "r":
        myList = ["r"]
        return myList
    if x == "b" and y == "b":
        myList = ["b"]
        return myList
    if x == "p" and y == "p":
        j = random.choice(["r", "p", "b"])
        myList = [j]
        return myList
    if (x == "r" and y == "p") or (x == "p" and y == "r"):
        m = random.choice(["r", "p"])
        myList = [m]
        return myList
    if (x == "r" and y == "b") or (x == "b" and y == "r"):
        myList = ["p"]
        return myList
    if (x == "b" and y == "p") or (x == "p" and y == "b"):
        n = random.choice(["b", "p"])
        myList = [n]
        return myList

# QUESTION 3:

def matePair(x,y,num):
    """This function returns a list with the required number of offspring, each generated in a way described for matePairOnce()."""
    myList = []
    for index in range(num):
        myList = myList + (matePairOnce(x,y))
    return myList 
		
    
# QUESTION 4:

def createGeneration(myL,n):
    """This function mates the first organism with the second, the third with the fourth, etc, each mating producing the required number of offspring. It returns the list with the ospring appended to the original list of organisms."""
    random.shuffle(myL)
    if len(myL) % 2 != 0:
        myL = myL[:-1]
    new_list = []
    for x in range(n):
        for i in range(len(myL[::2])):
            new_list = new_list + matePairOnce(myL[i],myL[i+1])
    return new_list


# QUESTION 5:

def calcFreq(myL):
   """This function calculates the relative frequencies of red, purple, and blue organisms in it and returns it as a list of 3 numbers."""
   counter_r = 0
   counter_p = 0
   counter_b = 0
   for r in range(len(myL)):
       if myL[r] == "r":
           counter_r = counter_r + 1.0
   for p in range(len(myL)):
       if myL[p] == "p":
           counter_p = counter_p + 1.0
   for b in range(len(myL)):
       if myL[b] == "b":
           counter_b = counter_b + 1.0
   return [counter_r/len(myL),counter_p/len(myL),counter_b/len(myL)]


# QUESTION 6:

def popSim(red, purple, blue, offspring, gen):
    """This function creates the founder population and proceeds to create 'gen' generations by mating paris that produce 'offspring' number of offspring"""
    for i in range(0,gen):
        L = createGeneration(makeFounders(red, purple, blue), offspring)
        return calcFreq(L)
