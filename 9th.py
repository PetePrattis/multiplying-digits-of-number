#!/usr/bin/python
# -*- coding: utf8 -*-

'''
Εργασία από τον μαθητή Παναγιώτη Πράττη Π15129 και Νίκο Κοντόπουλο Π15056
Άσκηση 9
Γράψτε μία συνάρτηση η οποία υπολογίζει το πόσες φορές πρέπει να πολλαπλασιάσω
τα ψηφία ενός αριθμού που παίρνει ως όρισμα, ωστε το αποτέλεσμα να βγει μονοψήφιος.
'''


import math


#Αυτή είναι η συνάρτηση
def multiTimes (val):
        x=0
        #1η περίπτωση για αν είναι μονοψήφιος αριθμός, φυσικά υπάρχουν και πολλοί
        #διψηφιοι(π.χ. 21), τριψίφιοι(π.χ. 312)... των οποιών το γινόμενο των ψηφίων τους κάνει μονοψήφιο με
        #1 προσπάθεια αλλά επέλεξα να τους συμπεριλάβω αυτούς και όλους τους υπόλοιπους αριθμούς στην άλλη περίπτωση
        #όπου κάνω ολόκληρη διαδικασία για να βρω το x 
        
        
        if val<10:
                x=1
                print "total multiplications needed to get a 1 digit number is ", x
                return;
        else:
                while val >= 10:
                        #βρίσκω το μήκος του αριθμού
                        length = int(math.log10(val))+1
                        print "The number's ", val, "length is ", length
                        z=1
                        for i in range(1, length + 1):
                                
                                #βρίσκω το υπόλοιπο που ειναι το τελευταίο ψηφίο
                                y = val%10
                                print "the digit", length +1 - i, "is ", y
                                #π.χ. y=123%10=3
                                #διαμορφώνω τον αριθμό ώστε στην επόμενη επανάληψη το υπόλοιπο να είναι το προτελευταίο ψηφίο
                                val = (val-y)/10
                                #π.χ. val=(123-3)/10=120/10=12
                                #αυτό θα υπολογίζει το γινόμενο των ψηφίων
                                z=z*y
                               
                              
                        x=x+1
                        #αν το γινόμενο είναι μονοψήφιος τελος, αλλιώς συνεχίζουμε έχοντας για νέο αριθμό το γινόμενο των ψηφίων
                        val = z
                        print "the new number which is the result of the multiplication is ", val
                        
                print "total multiplications needed to get a 1 digit number is ", x
                return;



#'Ελεγχος του αριθμού που εισάγει ο χρήστης
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


#εδώ καλώ την συνάρτηση
multiTimes( val );
print "Press enter to exit"
raw_input()




