x = 'Dog'
y = 'Cat'
z = x + ' ' + y
my_len = len(z) # Obtain the number of characters of z
print(my_len)
print(len(y)) # Obtain the number of characters of y
my_ls = z.split() # Separate each word of z and store the result in a list
print(my_ls[1]) # Print the second element in the list

# -------------------------------------------------------------------

capitals = {
"France": "Paris",
"Spain": "Madrid",
"Germany": "Berlin",
"Japan": "Tokyo",
"Norway": "Oslo"
}

for country, city in capitals.items():
    print(f"The capital of {country} is {city}.")

# -------------------------------------------------------------------
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
    sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg >= 65 and avg <= 69:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
    print("Average: " + str(avg))
    print("Grade: " + letter_grade)

    if letter_grade == "F":
        print("Student is failing.")
    else:
        print("Student is passing.")

# ------------------------------------------------------------------

# The function expects an integer
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        remainder = number % 10
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")

palindrome(11881118811)
palindrome(125542628)
palindrome(123789987321)
palindrome(12121)


# ---------------------------------------------------

def dummy_fun(x):
    print('This is just an example')
    x = x + 1
    return x

x = 0
for i in range(5):
    x = dummy_fun(x)
    print(x)