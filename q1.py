def string(a):
	d={"UPPER_CASE": 0 , "LOWER_CASE":0}
	for c in a:
		if c.isupper():
			d["UPPER_CASE"] +=1
		elif c.islower():
			d["LOWER_CASE"] +=1
		else:
			pass
	print (" Original String : ", a)
	print (" No. of Upper case character in the strin : " ,d["UPPER_CASE"])
	print ("No. of lower case character in the string :",d["LOWER_CASE"])
	
x = input("enter the string you want to save")
string(x)
