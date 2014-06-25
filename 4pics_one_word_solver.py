#imports iteration tools and the dictionary
import itertools
import enchant
import time

#lets the user input the bunch of letters and the space of the guess word
string = raw_input("Put in the letters given to you by 2pics one word:")
num = int(input("How many letters are in the word you have to guess?:"))

#gets first time
start_time = time.time()

#begins calculation of number of permutations
a = ""
n = 0

for a in string:
    n = n + 1
ans = n**num
print ans,"total permutations possible possible"
print("")
raw_input("Push any button to continue")
print("")

non_tuple_list = [list(tuple) for tuple in itertools.permutations(string, num)]

d = enchant.Dict("en_US")

usable_combos = []
a = 0
attempt = 0

for e in non_tuple_list:
 attempt = attempt + 1

 e =''.join(e)
 b =( d.check(e))
 if b == True:
  print e
  a = a + 1
  print attempt,"number of words checked"
  #calculates the percentage done
  percent = (float(attempt)/ans) * 100 
  print "It has gone through",percent,"%"
  print ""
print a,"Possible words"

#gets end time and subtracts first time from it
elapsed_time = time.time() - start_time

print "Time taken in this experiment:",elapsed_time,"seconds"

#print (usable_combos)
#print (non_tuple_list)
