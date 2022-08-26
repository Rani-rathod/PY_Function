# Number of Arguments
# 
# def my_function(fname):
#     print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")



# Arbitrary Arguments, *args

# def school(*kids):
# 	print(kids[1],"is my student.")

# school("rani","aaru","daksh","aanu")


# Keyword Arguments

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 




# def add(a,b,c=5):
#     d=a+b+c
#     print("addition",d)
# add(2,3,4)



# def name1(*name):
#   i=0
#   while i<len(name):
#     print("Hello",name[i])
#     i+=1
# name1("Rani","Divya","Nikita","Meera")


# def my_function(**kid):
#   print("His last name is " + kid["fname"])  
# my_function(fname = "Tobias", lname = "Refsnes") 


# def greet(*names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")



# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")



# def say_hello_people(name_x, name_y, name_z, name_a):
#     print("Namaste ", name_x) # hindi mein
#     print("Alah hafiz ", name_y) # urdu mein
#     print("Bonjour ", name_z) # french mein
#     print("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")



# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)
# icecream("chocolate", "butterscotch","vanilla","strawberry")


# def greet(*names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")


# def info(name, age):
#     print(name + " is " + age + " years old")
# info("Sonu","16")
# info("Sana", "17")
# info("Umesh", "18")


# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum
# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)


