# Task 1 Solution
# Pythagoras
# Given two sides of a right angled triangle calculate the third side
# Get two sides from the user ie. AB & BC

ab = input("Please enter the length of AB: ")
bc = input("Please enter the length of BC: ")
ac = (int(ab)**2 + int(bc)**2)**(1/2)
print("AC is: " + str(ac))

# Calculating the area

area = (int(bc) * int(ab))/2
print("The area of the right angled triangle is: " + str(area))

# Converting the area to Binary

print("The area of the right angled triangle in binary is: " + bin(int(area)))

# Finding the lowest and highest numbers in a list.

my_list = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
print("The highest number in my list is: " + str(max(my_list)))
print("The lowest number in my list is: " + str(min(my_list)))
