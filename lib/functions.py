#!/usr/bin/env python3
# /*
#   You should be able to call this function with no arguments and see its output in the terminal:
#   greetProgrammer();
#   => "Hello, programmer!"
# */
# function greetProgrammer() {
#   console.log("Hello, programmer!");
# }
def greet_programmer():
    print('Hello, programmer!')

# /*
#   You should be able to call this function with one argument and see its output in the terminal:
#   greet("Naureen");
#   => "Hello, Naureen!"
# */
# function greet(name) {
#   console.log(`Hello, ${name}!`);
# }
def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2