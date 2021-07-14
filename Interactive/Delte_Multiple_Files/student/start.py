from os import remove
from sys import argv
import random
import string

i=0
while i<50:
	file_name = "student/save_me" + str(i) + ".txt"
	file = open(file_name, "w")
	file.close()
	i=i+1

i=0
while i<50:
	file_name = "student/sav" + str(random.choice(string.ascii_letters)) + "_me" + str(i) + ".txt"
	file = open(file_name,"w")
	file.close()
	i=i+1
    
i=0
while i<50:
	file_name = "student/save_me" + str(i) + ".tx" + str(random.choice(string.ascii_letters))
	file = open(file_name, "w")
	file.close()
	i=i+1
    
remove(argv[0])