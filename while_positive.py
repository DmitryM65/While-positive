my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
imax = len(my_list)
while i < imax:
	if my_list[i] < 0:
		break                # отрицательное число, прерываем вывод
	elif my_list[i] == 0:
		i += 1               # ноль; пропускаем, но не прерываем
		continue
	else:
		print(my_list[i])
		i += 1
