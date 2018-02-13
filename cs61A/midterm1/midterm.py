def gcd(a, b):
	smaller = min(a, b)
	larger = max(a, b)
	if a % smaller == 0 and b % smaller == 0:
		return smaller
	else:
		return gcd(smaller, larger % smaller)

# print (gcd(34, 19))
# print (gcd(39, 91))
# print (gcd(20, 30))
# print (gcd(40, 40))

def hailstone(n):
	counter = 1
	print (n)
	if n == 1:
		return counter
	if n % 2 == 0:
		return hailstone( n // 2) + 1
	else:
		return hailstone (n * 3 + 1) + 1

a = hailstone(10)
# print (a)

def interleaved_sum(n, odd_term, even_term):
	return sum_function(1, n, odd_term, even_term)

def sum_function(counter, n, odd_term, even_term):	
	if counter == n:
		if counter % 2 == 0: 
			return even_term(counter)
		else:
			return odd_term(counter)
	else:
		if counter % 2 == 1:
			return odd_term(counter) + sum_function(counter + 1, n, odd_term, even_term)
		else:
			return even_term(counter) + sum_function(counter + 1, n, odd_term, even_term)   		

print (interleaved_sum(5, lambda x: x, lambda x: x*x))

def ten_pairs(n):
		