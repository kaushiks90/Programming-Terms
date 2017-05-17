e=["S","A","G","R","K"]
op="<ul>\n"

for x in e :
	op+='<li>{0}</li>\n'.format(x)
	print "Address of op is {0} ".format(id(op))

op+='</ul>'

