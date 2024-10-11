#Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

def is_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

print(is_triangle(1, 2, 3)) #False, "didn't work when sides were 1, 2, 3"
print(is_triangle(7, 2, 2)) #False, "didn't work when sides were 7, 2, 2"
print(is_triangle(5, 1, 2)) #False, "didn't work when sides were 5, 1, 2"