def cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# print(cascade(1234))

def count_partitions(n, m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	if m == 0:
		return 0
	# elif m == 0:
	# 	return 0
	return count_partitions(n - m, m) + count_partitions(n, m-1)

print(count_partitions(6,4))	