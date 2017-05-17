import time
def expensive_func(num):
	time.sleep(1)
	result=num*num
	return result

result=expensive_func(4)
print result

result=expensive_func(10)
print result

result=expensive_func(4)
print result

result=expensive_func(10)
print result
