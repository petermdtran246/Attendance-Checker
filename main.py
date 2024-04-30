import sys

# Get input from the user
attendance_string = input("Enter student's attendance record (0s and 1s): ")
min_percentage = int(input("Enter minimum attendance percentage required: "))
def student_eligible_for_exam(attendace_string, min_percentage):
    # Count the number of days the student was present
    present_days = attendance_string.count('1')
    # Calculate the total number of days based on the length of the attendance.
    total_days = len(attendance_string)
    # # Calculate the attendance percentage as an integer
    attendance_percentage= int((present_days / total_days) * 100)

    # Check if the attendance percentage is greater than or equal to the minimum percentage required
    if attendance_percentage >= min_percentage:
        return f'{attendance_percentage} Yes'
    else:
        return f'{attendance_percentage} No'

# Call the function to check eligibility and print the result
result = student_eligible_for_exam(attendance_string, min_percentage)
print(result)








