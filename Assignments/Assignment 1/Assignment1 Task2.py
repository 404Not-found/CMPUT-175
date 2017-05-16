# Yunshu Zhao
# 2016 Winter Term
# University of Alberta
# Collaborate with zuofu li from Section B1
# Open two files and create a output file called 'callgraph.txt'
calls=open('calls.txt', 'r')
customers=open('customers.txt','r')
output=open('callgraph.txt','w')

# Create 5 dictionaries
name={}
location={}
info={}
nodes={}
position={}

# Ask user for a input and store the input in variables Data and Edge
print('Data for:')
Data = input('Directed graph .....1'+'\n'+'Undirected graph ...0'+'\n')

print('Edge weight is:')
Edge = input('The number of calls ...1'+'\n'+'The time spent ........0'+'\n')

# Use a for loop to split the values in the txt file
for x in calls:
    code, caller, receiver, duration, rate=x.split(';')
    
    #This is a calculation of total duration
    if caller in info:
        mylist=info[caller]  
        mylist[0]=mylist[0]+int(duration)
    else: 
        mylist=[int(duration)]
        info[caller]=mylist
    
    # This is to check whether the user input is equal to 1 or 0
    # Put different value in the key 'key'
    if Data == '1':
        key=caller+receiver
        
    elif Data == '0':
        
        if caller>receiver:
            key = receiver+caller
        else:
            key = caller+receiver        
    else:
        print('input is invalid')
        break
    
    # Check if the key in the dictionary
    # This concept is from the TA
    
    if key in nodes:
        
        if Edge == '1':         #Check whether the user ask for the number of calls or the time spent
            nodes[key]=nodes[key]+1
            
        elif Edge == '0':
            nodes[key]=nodes[key]+int(duration)
            
    else:
        
        if Edge == '1':         #Check whether the user ask for the number of calls or the time spent
            nodes[key]=1
            
        elif Edge == '0':
            nodes[key]=int(duration)
            
# Use a for loop to split the value in txt file and put values in the dictionary 
# The key is the phone number

i=1
for x in customers:
    
    numbers, names, locations = x.split(';')
    name[numbers] = names           # Put names in the dictionary
    location[numbers] = locations.replace('\n','')  # replace the '\n' with a space
    position[numbers] = i
    i = i +1
    
# Sort the value
for x in sorted(info.keys()):
    
    sequency = str(position[x])
    phoneNumber = str(x)
    totalTime = str(info[x][0])
    
    output.write(sequency+', '+phoneNumber+', '+name[x]+', '+location[x]+', '+totalTime+'\n')
    print(sequency+', '+phoneNumber+', '+name[x]+', '+location[x]+', '+totalTime)
    
output.write('\n')
print('')

# Sort the value
for key in sorted(nodes.keys()):
    
    output.write(str(position[key[:10]])+ ', '+str(position[key[10:]])+', '+str(nodes[key])+'\n')
    i = i+1
    
    print(str(position[key[:10]])+', '+str(position[key[10:]])+', '+str(nodes[key]))
    
calls.close()
customers.close()
output.close()