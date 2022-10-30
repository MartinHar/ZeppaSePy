import sys
import names
import random
import os
import sys

import requests
from faker import Faker
fake = Faker()

# image_url = fake.image_url()
# s = requests.get(image_url)
# with open(f"{fake.word()}.jpg", "wb") as f:
#     f.write(s.content)

my_width = 1280
my_height = 1024
image_url = fake.image_url(my_width, my_height)
s = requests.get(image_url)
print(s.url)

img = fake.word()+'.jpg'
print(img)
with open(img, "wb") as file:
    file.write(s.content)


# def user_store_choice():
#     while True:
#         choice = input("Enter user/store ID: ")
#         if choice.isdigit():
#             return choice
#         # elif choice.is:
#         #     print("float input")
#         #     break
#         else:
#             print("You should enter either only digits")


# fake = Faker('hy_AM')
# for _ in range(10):
#     print(fake.first_name_male())
# for i in range(1):
#     print(names.get_full_name())
# #
# #
# # convert string to brackets ''
# def convert(string):
#     li = list(string.split(" "))
#     return li
#
# str1 = "Ագապի Ազատուհի Այծեմնիկ Անի Անթառամ Աշխէն Ասթինէ Աստղիկ Արեգնազան Արշակուհի Արտեմիս Արփենիկ Արփի Բերկրուհի Գոհար Գոհարիկ Դալար Դեղձանիկ Դշխուհի Դիցուհի Եսթեր Երանիկ Երանուհի Թագուհի Ժպտանոյշ Իմաստուհի Իշխանուհի Իսկուհի Լալա Լիլիթ Լուսաբեր Լուսածին Լուսարփի Լուսնթագ Խոսրովանոյշ Խոսրովիդուխտ Ծովինար Կատարինէ Մարալ Մարգարիտ"
#
# print(convert(str1))

# index in loop (id = index)
# for idx, i in enumerate(arm_street_names):
# from faker import Faker
# faker = Faker(['hy_AM'])
#
# for _ in range(10):
#     print(faker.image_url())
#
# print(faker.license_plate())

#
# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total
#
#
# print(multiply(1, 3, 5))



