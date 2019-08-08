#class Memoize:

#    def __init__(self, fn):
#        self.fn = fn
#        self.memo = {}

#    def __call__(self, *args):
#        if args not in self.memo:
#	    self.memo[args] = self.fn(*args)
#        return self.memo[args]

def addTo80(n):
	print("Looooong time")
	return 80 + n

#@Memoize	
def memoizedAddTo80(n, cache):
	if n in cache:
		return cache[n]
	else:
		print("Looooong time")
		cache[n] = n+80
		return cache[n]
		
def fibonacci(n, cache):
	if n in cache:
		return cache[n]
	
	if n == 0:
		cache[0] = 0
		return 0
	if n ==1 or n==2:
		cache[n] = 1
		return 1
		
	print("Looooong time")
	cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
	return cache[n]
	
def test():
	cache = dict()
	print(fibonacci(0, cache))
	print(fibonacci(1, cache))
	print(fibonacci(2, cache))
	print(fibonacci(3, cache))
	print(fibonacci(4, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	print(fibonacci(5, cache))
	