old_list = [12,24,35,70,88,120,155]
new_list = [i for i in old_list if i %2 != 0]
print("the list after removing all even no. are:",new_list)
print("the no in new list devisible by 5 or 7 :",[i for i in new_list if i%5 == 0 or i%7 ==0])
 
