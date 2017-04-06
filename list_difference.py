#the following function takes in two lists and returns their difference in a set
def list_differ(alist1, alist2):
	if bool(alist1) == 0 or bool(alist2) == 0:
		return 0
	else:
		result = set(alist2) - set(alist1)
	return result
