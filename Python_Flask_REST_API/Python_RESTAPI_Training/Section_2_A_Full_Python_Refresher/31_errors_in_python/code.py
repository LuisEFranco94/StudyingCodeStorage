def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

#grades = []
students = [
    {"name": "Bob", "grades": [75,90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100,90]},
]
#print("Welcome to the average grade program.")
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averages {average}")
except ZeroDivisionError:
    # except ZeroDivisionError as e:
    #print(e)
    print(f"ERROR: {name} has no grades!")
else:
    # print(f"The average grade is {average}.")
    print(f"-- All student averages calculated --")
finally:
    # print("Thank you!")
    print("-- End of student average calculation --")


