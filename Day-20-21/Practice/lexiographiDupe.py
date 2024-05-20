def removeDuplicateLetters(s: str) -> str:
    last_occurrence = {char: i for i, char in enumerate(s)}
    stack, seen = [], set()
    print(last_occurrence)
    for i, char in enumerate(s):
        if char in seen:
            continue
        while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


# Example usage:
# print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cbacdcbc"))
