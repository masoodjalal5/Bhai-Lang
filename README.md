# Bhai Lang
// Description

### Instructions
- Write the Bhai program in a text editor, ```Notepad++``` is prefered
- save the file with an extention ```.bhai```
**Method 1:**
- open command prompt in the file directory
- type ```bhaipretor_v02.py``` and press enter to run the program.
- when promped, enter the file name with extention.
- the ```bhaipretor``` will create a ```.cpp``` and ```.bhai``` file in the directory.
- the ```bhaipretor``` will also run the program and give output on the console screen.

**Method 2:**
- double click the ```bhaipretor_v02.py``` file
- when promped, enter the file name with extention.
- the ```bhaipretor``` will create a ```.cpp``` and ```.bhai``` file in the directory.
- the ```bhaipretor``` will also run the program and give output on the console screen.


## Requirements
**Languages**
- ```Python 3``` or newer
- ```C++ 11``` or newer

**Compilers**
- ```g++``` compiler for C++

**Python Libraries**
- ```time```
- ```os```


# Documentation

### Hello World
Every Bhai Lang program starts with a ```salam bhai``` and ends with ```shukria bhai```.
```
salam bhai
	bol bhai "Hello Bhai!";
shukria bhai
```
**Output**
```Hello Bhai!```

### Variables
Bhai Lang supports all common variable data-types.

- number			// integer
- lambaNumber		// long
- asharia			// float
- dugnaAsharia		// double
- harf				// character
- haan ya na		// boolean

**Boolean Values**
```haan ya na``` only accepts 2 values,
- ```sahi``` for true
- ```ghalat``` for false

```ko do``` assigns value to variable.
```
salam bhai

	/* integer*/
	number a ko do 5;
	lambaNumber b ko do 10;
	
	/* floating point*/
	asharia f ko do 2.6;
	dugnaAsharia g ko do 15.67;
	
	/* character*/
	harf h ko do 'c';
	
	/* boolean*/
	haan ya na isSahi ko do sahi;

shukria bhai
```

**Arthematic Operations**
The variables can be manipulated using arthematic operations.

- jama			// +
- manfi			// -
- zarb			// *
- taqseem		// /
- remainder		// %


### Print/Display Output

**Strings**
Strings and statements can be printed on the console using ```bol bhai``` operator.
```
salam bhai
	bol bhai "Print this statement bhai";
shukria bhai
```
**Output**
```
Print this statement bhai
```

**Multiple Strings**
Multiple strings can be separated using **separation operator** ```<```
```
salam bhai
	bol bhai "First statement " < "Secod statement " < "nth statement";
shukria bhai
```
**Output**
```
First statement Secod statement nth Statement
```

**Newline**
You can print the statemnt on newline using ```\n``` sequence or by using ```agla jumla bhai``` 

**Variables**
Variables and variable operations can be performed and displayed.
```
salam bhai
	/* multiple variables can be declared and defined in a single statement */
	number a ko do 5, b ko do 10;
	
	bol bhai "This is number a: " < a < "\n";
	bol bhai "This is number b: " < b < agla jumla bhai;
	
	bol bhai "The sum is: " < a jama b;
shukria bhai
```
**Output**
```
This is number a: 5
This is number b: 10
The sum is: 15
```

**Comments**
Bhai Language supports comments which are enclosed between```/*``` and ```*/```.
```
salam bhai
	/* This is a comment*/
	bol bhai "The comments will not be displayed";

shukria bhai
```

### Conditionals

**Comparison Operators**
Comparison operators are used to compare values and find the relation between them
The common comparison operators in bhai lang are

- ```barabr``` 				// equals to
- ```chota```				// less than
- ```Chota ya Barabr``` 	// less than or equal to
- ```bara```				// greater than
- ```Bara ya Barabr```		// greater than or equal to
- ```Barabr nahi```			// not equal to

**```agr bhai```-```agr nahi bhai``` Conditional**
Bhai Lang its own if-else statement which execute the block if ```agr bhai``` is ```sahi``` and will execute ```agar nahi bhai``` if is ```ghalat```
```
salam bhai

	number i ko do 5;
	
	agr bhai(i chota 10){
		bol bhai "i is less than 10";
	}
	agr nahi bhai{
		bol bhai "i is greater than 10";
	}
shukria bhai
```
**Output**
```
i is less than 10
```

**```agr bhai```-```warna bhai```-```agr nahi bhai``` Conditional**
If there are multiple conditions that must be compared, than ```warna bhai``` can be used as many times as needed
```
salam bhai

	number i ko do 5;
	
	agr bhai(i chota 10){
		bol bhai "i is less than 10";
	}
	warna bhai(i barabr 5){
		bol bhai "i is equal to 5";
	}
	agr nahi bhai{
		bol bhai "i is greater than 10";
	}
shukria bhai
```
**Output**
```
i is less than 10
```

If there are multiple conditions they can be separated by using ```and``` and ```or``` operators.
- ```and```		// The block will execute if both or all the conditions are ```sahi```
- ```or```		// The block will execute if one of the condition is ```sahi``` 

### Loops
The ```jab tak bhai``` loop will run as long as the condition is ```sahi``` and stop when the condition becomes ```ghalat```
```
salam bhai

	number i ko do 0;
	
	jab tak bhai(i chota 10){
		bol bhai i;
	}
shukria bhai
```
**Output**
```
0123456789
```

**```bs bhai``` and ```agla dekho bhai```**
the ```bs bhai``` operator will stop the ```jab tak bhai``` loop,
the loop will go to the next iteration when it reaches ```agla dekho bhai``` operator.
```
salam bhai
	
	number i ko do 0;
	jab tak bhai(sahi){

	i++;
		
		agr bhai((i remainder 2) barabr 1){ /* skips odd values */
			bol bhai "continuing\n";
			agla dekho bhai;
		}
		warna bhai(i bara 10){	/* closes the loop if i is greater than 10 */
			bol bhai "closing the loop\n";
			bs bhai;
		}
		agr nahi bhai{	/* if it is even the program displays it */
			bol bhai i < " is even\n";
		}
	}
shukria bhai
```
**Output**
```
continuing
2 is even
continuing
4 is even
continuing
6 is even
continuing
8 is even
continuing
10 is even
continuing
closing the loop
```

### More Updates to follow. 