
# def greet_user():
# #Display a simple greeting.
#     print("Hello!")
# greet_user()

# def greet_user(username):
#     print("hello, "+username.title()+"!")
# greet_user("jesse")

# def display_message():
#     #Tell others what i am learning about chapter 8.
#     print("Chapter 8 is about functions.")
# display_message()

# def favorite_book(title):
#     #Show one of my favorite book.
#     print("My favorite book is "+title.title()+'.')
# favorite_book("The Great Gatsby")

# def describe_pet(animal_type,pet_name):
#     #Display information about a pet.
#     print("I have a "+animal_type+'.')
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
# describe_pet('cat','chouchou')
# describe_pet("chouchou","cat")
# describe_pet(animal_type='cat',pet_name='chouchou')

# def describe_pet(animal_type,pet_name='chouchou'):
#     #Display information about a pet.
#     print("I have a "+animal_type+'.')
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
# describe_pet(animal_type="cat")
# describe_pet(animal_type="cat",pet_name="chou")
# describe_pet("dog")
# describe_pet("dog","you")

# def get_full_name(first_name,second_name):
#     #Return a full name, neatly formatted.
#     full_name = first_name+' '+second_name
#     return full_name
# musician = get_full_name("Sean","Xiao")
# print(musician)

# def get_formatted_name(first_name, middle_name, last_name):
#     #Return a full name, neatly formatted.
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     #Return a full name, neatly formatted.
#     if middle_name:
#         full_name =first_name+' '+middle_name+' '+last_name
#     else:
#         full_name = first_name+' '+last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# def build_person(first_name,last_name):
#     #Return a dctionary of information about a person.
#     person = {'first':first_name,'last':last_name}
#     return person
# musician = build_person("Sean","Xiao")
# print(musician)

# def build_person(first_name, last_name, age=''):
#     #Return a dictionary of information about a person.
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age']=age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)
# musician = build_person("Sean","Xiao")
# print(musician)

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     f_name = raw_input("First name: ")
#     l_name = raw_input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name.")
#     print("Enter 'q' to Quit.")
#     f_name = raw_input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = raw_input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name,l_name)
#     print("\nHello "+formatted_name+".")

# def city_country(city,country):
#     #Return a city and country.
#     CC = city+","+country
#     return CC.title()
# place = city_country('Santiago','Chile')
# print(place)

# def greet_users(names):
#     #Print a simple greeting to each user in the list.
#     for name in names:
#         msg = "Hello, "+name.title()+"!"
#         print(msg)
# username=['hannah','ty','margot']
# greet_users(username)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # Simulate creating a 3D print from the design.
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

# def show_magicians(unmagicains):
#     while unmagicains:
#         cmagicain = unmagicains.pop()
#         print("Wellcom magicain "+cmagicain+".")
# magicians=["Bob","Kevin","Stuart"]
# show_magicians(magicians)
# print(magicians)
# magicians=["Bob","Kevin","Stuart"]
# show_magicians(magicians[:])
# print(magicians)

# def make_pizza(*toppings):
#     #Print the list of toppings that have been requested.
#     print(toppings)
# make_pizza("pepperoni")
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) +
#           "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein',
# location='princeton',
# field='physics')
# print(user_profile)
# user_profile1 = {'location':'wuhan','field':'physics'}
# user_profile = build_profile('alber','einstein',**user_profile1)
# print(user_profile)


# def greet_user():
#     username = raw_input("what's your name?")
#     print("hello "+username+".")
# greet_user()

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# def make_shirt(size,message):
#     print("\nI have a "+size+" size shirt.")
#     print("On shirt wirte "+message+'.')
# make_shirt('medium','wow')
# make_shirt(size='medium',message='wow')

# def get_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name = first_name+" "+middle_name+" "+last_name
#     else:
#         full_name = first_name +" "+last_name
#     return full_name.title()
#
# my_name = get_name('Sean','Xiao',)
# print(my_name)
# my_name = get_name('Sean','Xiao','CR')
# print(my_name)

# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=''):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi','hendrix',age=21)
# print(musician)

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = raw_input("First name: ")
#     l_name = raw_input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")








