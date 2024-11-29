'''
reading form external file csv file
'''
# relative file path, absolute file path.
employee_file = open("employee list.txt", "r") # r - read,w - write,a - append, r+ - read and write
# get info from the file (functions to be used)
# print(employee_file.readable()) # readable function to check weather file is readable or not
# print(employee_file.read()) # read all the content of the file
# print(employee_file.readline()) # read individual line of the file
# print(employee_file.readline()) # read individual line of the file - 2nd line
# print(employee_file.readline()) # read individual line of the file - 2nd line
# print(employee_file.readline()) # read individual line of the file - 2nd line
# print(employee_file.readlines()) # read lines and put them in a list
# print(employee_file.readlines()[1]) # read line and access the element of the list
for employee in employee_file.readlines():
    print(employee)
# close file if you open file as well
employee_file.close()


