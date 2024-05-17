list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

concatenated_list = list1 + list2

list1.append(6)

list1.extend(list2)

list2.insert(2, 11)

list1.remove(3)

last_element = list2.pop()

list1.reverse()

list2.sort()


print("Concatenated List:", concatenated_list)
print("Appended List1:", list1)
print("Extended List1:", list1)
print("Inserted List2:", list2)
print("Removed Element from List1:", list1)
print("Last Element from List2:", last_element)
print("Reversed List1:", list1)
print("Sorted List2:", list2)
