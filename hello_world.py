# Hello World
print("Hello World!")
# Math Practice (addition/multiplication/division/division(rounds down))
#print(2+2)
#print(3*9)
#print(5/3)
#print(5//3)

#list Project: AWS Service Inventory
#list items:'EC2', 'Lambda', 'S3', 'DynamoDB', 'Cloud9'
#start empty and add each item
my_list = [ ]
my_list.append('EC2')
my_list.append('Lambda')
my_list.append('S3')
my_list.append('DynamoDB')
my_list.append('Cloud9')
#print list and list length
print(my_list)
print(len(my_list))
#remove 2 items (Lambda + DynamoDB)
my_list.remove('Lambda')
my_list.remove('DynamoDB')
#print new list and list length
print(my_list),print(len(my_list))
