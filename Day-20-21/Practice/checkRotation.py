def check_rotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    temp=s1+s1
    if s2 in temp:
        return True
    else:
        return False
s1 = "ABCD"
s2 = "ACBD"
print(check_rotation(s1,s2))


# def are_rotations(s1, s2):
#     # Check if lengths of two strings are equal
#     if len(s1) != len(s2):
#         return False
#
#     # Concatenate s1 with itself
#     temp = s1 + s1
#
#     # Check if s2 is a substring of the concatenated string
#     if s2 in temp:
#         return True
#     else:
#         return False
#
#
# # Example usage
# s1 = "ABCD"
# s2 = "ACBD"
#
# if are_rotations(s1, s2):
#     print("Strings are rotations of each other")
# else:
#     print("Strings are not rotations of each other")
