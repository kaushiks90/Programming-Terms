#f(f(x))=f(x)
def add_ten(num):
	return num+10

print add_ten(10)
print add_ten(add_ten(10))

##The above function is not ideempotent the reason is when the function is passed into a function
#it should retun the same original result 


#Example of idempotent

print abs(-10)
print abs(abs(-10))