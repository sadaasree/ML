
import pickle
import random
import ast 
#create access data as dict with list containments
userAccess = {}
userName =['itmd513','james','sadaa','sree','monica','rachel','vijay',
           'sourav','prabhu','vidhiya','python','sam','ross','joey','chandler',
           'jane','kaleesi','arya','sansa','jonsnow']

with open("users.dat", "w") as myfile:
    myfile.write("{")
    for v in range(0,len(userName)):
            k = random.randint(0,10**5)
            value = random.randint(1000,1021)   
            myfile.write("'"+str(k)+"':['"+str(userName[v])+"','"+ str(value) +"'],\n")
    myfile.write("}")

