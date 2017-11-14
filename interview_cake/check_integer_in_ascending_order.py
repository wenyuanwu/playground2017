# Suppose we had a list ↴ of n integers sorted in ascending order. How quickly could we check if a given integer is in the list?

def integer_in_list(l, i):
	print(l)
	mid_idx = int(len(l) / 2)
	mid_el = l[mid_idx]
	print(mid_idx)
	if mid_el == i:
		return True
	if mid_idx == 0:
		return False
	if mid_idx == len(l):
		return False
	if mid_el > i:
		return integer_in_list(l[:mid_idx], i)
	if mid_el < i:
		return integer_in_list(l[mid_idx + 1:], i)

l = [2,5,7,9]
i = 7
m = [3,5,7]
n = 3
# print(integer_in_list(l, i))
print(integer_in_list(m, n))
