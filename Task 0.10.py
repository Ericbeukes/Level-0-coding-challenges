def string_compare(string1,string2):
	result=[] 
	if(len(string1)<len(string2)): 
		for i in string1: 
			if(i in string2): 
				result.append(i) 
	else: 
		for i in string2: 
			if(i in string1): 
				result.append(i) 
	print("Common letters:",*result) 

string_compare("house","computers")