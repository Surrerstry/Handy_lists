import doctest


def remove_list_from_list(base_list, sub_list):
	"""
	>>> remove_list_from_list([1,2,3,4], [1,2]) 
	[3, 4]
	>>> remove_list_from_list([1,2,3,4], [])
	[1, 2, 3, 4]
	>>> remove_list_from_list([], [])
	[]
	>>> remove_list_from_list([], [1,2])
	[]
	>>> remove_list_from_list([1], [1,2])
	[]
	"""
	for item_from_sublist in sub_list:
		if item_from_sublist in base_list:
			base_list.remove(item_from_sublist)
	
	return base_list


if __name__ == '__main__':
  doctest.testmod()
