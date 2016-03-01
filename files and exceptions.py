
# with open('../digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# filename = '../digits.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

    # lines = file.readlines()
    # print(lines)
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))

# with open(filename,'a') as file_object:
#     file_object.write('\nI love u')
#
# with open (filename) as file_object:
#     content = file_object.read()
#     print(content)

# filename = '../digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# birthday = raw_input("Please enter you birthday: ")
# if birthday in pi_string:
#     print("your birthday is find.")
# else:
#     print("your birthday isn't find.")

# with open('../digits.txt')as file_object:
#     content = file_object.read()
#     print(content)
# with open('../digits.txt')as file_object:
#     for line in file_object:
#         print(line)
# with open('../digits.txt')as file_object:
#     lines = file_object.readlines()
#     print(lines)
# for line in lines:
#     print(line.rstrip())


######################################################################
#Exceptions

#print(5/0)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero.")

# print("Enter two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = raw_input("\nFirst number: ")
#     if first_number =='q':
#         break
#     second_number =raw_input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero.")
#     else:
#         print(answer)

# filenmae='alice.txt'
# try:
#     with open(filenmae)as f_obj:
#         content = f_obj.read()
# except IOError:
#     msg = "Sorry, the file "+filenmae+" does not exist."
#     print(msg)
# else:
#     print(content)

# title = "Alice in Wonderland"
# print(title.split())

# filenmae='../digits.txt'
# try:
#     with open(filenmae)as file_object:
#         content = file_object.read()
# except IOError:
#     print("Sorry, the file "+filenmae+" doesn't exist.")
# else:
#     each_number = content.split()
#     length = len(each_number)
#     print("The file "+filenmae+" has about "+str(length)+" words.")

# def count_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except IOError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) +
#             " words.")
# filename = 'alice.txt'
# count_words(filename)
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)

# def count_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except IOError:
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) +
#             " words.")
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)

# import json
# number =[2,3,5,7,11,13]
# filename = 'numebr.json'
# with open(filename,'w')as f_obj:
#     json.dump(number,f_obj)
#
# with open(filename)as file_object:
#     numbers= json.load(file_object)
# print(numbers)

# import json
# username = raw_input("What's your name?")
# filename = "username.json"
# with open(filename,'a')as file_object:
#     json.dump(username,file_object)
#     print("We'll remember you "+username+".")

# import json
# filename = 'username.txt'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except IOError:
#     username = raw_input("What is your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

