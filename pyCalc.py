print "Calculator Booting"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
	radius = float(raw_input("Please enter the circles radius: "))
	area = 3.14159 * (radius ** 2)
	print "The circles radius is %s :" % area  
elif option == 'T':
	base = float(raw_input("Please enter the triangles base"))
	height = float(raw_input("Please enter the triangles height: "))
	area = 0.5 * b * h
	print "The triangle's area is %s" % area
else :
	print "Error: Invalid Shape"
