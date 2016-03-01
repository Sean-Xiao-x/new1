#in python 2 is raw_input / in python 3 is input
# message = raw_input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = raw_input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = raw_input(prompt)
# print("\nHello, " + name + "!")

# age = raw_input('How old are you?')
# print(age)

# age = raw_input('how old are you?')
# print(int(age)>=18)

# height = raw_input('how tall are you, in inches?')
# height = int(height)
# if height >= 36:
#     print("\n you're tall enough to ride")
# else:
#     print("\n you'll be able to ride when you're a litter older")

#% is modulo operator,which divides one number by another number and returns the remainder.
# print(4%3)
# print(5%3)
# print(7%4)

# number = raw_input("enter a number,and I'll tell you if it's even or odd:")
# number = int(number)
# if number%2 == 0:
#     print("\n the number "+str(number)+" is even.")
# else:
#     print("\n the number "+str(number)+" is odd.")

# car_type = raw_input("What kind of car would you like?")
# print("\nLet me see if I can find you a "+car_type+".")

# customer_number = raw_input("how many people are in your dinner group?")
# customer_number = int(customer_number)
# if customer_number > 8:
#     print("\nplease wait")
# else:
#     print("\nyour table is already")

# number = raw_input("please input a number and I'll tell you is a multiple of 10 or not.")
# number = int(number)
# if number%10 == 0:
#     print("\nThe number "+str(number)+" is multiple of 10.")
# else:
#     print("\nThe number "+str(number)+" is not multiple of 10.")


##########################################################################
#while loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
# #current_number +=1 is a shorthand for cuttent_number = current_number +1
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = raw_input(prompt)
#     print(message)

# while message != 'quit':
#     message = raw_input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = raw_input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# while True:
#     message = raw_input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# prompt = "\nTell me something, and I will add it to you pizza:"
# prompt += "\nEnter 'quit' to end."
# while True:
#     topping = raw_input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print("\nYou'll add "+topping.title()+" to your pizza.")

# age = raw_input("Please enter your age to confirm ticket price:")
# age = int(age)
# if age < 3:
#     price = 0
# elif age <= 12:
#     price = 10
# else:
#     price = 15
# print("\nYour ticket price is $"+str(price)+".")

# prompt = "\nPlease enter your age to confirm ticket price:"
# prompt += "\nEnter 'quit' to end the program. "
# while True:
#     age = raw_input(prompt)
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age <= 12:
#             price = 10
#         else:
#             price = 15
#         print("\nYour ticket price is $"+str(price)+".")

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     confirmed_user = unconfirmed_users.pop()
#     print("verifying user: "+confirmed_user.title())
#     confirmed_users.append(confirmed_user)
# print("\nThe following users have been confirmed:")
# for users in confirmed_users:
#     print(users.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
# polling_active = True
# while polling_active:
#     name = raw_input("\nWhat is your name?")
#     response = raw_input("which mountain would you like to climb someday?")
#     responses[name]=response
#     repeat = raw_input("Would you like to let another person respond?(yes/no)")
#     if repeat == 'no':
#         polling_active = False
#
# for name,response in responses.items():
#     print(name+" would like to climb "+response+".")

# sandwish_orders = ['big','medium','small']
# finished_sandwishes = []
# while sandwish_orders:
#     current_sandwish = sandwish_orders.pop()
#     print("\nI made you a "+current_sandwish.title()+" sandwish.")
#     finished_sandwishes.append(current_sandwish)
# for finished in finished_sandwishes:
#     print(finished)

