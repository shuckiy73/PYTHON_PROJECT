names = ["Андрей", "Василий", "Марина"]
names_dict = {
    "Андрей": 24,
    "Василий": 35,
    "Марина": 13
}
print(names_dict[names[0]])
print(names_dict[names[1]])
print(names_dict[names[2]])
print("Имя:", names[2], "Возраст:", names_dict[names[2]])
str_result = f"Имя: {names[0]}, Возраст: {names_dict[names[0]]}"
print(str_result)
print(names)
names.append("Игорь")
names.append("Валерий")
names.append("Валерия")
print(names)
names_dict["Игорь"] = 17
names_dict["Валерий"] = 27
names_dict["Валерия"] = 37
print(names_dict)
