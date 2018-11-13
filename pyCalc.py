print "Calculator Booting"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
radius = float(raw_input("Please enter the circle's radius"))
area = 3.14159 * (radius ** 2)
print "The circle's radius is %" (area)
elif option == 'T':
base = float(raw_input("Please enter the triangle's base"))
height = float(raw_input("Please enter the triangle's height"))
area = .5(b * h)
print "The triangle's area is %" (area)
else print "Error: Invalid Shape"


print "Calculator Exiting"
