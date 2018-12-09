# 2-1. Simple Message: Store a message in a variable, and then print that message
message = "I like my cat"
print(message)
# 2-2. Simple Messages: Store a message in a variable, and print that message.
# Then change the value of your variable to a new message, and print the new
# message
message = "I like playing with my cat."
print(message)
message = "He is a good cat"
print(message)
# 2-3. Personal Message: Store a person’s name in a variable, and print a message
# to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
first_name = "Wyatt"
last_name = "Vander Linde"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "would you like to learn some math?")
# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase
name = "Wyatt Vander Linde"
print(name.upper())
print(name.lower())
print(name.title())
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”
print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')
# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
name = "\tWyatt Vander Linde\n"
print("Unmodified:")
print(name)
print("\nUsing lstrip():")
print(name.lstrip())
print("\nUsing rstrip():")
print(name.rstrip())
print("\nUsing strip():")
print(name.strip())
# 2-8. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print statements to see the results.
print(4+4)
print(12-4)
print(8*1)
print(16/2)
# 2-9. Favorite Number: Store your favorite number in a variable. Then, using
# that variable, create a message that reveals your favorite number. Print that
# message.
favorite_number = 3
message = "My favorite number is " + str(favorite_number) + "."
print(message)
# 2-10. Adding Comments
# This is a comment 