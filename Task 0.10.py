#Get two words or strings as input
string1 = input('Enter your word or sentence: ').lower()
string2 = input('Enter your word or sentence: ').lower()
#Compare the two strings
result=[] 
if(len(string1)<len(string2)): 
	for i in string1: 
		if(i in string2): 
			result.append(i) 
else: 
	for i in string2: 
		if(i in string1): 
			result.append(i) 
#Output letters
print("Common letters:",*result) 