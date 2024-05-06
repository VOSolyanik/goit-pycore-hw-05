def caching_fibonacci():
	"""Create a closure for caching fibonacci numbers"""
	cache = {}

	def fibonacci(n):
		# Check if the number is already in the cache
		if n in cache:
			return cache[n]
		# Return 0 if n is less than or equal to 0
		if n <= 0:
			return 0
		# Return 1 if n is equal to 1
		if n == 1:
			return 1
		# Calculate fibonacci number for n and store it in cache
		cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
		
		return cache[n]

	return fibonacci

def main() -> None:
	# Create a closure for caching fibonacci numbers
	fibonacci = caching_fibonacci()

	print(fibonacci(10))  # return 55
	print(fibonacci(15))  # return 610
	
if __name__ == "__main__":
	main()