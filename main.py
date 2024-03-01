
# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
#
# users = (1, 'Toxir', 'Toxirov', 20, 'toxir@gmail.com')

# user = User(users[0], users[1], users[2], users[3], users[4])

# -------------------------------------------

# from collections import namedtuple
#
# User = namedtuple('User', 'id name lastname age email')
#
# users = [
#     (1, 'Toxir', 'Toxirov', 20, 'toxir@gmail.com'),
#     (2, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
#     (3, 'Toxir', 'Toxirov', 19, 'toxir@gmail.com'),
#     (4, 'Toxir', 'Toxirov', 25, 'toxir@gmail.com')
#
# ]
#
# for user in users:
#     us = User(*user)
#     print(us.id, us.name, us.lastname, us.age, us.email)

# -------------------------------------------

from collections import namedtuple

car = ('Malibu', 'Red', '300 km/h', 20000, 4, 'avtomat')

info = namedtuple('name color speed, price ruller avto')








