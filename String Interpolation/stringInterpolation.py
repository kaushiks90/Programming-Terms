name ='Kaushik'
age=26
#greeting="My name is "+name+" and I am "+str(age)+"years old"
# The above procedue is very difficult in maintaining spcae for this reason we use format  sowe dont have to typecast the int to string
#and space can be prevailed
greeting="My name is {0} and I am {1} years old".format(name,age)
print greeting
