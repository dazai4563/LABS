# def write_to_file(filename="user_input.txt", append=False):
#     text = input("Введите текст, который хотите записать в файл:\n")
#
#     try:
#         if append:
#             mode = "a"
#         else:
#             mode = "w"
#
#         with open(filename, mode, encoding="utf-8") as file:
#             file.write(text + "\n")
#         print(f"Текст успешно {'добавлен в' if append else 'записан в'} файл '{filename}'.")
#
#     except Exception as e:
#         print(f"Произошла ошибка при записи в файл: {e}")
#
#
# while True:
#     action = input(
#         "Выберите действие:\n 1. Создать новый файл или перезаписать существующий.\n 2. Добавить текст в существующий файл.\n 3. Выйти. \n")
#
#     if action == "1":
#         write_to_file()
#         break
#     elif action == "2":
#         write_to_file(append=True)
#         break
#     elif action == "3":
#         break
#     else:
#         print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
#
#
#
# 
# def wwod(filename, a):
#     try:
#         strs = ''
#         if a == 'full':
#             with open(filename, 'r', encoding='utf - 8') as file:
#                 contet = file.read()
#             return contet
#         elif a == 'str':
#             with open(filename, 'r', encoding='utf - 8') as file2:
#                 for line in file2:
#                     strs = strs + line
#                 return strs
#         else:
#             print('error:str or full')
#     except FileNotFoundError:
#         return f'error file {filename} not found'
#
#
# print('выберете файл')
# filename = input()
# print('введите тип считывания(full or str)')
# a = input()
# print(wwod(filename,a))

