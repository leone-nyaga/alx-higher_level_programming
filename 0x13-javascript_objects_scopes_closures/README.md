# 0x13. JavaScript - Objects, Scopes and Closures

## Resources

Read or watch:

+ [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Object_basics)
+ [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Classes_in_JavaScript) (read all examples!)
+ [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
+ [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
+ [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
+ [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Object_prototypes)
+ [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Classes_in_JavaScript)
+ [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
+ [this/self](https://alistapart.com/article/getoutbindingsituations)
+ [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique), without the help of Google:

## General

+ Why JavaScript programming is amazing
+ How to create an object in JavaScript
+ What this means
+ What undefined means
+ Why the variable type and scope is important
+ What is a closure
+ What is a prototype
+ How to inherit an object from another

## Copyright - Plagiarism

+ You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
+ You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
+ You are not allowed to publish any content of this project.
+ Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

## General

+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/node
+ A README.md file, at the root of the folder of the project, is mandatory
+ Your code should be semistandard compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/standard/semistandard)
+ All your files must be executable
+ The length of your files will be tested using wc
+ You are not allowed to use var

## More Info

## Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```bash
$ sudo npm install semistandard --global
```

## Quiz Questions

## Tasks

0. Rectangle #0

Write an empty class Rectangle that defines a rectangle:

+ You must use the class notation for defining your class

```bash
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x13-javascript_objects_scopes_closures
+ File: 0-rectangle.js

1. Rectangle #1

Write a class Rectangle that defines a rectangle:

+ You must use the class notation for defining your class
+ The constructor must take 2 arguments w and h
+ Initialize the instance attribute width with the value of w
+ Initialize the instance attribute height with the value of h

```bash
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x13-javascript_objects_scopes_closures
+ File: 1-rectangle.js

2. Rectangle #2

Write a class Rectangle that defines a rectangle:

+ You must use the class notation for defining your class
+ The constructor must take 2 arguments w and h
+ Initialize the instance attribute width with the value of w
+ Initialize the instance attribute height with the value of h
+ If w or h is equal to 0 or not a positive integer, create an empty object

```bash
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x13-javascript_objects_scopes_closures
+ File: 2-rectangle.js

3. Rectangle #3

Write a class Rectangle that defines a rectangle:

+ You must use the class notation for defining your class
+ The constructor must take 2 arguments: w and h
+ Initialize the instance attribute width with the value of w
+ Initialize the instance attribute height with the value of h
+ If w or h is equal to 0 or not a positive integer, create an empty object
+ Create an instance method called print() that prints the rectangle using the character X

```bash
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$
```

Repo:

+ GitHub repository: alx-higher_level_programming
+ Directory: 0x13-javascript_objects_scopes_closures
+ File: 3-rectangle.js
