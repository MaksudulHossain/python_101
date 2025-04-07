# •  Tests for equality and inequality with strings
message = "Eid Mubarak"
print(message=="Eid Mubarak")
print(message=="Ramadan Mubarak")

# •  Tests using the lower() method
message = "Eid"
print(message.lower()=="eid")
print(message=="EiD")

# •  Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
marks = 65
print(marks == 65)
print(marks >= 65)
print(marks > 65)
print(marks <= 65)
print(marks < 65)

# •  Tests using the and keyword and the or keyword
password = "mypassword"
valid_user = True 

print(password=="mypassword" and valid_user==True)
ap_exam_passed = False 
ap_course_taken = True

print(ap_exam_passed or ap_course_taken)

# •  Test whether an item is in a list
cars = ["mazda", "toyota", "bmw", "camaro"]
print("prius" in cars)
print("mazda" in cars)

# •  Test whether an item is not in a list
print("prius" not in cars)