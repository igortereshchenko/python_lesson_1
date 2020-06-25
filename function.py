import re


def hello(name, age):
    print('Your naame is',name,'Your age is', age)
    print('Next year your age will be', age+1)

    print('End function')


def get_countries(list):
    user_countries = []

    for element in list:

        if isinstance(element, str):

            result = re.match(r'^[A-Z][A-Z]$', element)

            if result!=None:
                # print(result.group(0))
                user_countries.append(result.group(0))

    user_countries.sort()

    return user_countries



# name = input("Enter your name")
# age = int(input("Enter your age"))


# hello(name,age)

# print(type("a"))
# print(type('a'))
# print(type(1))
# print(type(1.1))
# print(type(True))
# print(type(False))
# print(type(None))
#
# print(float('1'))
# print(type(float('1')))

countries = ['GB', 'PL', 'DE', True, 1.1, '1.2','**** you', ['Kyiv','Odessa'], [[['ok']]] ]

print(get_countries(countries))

# user_countries = []
#
# for element in countries:
#
#     if isinstance(element, str):
#
#         result = re.match(r'^[A-Z][A-Z]$', element)
#
#         if result!=None:
#             print(result.group(0))
#             user_countries.append(result.group(0))



# sorted = user_countries.copy()
# sorted.sort()
# print(user_countries)
# print(sorted)
#
# sorted.extend(['DE','IT'])
#
# print(sorted)
# print(sorted.count('DE'))