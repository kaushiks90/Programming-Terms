import itertools

my_list=[1,2,3]
p=itertools.permutations(my_list,3)

for x in p:
	print x


word="sample"
rev="plemas"
p=itertools.permutations(rev,6)

for x in p:
	if ''.join(x)==word:
		print "Match found {}".format(''.join(x))
		break
else:
	print "No Match found"
