from datetime import date

def agecalci(num):
	today = date.today()
	
	age = today.year -  num.year - ((today.month,today.day) < (num.month,num.day))
	return age
	
print(agecalci(date(1997,2,3)),"years")
