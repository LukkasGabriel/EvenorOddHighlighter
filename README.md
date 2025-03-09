# Even or Odd Highlighter
This Python script takes a user-inputted number and displays all numbers from 1 to that number, highlighting even numbers in green and odd numbers in red using ANSI escape codes.



https://github.com/user-attachments/assets/77f5dacf-3f72-40cf-8591-a2ed8f3b4f5e

#Features

- Displays numbers from 1 to the user-defined limit.

- Even numbers are highlighted in green.

- Odd numbers are highlighted in red.

- Uses ANSI escape codes for colored terminal output.

# How to Use

1. Run the script in a Python environment that supports ANSI escape codes (such as a terminal or command prompt that supports color).

2. Enter a number when prompted.

3.The script will print all numbers up to the entered value, with even and odd numbers highlighted accordingly.

# Example Output

````
================================
Digite um número e direi quais são pares ou ímpares.
================================
Vermelho = Ímpar
Verde = Par
================================
Digite um número: 10

[31m 1 [30m  [32m 2[30m  [31m 3 [30m  [32m 4[30m  [31m 5 [30m  [32m 6[30m  [31m 7 [30m  [32m 8[30m  [31m 9 [30m  [32m 10[30m  
````

# Requirements

- Python 3.x

- A terminal that supports ANSI color codes

# Customization

You can modify the ANSI color codes to change the colors:

- \033[31m → Red (Odd numbers)

- \033[32m → Green (Even numbers)

- \033[30m → Reset to default text color

# License

This project is open-source and free to use.
