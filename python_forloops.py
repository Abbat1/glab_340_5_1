#Example 1: Display sum of natural numbers


# Input: Take the value of 'n' from the user
n = int(input("Enter a positive integer (n): "))


# Initialize a variable to store the sum
sum_of_natural_numbers = 0


# Calculate the sum of the first 'n' natural numbers
for i in range(1, n + 1):
    sum_of_natural_numbers += i


# Display the sum
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers}")



#Example 2: Palindrome

# Input: Take a number from the user
number = int(input("Enter a number: "))

#Convert the number to a string for easier comparison
num_str = str(number)

# Reverse the number
reversed_str = num_str[::-1]

#Example 3: pattern

n=5;
for i in range(n):
    for j in range(i):
        print ('*', end="")
        print ('')
               
for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
        print('')


#Example 4: Pyramid pattern
        # Input: Take the number of rows for the pyramid from the user
n = int(input("Enter the number of rows for the pyramid: "))


# Outer loop for the number of rows
for i in range(1, n + 1):
    # Print leading spaces for formatting
    for j in range(n - i):
        print(" ", end="")
    # Print asterisks for the current row
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line for the next row
    print()