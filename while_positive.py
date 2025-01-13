my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
imax = len(my_list)
while i < imax:
	if my_list[i] < 0:
		break
	elif my_list[i] == 0:
		i += 1
		continue
	else:
		print(my_list[i])
		i += 1
