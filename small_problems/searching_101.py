# Write a program that solicits six (6) numbers from the user and prints a 
# message that describes whether the sixth number appears among the first five.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

'''
P: Understand the Problem

- Questions
    - Does the program only accept 6 numbers? As a list?
    - Are the numbers stored locally in the function?
    - Is a function required?
    - Are these inputs strings or integers (does it matter?)
- Inputs
    -6 numbers
- Outputs
    - A statement saying if the 6th number appears among the first five.
- Rules
    - Explicit
        - Must solicit six numbers from users.
        - Must compare sixth number to previous five inputs.
    - Implicit
        - N/A

E: Examples/Test Cases:

- Provided above

D: Data Structure(s)
- Strings or Integers
- List?

A: Algorithm

1. Create an empty results list
2. Solicit user for 6 numbers
3. Append first 5 numbers to the results list.
4. See if 6th input is in the results list.
5a.If true, print statement.
5b. If false, print statement.

C: Code
'''
result = []

result.append(input("Enter the 1st number: "))
result.append(input("Enter the 2nd number: "))
result.append(input("Enter the 3rd number: "))
result.append(input("Enter the 4th number: "))
result.append(input("Enter the 5th number: "))
last_number = input("Enter the last number: ")

result_list = ', '.join(result)

if last_number in result:
    print(f"{last_number} is in {result_list}.")
else:
    print(f"{last_number} isn't in {result_list}.")