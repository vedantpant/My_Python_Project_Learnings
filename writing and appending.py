# employee_file = open("employee list.txt", "a") # a - append
# employee_file.write("\nKelly - Customer Service")
# employee_file.write("\nToby - Human Resources") #\n - escape characters
# employee_file.close()

# write into a new file or overwrite the existing file
# employee_file = open("employee list.txt", "w") # w - overwrite on old file
# employee_file = open("employee list1.txt", "w") # w - write a new file
employee_file = open("index.html.", "w") # w - write a new file
employee_file.write("<p>This is HTML</p>")
# employee_file.write("\nKelly - Customer Service")
# employee_file.write("\nToby - Human Resources") # \n - escape characters
employee_file.close()