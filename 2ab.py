#write the python progrsm to read in a list of numbers
#use one-line comprehensions of vreate a new list of even numbers
#create another list in reversing the elements
S = [ x**2 for x in range(10)] #read element of the list
M = [x for x in S if x % 2 == 0]
M.reverse()
print(S)
print(M)


