
def tempcelcius(a):
	c = ((a-32)*5)/9
	print("temp in celcius is ", c)
	
def tempfeh(b):
	d = ((c*9)/5) +32
	print("temperature in fahrenie is ",d)
	
while True:
	x = input("enter your choice : \n 1 for feh to celcius \n 2 for celcius to feh \n 3 for exit \n")

	if x == "1":
		f = float(input("enter feh value") )
		tempcelcius(f)
	elif x == "2":
		c = float(input("enter celcius value"))
		tempfeh(c)
	else:
		break
		
