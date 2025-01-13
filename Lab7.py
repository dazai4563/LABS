# list = []
#
#
# class Emploer:
#     def __init__(self, name, idd):
#         self.name = name
#         self.idd = idd
#
#     def get_info(self):
#         return ('name:', self.name, 'id:', self.idd)
#
#
# class Manager():
#     def __init__(self, department):
#         self.department = department
#
#     def manage_project(self):
#         return ('manage_project:', self.department)
#
#
# class Technician():
#     def __init__(self, specialization):
#         self.specialization = specialization
#
#     def perfom_maintenanse(self):
#         return self.specialization
#
#
# class TechManager(Emploer, Manager, Technician):
#     def __init__(self, name, idd, department, specialization):
#         Emploer.__init__(self, name, idd)
#         Manager.__init__(self, department)
#         Technician.__init__(self, specialization)
#
#     def add_emploer(self):
#         list.append(
#             'name:' + self.name + ' ' + 'id:' + self.idd + ' ' + 'department:' + self.department + ' ' + 'specialization:' + self.specialization)
#         return 'done'
#
#     def get_team_info(self):
#         return list
#
#
# import lab07
#
# emploer = lab07.TechManager('anton','45', 'it', 'program')
# print(emploer.add_emploer())
# print(emploer.get_team_info())