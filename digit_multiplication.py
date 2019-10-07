#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
A program which calculates how many times we have to multiply the digits of a number 
in order to get one digit result.
'''

import math

#This is the function
def multiTimes (val):
        x=0
        '''
        first case is for one digit numbers, there could be a way to include the multi digit numbers 
        that their digits if multiplied result to one digit number to first case, for instance 21, 312
        '''     
        
        if val<10:
                x=1
                print "total multiplications needed to get a 1 digit number is ", x
                return;
        else:
                while val >= 10:
                        #get number's length
                        length = int(math.log10(val))+1
                        print "The number's ", val, "length is ", length
                        z=1
                        for i in range(1, length + 1):                             
                                #get last digit from remainder by 10
                                y = val%10
                                print "the digit", length +1 - i, "is ", y
                                #subtract last digit and divide by 10 to get number with one less digit
                                val = (val-y)/10
                                #calculation of digit multiplication
                                z=z*y
                                           
                        x=x+1
                        #if the result in one digit it terminates, else we continue 
                        #using the the multiplication of digits as next number
                        val = z
                        print "the new number which is the result of the multiplication is ", val
                        
                print "total multiplications needed to get a 1 digit number is ", x
                return;


#main
#We check for user input
while True:
        number  = int(input('Enter a positive number: '))        
        try:
                val = int(number)
                if val < 0:
                        print("Sorry, input must be a positive integer, try again")
                        continue
                break
        except ValueError:
                print("That's not an integer!")

 
print "Your number is ", val


#call the function
multiTimes( val );
print "Press enter to exit"
raw_input()

