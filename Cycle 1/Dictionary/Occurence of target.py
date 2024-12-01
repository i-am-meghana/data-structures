#Given a list of numbers and a target number count how many times the target appears in the list
#so make a dict that stores the count. then using dict method get to get the value of the target


user_list = input("ENter list of nos separated by spaces")
my_list = list(map(int, user_list.split())) #input gets a string we split it using whitspace and then turn it into a list
target = int (input("enter target"))

count_dict = {}
for item in my_list:
    count_dict[item] = count_dict.get(item, 0)+1 #default is 0 

count = count_dict.get(target,0)
print(target, count)
    
    
#why not list why are we using dicitonary


#grouping numebrs by their parity
#grouping students by grade
#all occcurences of elements in a list 
#nested dictionary
#dynamic aggregation
