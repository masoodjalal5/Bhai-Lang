# to run the command prompt to run the compiler
import os
import time

# Take File name from the user
file_name = input("Enter File Name: ")
handle = open(file_name, "r")
lines = handle.readlines()

# Debugging purposes
# print(lines, "\n")

# Outputing into a .cpp file
out_file_name = file_name.replace("bhai", "cpp")

# Openin c
f = open(out_file_name, "w")
#include the header files
f.write("#include <iostream>\n")
f.write("using namespace std;\n\n")

for line in lines:

	# if the line is empty, Just to tidy the code 
	if line == "\t\n" or "\t\n" in line: 
		line = line.replace("\t\n", "")
	else:
		pass

	# Basic conversion from bhai lang to c++
	# standard namespace
	# line = line.replace("lughat", "#include")
	# main function
	line = line.replace("salam bhai", "int main(){\n")
	# return 0 and ending
	line = line.replace("shukria bhai", "\n\n\treturn 0;\n}") # think about return 0, it is mostly not needed and will create issues in case of header files
	# cout
	line = line.replace("bol bhai", "cout <")
	
	# Corresponds to excursion operation
	if "cout" in line:
		# print("True")
		line = line.replace("<", "<<")

	# Data Type/Retrun Type
	line = line.replace("number", "\n\tint")			# Integer
	line = line.replace("lambaNumber", "\n\tlong")		# long
	line = line.replace("asharia", "\n\tfloat")			# float
	line = line.replace("dugnaAsharia", "\n\tdouble")	# double
	line = line.replace("harf", "\n\tchar")				# char
	line = line.replace("haan ya na", "\n\tbool")		# bool

	# for boolean values
	line = line.replace("sahi", "true")		# if true
	line = line.replace("ghalat", "false")	# if false


	# Assignment Operator
	line = line.replace("ko do", "=")

	# Arithematic Operations
	line = line.replace("jama", "+")		# Addition
	line = line.replace("manfi", "-")		# Subtraction
	line = line.replace("zarb", "*")		# Multiplication
	line = line.replace("taqseem", "/")		# Division
	line = line.replace("remainder", "%")	# Modulus/Remainder

	# Next line by endl
	line = line.replace("agla jumla bhai", "endl")

	# Comparison operators
	line = line.replace("barabr", "==")				# equals to
	line = line.replace("chota", "<")				# less than
	line = line.replace("Chota ya Barabr", "<=")	# less than or equal to
	line = line.replace("bara", ">")				# more than
	line = line.replace("Bara ya Barabr", ">=")		# more than or equal to
	line = line.replace("Barabr nahi", "!=")		# not equal to

	# Logical operators
	if "cout" not in line:
		line = line.replace("and", "&&")
		line = line.replace("or", "||")
		

	# conditionals
	# if conditional
	line = line.replace("agr bhai", "\n\tif")			# if
	line = line.replace("warna bhai", "\n\telse if")	# else if			
	line = line.replace("agr nahi bhai", "\n\telse")	# else

	# switch conditional
	# ToDo

	# Loops
	# while loop
	line = line.replace("jab tak bhai", "while")

	# break
	line = line.replace("bs bhai", "break")
	# continue
	line = line.replace("agla dekho bhai", "continue")

	# for loop and do while loops
	# ToDo: 

	# increment/decrement
	# ToDo
	if "++" in line:
		increment = "\n" + line
		line = line.replace(line, increment)

	# just for clear formatting 
	line = line.replace("\t}", "\n\t}")

	# Writing the line to file
	f.write(line)

	# Debugging purposes
	# print("\n\nLine:", line)

# closing file handler
f.close()


# Get the directory of the file
file_directory = os.path.abspath(os.getcwd()) + "\\"

# outfile with no extention to give to the first cmd command
compile_output_file_no_extention = out_file_name[:-4]
# executeble file with .exe format
compiled_executeable_file = out_file_name.replace("cpp", "exe")


# first command to compile the file save it in the same directory
# second command to run the executeable file
commands = [
			"start cmd /c g++ " + out_file_name + " -o " + compile_output_file_no_extention,
			"start /wait cmd /K " + compiled_executeable_file
			# "start /wait cmd /K a.exe"
			]

# Loop through the commands
for command in commands:
	os.system(command)

	# some sleep time to help with execution
	time.sleep(5)
