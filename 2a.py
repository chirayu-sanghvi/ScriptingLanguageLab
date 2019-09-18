#write a program to read in a list of elements.
#create a new list that holds all the elemetns minus the duplicates (use function)

def remove_duplicates(numbers):
	newlist = []
	for number in numbers:
		if number not in newlist:
			newlist.append(number)
	
	
	print(newlist);
	return newlist;
remove_duplicates([1,2,3,4,5,5,5,6,3,2])		
