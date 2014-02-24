#-*- coding:utf-8 -*-
#from sys import argv 
#script, first, second, third = argv
#
#print "The script is called:", script
#print "Your first variableis is:", first
#print "Your second variableis is:",second
#print "Your third variableis is:", third


#raw_input()和argv不能合起来用。
x = raw_input('? ') 
from sys import argv
script,list1,list2 = argv
print "The script is called:", script
print "Your first variableis is:", list1
print "Your second variableis is:", list2


list1 = raw_input("What's list1's name?")
list2 = raw_input("What's list2's name?")