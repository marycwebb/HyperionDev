"""
Write a program that allows a user to register students for an exam venue
First create an empty list
Ask the user how many students are registering, caste input as integer
Create a for loop based on the amount of students 
Within the for loop ask the user to keep entering ID numbers 
Append each ID number to the new list
Write the ID numbers to the text file reg_form
For each iteration add a dotted line and start a new line so once printed each student can sign their name next to their ID number
"""
new_list = []
amount_students = int(input("Please enter how many students are registering: "))
for i in range(amount_students):
    reg_form = input("Please enter the next students ID number: ")
    new_list.append(reg_form)

with open("reg_form.txt", 'w') as file:
    for i in new_list:
        file.write(str(i) + str(20*".")+ "\n")

  