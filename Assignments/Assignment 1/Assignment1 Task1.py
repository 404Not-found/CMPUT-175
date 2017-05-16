# Yunshu Zhao
# 2016 Winter Term
# University of Alberta
# Collaborate with zuofu li from Section B1
# Open two files and create a output file called 'callgraph.txt'

customers = open('customers.txt','r+')
calls = open('calls.txt','r+')
output = open('output.txt','w')

# Cite from 'http://stackoverflow.com/questions/775049/python-time-seconds-to-hms'
# Use to calculate the time
def clock(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

# Create dictionaries and list
info = {}
name = {}
sumTime = {}
sumFee = {}
totalFee = []

# Use a for loop to split the value in txt file
for x in calls:
    timestamp, caller, receiver, duration, rate = x.split(';')
    
    # Calculate the total fee and append it to the list
    a = float(rate)*(float(duration)/60)
    totalFee.append(a)    
    
    if caller not in info:
        Count = [1]         # The total number of call times
        info[caller] = Count  
        
        time = [int(duration)]  # The total duration
        sumTime[caller] = time
        
        fee = [float(rate)*(float(duration)/60)]    # The total fee of each person
        sumFee[caller] = fee
        
    else:
        
        Count=info[caller]
        Count[0]=Count[0]+1
        
        time = sumTime[caller]
        time[0] = time[0] + int(duration)
        
        fee = sumFee[caller]
        fee[0] = fee[0] + float(rate)*(float(duration)/60)

# Round the totalFee to 2 decimal
p = round(sum(totalFee),2)

# Split the value from the txt file
for x in customers:
    numbers, names, locations = x.split(';')
    name[numbers] = names

# Start write the file
output.write('+--------------+------------------------------+---+---------+--------+'+'\n')
output.write('| Phone number | Name                         | # |Duration | Due    |'+'\n')
output.write('+--------------+------------------------------+---+---------+--------+'+'\n')

# Sort the value and write to the file
for z in sorted(info.keys()):
    
    phoneNumber = '('+str(z[:3])+') '+ str(z[3:6])+' '+ str(z[6:10])
    totalFee = str(round(sumFee[z][0],2))
    
    mTime = (clock(sumTime[z][0]))
    totalTime = str(mTime[:2]) + 'h' + str(mTime[3:5])+'m' +str(mTime[6:8])+'s'
    
    # This if statement is just to check whether to put ++ or **
    if float(info[z][0]) > 350 and float(totalFee) > 850:  
        output.write('|'+phoneNumber+'|'+name[z].ljust(30)+'|'+str(info[z][0])+'|'+totalTime.ljust(9)+'|'+'$'+totalFee.rjust(7)+'|'+'++'+'\n')
        
    elif float(info[z][0]) > 350 and float(totalFee) < 850:
        output.write('|'+phoneNumber+'|'+name[z].ljust(30)+'|'+str(info[z][0])+'|'+totalTime.ljust(9)+'|'+'$'+totalFee.rjust(7)+'|'+'**'+'\n')
        
    else:
        output.write('|'+phoneNumber+'|'+name[z].ljust(30)+'|'+str(info[z][0])+'|'+totalTime.ljust(9)+'|'+'$'+totalFee.rjust(7)+'|'+'\n')

output.write('+--------------+------------------------------+---+---------+--------+'+'\n') 
output.write('| Total dues   |                                          $   '+str(p)+'|'+'\n')
output.write('+--------------+------------------------------+---+---------+--------+'+'\n')

customers.close()
calls.close()
output.close()