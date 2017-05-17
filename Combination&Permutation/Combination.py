import itertools

my_list=[1,2,3]
combination=itertools.combinations(my_list,3)

for x in combination:
	print x


#Example where combination can be used
my_list=[1,2,3,4,5,6,7,8]
combination=itertools.combinations(my_list,3)
print [x for x in combination if sum(x)>18]