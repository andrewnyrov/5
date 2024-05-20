task = 'Неизменяемые и изменяемые объекты. Кортежи'
print(task)
immutable_var = 200, 300, 400, True, 'alterable'
print(immutable_var)
   #immutable_var[1] = 500
   #print(immutable_var) #TypeError: 'tuple' object does not support item assignment. Элементы в кортеже нельзя изменить, только переменные в нём
mutable_list = [600, 700, 800, True, 'x', 'z', 'Modified']
print(mutable_list)
mutable_list.extend('mute')
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list.remove(False)
print(mutable_list)