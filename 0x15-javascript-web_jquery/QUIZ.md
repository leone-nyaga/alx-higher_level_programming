# Quiz Questions

## Question #0

In the following code snippet, does the selector called ('body header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
1. No

2. **Yes** (**ans**)

## Question #1

In the following code snippet, does the selector called ('.header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. **No** (**ans**)

2. Yes

## Question #2

In the following code snippet, does the selector called ('header.my_header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. No

2. **Yes** (**ans**)

## Question #3

In the following code snippet, does the selector called ('section.my_header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. **No** (ans)

2. Yes

## Question #4

In the following code snippet, does the selector called ('#my_header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul id="my_header">
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. **No** (**ans**)

2. Yes

## Question #5

In the following code snippet, does the selector called ('header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. No

2. **Yes** (**ans**)

## Question #6

In the following code snippet, does the selector called ('HeAdER') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. No

2. **Yes** (**ans**)

```
**Tips**:
Selectors are case insensitive
```

## Question #7

How many HTML tags are present in the following HTML code?

```html
<!DOCTYPE html> is not an HTML tag
<head></head> is considered one HTML tag.
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. 16

2. 18

3. 20

4. **15** (**ans**)

## Question #8

In the following code snippet, does the selector called ('#my_header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. **No** (**ans**)

2. Yes

## Question #9

How many HTML tags are present in the following HTML code?

```html
<!DOCTYPE html> is not an HTML tag
<head></head> is considered one HTML tag.
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. 5

2. **6** (**ans**)

3. 7

4. 4

## Question #10

In the following code snippet, does the selector called ('#my_header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header id="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. No

2. **Yes** (**ans**)

## Question #11

In the following code snippet, does the selector called ('#header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. **No** (**ans**)

2. Yes

## Question #12

In the following code snippet, does the selector called ('.my_header') access the HTML tag <header>:

(using document.querySelector or $(...))?

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. No

2. **Yes** (**ans**)

## Question #13

How many HTML tags are present in the following HTML code?

```html
<!DOCTYPE html> is not an HTML tag
<head></head> is considered one HTML tag.
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <ul>
        <li>Home</li>
        <li>Admission</li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

1. **12** (**ans**)

2. 13

3. 14

4. 11
