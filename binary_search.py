def binary_search(Item, alist):
	found = False
	bottom = 0
	top = len(alist)- 1
	while bottom <= top and not found:
		middle = (bottom + top) // 2
		if alist[middle] == Item:
			found = True
		elif alist[middle] < Item:
			bottom = middle + 1
		else:
			top = middle - 1
	return found
