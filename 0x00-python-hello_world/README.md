# 0x00. Python - Hello, World

## Resources

+ [The Python tutorial](https://docs.python.org/3/tutorial/index.html)
+ [Whetting your appatite](https://docs.python.org/3/tutorial/appetite.html)
+ [Using the python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
+ [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
+ [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
+ [Learn to program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
+ [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
+ Why Python programming is awesome
+ Who created Python
+ Who is Guido van Rossum
+ Where does the name ‘Python’ come from
+ What is the Zen of Python
+ How to use the Python interpreter
+ How to print text and variables using print
+ How to use strings
+ What are indexing and slicing in Python
+ What is the official Python coding style and how to check your code with pycodestyle

## Copyright - Plagiarism

+ You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
+ You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
+ You are not allowed to publish any content of this project.
+ Any form of plagiarism is strictly forbidden and will result in removal from the program.

##Requirements

+ Python Scripts
+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/python3
+ A README.md file at the root of the repo, containing a description of the repository
+ A README.md file, at the root of the folder of this project, is mandatory
+ Your code should use the pycodestyle (version 2.8.*)
+ All your files must be executable
+ The length of your files will be tested using wc

## Shell Scripts

+ Allowed editors: vi, vim, emacs
+ All your scripts will be tested on Ubuntu 20.04 LTS
+ All your scripts should be exactly two lines long (wc -l file should print 2)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/bin/bash
+ All your files must be executable

## C Scripts

+ Allowed editors: vi, vim, emacs
+ All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
+ All your files should end with a new line
+ Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
+ You are not allowed to use global variables
+ No more than 5 functions per file
+In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
+ The prototypes of all your functions should be included in your header file called lists.h
+ Don’t forget to push your header file
+ All your header files should be include guarded

# More Info

## Zen

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## TASKS

0. Run Python file

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

```bash
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x00-python-hello_world
+ File: 0-run

1. Run inline

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

```bash
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x00-python-hello_world
+ File: 1-run_inline

2. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

```bash
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x00-python-hello_world
+ File: 2-print.py

3. Print integer

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
+ The output of the script should be:
  + the number, followed by Battery street,
  + followed by a new line
+ You are not allowed to cast the variable number into a string
+ Your code must be 3 lines long
+ You have to use f-strings tips

```bash
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x00-python-hello_world
+ File: 3-print_number.py

4. Print float

Complete the source code in order to print the float stored in the variable **number** with a precision of 2 digits.

+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
+ The output of the program should be:
  + Float:, followed by the float with only 2 digits
  + followed by a new line
+ You are not allowed to cast number to string
+ You have to use f-strings

```bash
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x00-python-hello_world
+ File: 4-print_float.py



