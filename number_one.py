# í)
def circle_area(radius):
    pi = 3.14  
    area = pi * (radius ** 2)  
    return area
radius = 4
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}")


 # íí)
numbers = [ 7, 9, 15]
total = sum(numbers)
print(f'sum of the odd numbers {total}')

# ííí)
def list_numbers():
   numbers =[4,2]
   print(numbers[6])
   print(numbers[4])
   print(numbers[ 2])
   print(numbers[8])
   sum = 6
   difference=4
   qoutient=2
   product=8
   for elements in numbers:
    sum+=elements
    difference-=elements
    qoutient/=elements
    product*=elements
    print(f"The sum  of the elements is")
    print(f"The difference  of the elements is")
    print(f"The qoutient  of the elements is")
    print(f"The product  of the elements is")



# ív)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 26
student_info['city'] = 'Kampala'
print(student_info)