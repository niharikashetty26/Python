# Initializing strings
str1 = "Hello"
str2 = "World"
str3 = "Python"
str4 = "  Trim me  "
str5 = "12345"

# Basic String Operations
# Concatenation
concatenated = str1 + " " + str2
print(f"Concatenated: {concatenated}")

# Repetition
repeated = str1 * 3
print(f"Repeated: {repeated}")

# Length
length = len(str1)
print(f"Length of '{str1}': {length}")

# Accessing characters
first_char = str1[0]
last_char = str1[-1]
print(f"First character of '{str1}': {first_char}")
print(f"Last character of '{str1}': {last_char}")

# Slicing
slice_str = str2[1:4]
print(f"Sliced string (str2[1:4]): {slice_str}")

# Case conversion
upper_str = str1.upper()
lower_str = str2.lower()
title_str = str3.title()
print(f"Upper case: {upper_str}")
print(f"Lower case: {lower_str}")
print(f"Title case: {title_str}")

# Trimming
trimmed_str = str4.strip()
print(f"Trimmed string: '{trimmed_str}'")

# Checking start and end
starts_with = str1.startswith("He")
ends_with = str2.endswith("ld")
print(f"'{str1}' starts with 'He': {starts_with}")
print(f"'{str2}' ends with 'ld': {ends_with}")

# Finding substrings
find_sub = str3.find("th")
print(f"Position of 'th' in '{str3}': {find_sub}")

# Replacing substrings
replaced_str = str3.replace("Python", "JavaScript")
print(f"Replaced string: {replaced_str}")

# Splitting and joining
split_str = str5.split("3")
joined_str = "-".join(["a", "b", "c"])
print(f"Split '{str5}' by '3': {split_str}")
print(f"Joined list with '-': {joined_str}")

# Checking if all characters are digits
is_digit = str5.isdigit()
print(f"All characters in '{str5}' are digits: {is_digit}")

# String Formatting
# Using % operator
formatted_old_style = "This is %s and that is %s." % (str1, str2)
print(f"Old style formatted string: {formatted_old_style}")

# Using str.format()
formatted_new_style = "This is {} and that is {}.".format(str1, str2)
formatted_indexed = "This is {0} and that is {1}. And {0} again.".format(str1, str2)
formatted_named = "This is {first} and that is {second}.".format(first=str1, second=str2)
print(f"New style formatted string: {formatted_new_style}")
print(f"Indexed formatted string: {formatted_indexed}")
print(f"Named formatted string: {formatted_named}")

# Using f-strings (Python 3.6+)
formatted_f_string = f"This is {str1} and that is {str2}. And {str3.upper()} is fun!"
print(f"F-string formatted string: {formatted_f_string}")

# Padding and alignment
left_aligned = f"{str1:<10}"  # Left aligned
right_aligned = f"{str1:>10}"  # Right aligned
center_aligned = f"{str1:^10}"  # Center aligned
print(f"Left aligned: '{left_aligned}'")
print(f"Right aligned: '{right_aligned}'")
print(f"Center aligned: '{center_aligned}'")

# Formatting numbers
number = 1234.56789
formatted_number = f"{number:.2f}"  # Two decimal places
formatted_number_with_commas = f"{number:,.2f}"  # Two decimal places with commas
print(f"Formatted number: {formatted_number}")
print(f"Formatted number with commas: {formatted_number_with_commas}")

# Escape sequences
new_line_str = "Hello\nWorld"
tab_str = "Hello\tWorld"
escaped_quote_str = "He said, \"Hello World\""
print("New line escape:\n" + new_line_str)
print("Tab escape:\t" + tab_str)
print("Escaped quote: " + escaped_quote_str)
