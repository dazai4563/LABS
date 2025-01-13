#
# class User_Account:
#     def __init__(self,password ,username, email):
#         self.password = password
#         self.username = username
#         self.email = email
#
#     def set_password(self, new_password):
#         # global password
#         self.password = new_password
#         return self.password
#
#     def check_password(self, new_password):
#         if self.password == new_password:
#             return True
#         else:
#             return False
#
#
# from user_ac import User_Account
# a = User_Account('12', 'frfr', 'eree')
# print(a.set_password('12'))
# print(a.check_password('12'))


# class Vehicle():
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def get_info(self):
#         return (self.make, self.model)
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, fuel_type):
#         super().__init__(make, model)
#         self.fuel_type = fuel_type
#
#     def get_info(self):
#         return (self.make, self.model, self.fuel_type)
#
# from versicle import Car
# a = Car("laborgini", "samolet", "benzin")
# print(a.get_info())
