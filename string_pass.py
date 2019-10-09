

def changestr(stri):
	stri = list(stri)
	for i in range(0,len(stri)):
		 
		if ord(stri[i]) in range(65,90):
		  stri[i]=chr(ord(stri[i])+1)
		
		elif ord(stri[i]) in range(97,122):
		  stri[i]= chr(ord(stri[i])+1)
		
		elif  (ord(stri[i]) == 90):
			stri[i] =chr(65)		 		 	
		
		else:
			stri[i] = chr(97)
		
	for x in range(0,len(stri)):
		     
		  if stri[x] in ('a','e','i','o','u'):
			   stri[x] = stri[x].upper()
			
	print("the modified string is : ",stri)

s1 = input("enter the string you want to be modified")
changestr(s1)

