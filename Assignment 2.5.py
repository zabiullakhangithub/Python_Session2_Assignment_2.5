# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:41:01 2018

@author: zabiulla.khan

Problem Statement 1:
Write a Python program using function concept that maps list of words into a list of
integers representing the lengths of the corresponding words.
Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as
[2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.

Problem Statement 2:
Write a Python function which takes a character (i.e. a string of length 1) and returns
True if it is a vowel, False otherwise.

"""
def LowToLoi(list1):
    inp_lst = []
    inp_lst = list1
    out_loi = []
    # Loop through the input list of words and identify/store the lengths
    for LOW in inp_lst:
        # Create a list of lenghts for the input words
        out_loi.append(len(LOW))
    #Display the lenghts of the words list
    print(out_loi)
    
LowToLoi(["Egg","Fish","Chicken","Meat"])

def checkifVowel(char):
    vowels =  ['a','e','i','o','u','A','E','I','O','U']
    #Check if passed char in function is an vowel or not and display true/false
    for letter in vowels:
        if char == 'a' or char=='A' or char == 'e' or char=='E' or char == 'i' or char=='I' or char == 'o' or char=='O' or char == 'u' or char=='U':
            return True
        else:
            return False

print(checkifVowel("E"))
print(checkifVowel("Z"))