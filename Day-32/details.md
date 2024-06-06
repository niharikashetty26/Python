Indentation:

Use 4 spaces per indentation level.
Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets, and braces, or using a hanging indent.

Maximum Line Length:
Limit all lines to a maximum of 79 characters.
For lines containing comments or docstrings, limit to 72 characters.

Blank Lines:
Surround top-level function and class definitions with two blank lines.
Method definitions inside a class are surrounded by a single blank line.


Imports:
Imports should usually be on separate lines.

Imports are grouped in the following order:
Standard library imports.
Related third-party imports.
Local application/library-specific imports.
Import statements should be placed at the top of the file, just after any module comments and docstrings, and before module globals and constants.
Whitespace in Expressions and Statements

Avoid extraneous whitespace:
Immediately inside parentheses, brackets, or braces.
Between a trailing comma and a following close parenthesis.
Immediately before a comma, semicolon, or colon.
Before the open parenthesis that starts the argument list of a function call.
Always use a single space around operators and after commas, colons, and semicolons:

Example: a = f(1, 2) + g(3, 4)
Don't use spaces around the equals sign when used to indicate a keyword argument or a default parameter value:

Example: def complex(real, imag=0.0):
Comments
Block Comments:

Block comments generally apply to some (or all) code that follows them and are indented to the same level as that code.
Each line of a block comment starts with a # and a single space.
Inline Comments:

Use inline comments sparingly.
Inline comments should be separated by at least two spaces from the statement.
They should start with a # and a single space.
Docstrings:

Use triple double quotes for docstrings.
All public modules, functions, classes, and methods should have docstrings.
Docstrings should describe the method's effect as a command ("Do this", "Return that"), not as a description; e.g. don't say, "Returns the pathname ...".
Naming Conventions


Variable Names:
Use snake_case for variable names.
Avoid using names that are too short or not descriptive.
Function Names:

Function names should be lowercase, with words separated by underscores as necessary to improve readability.


Class names should normally use the CapWords convention.


Constants should be written in all capital letters with underscores separating words.
Programming Recommendations

Comparisons:
Use is and is not for comparing to None.
Use == and != for comparing values.

Boolean Values:
Use the fact that empty sequences are false in boolean contexts. E.g., if not x: rather than if x == []

Exceptions:
Use specific exceptions whenever possible, rather than a bare except: clause.
