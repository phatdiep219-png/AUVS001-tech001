#1
def valid_course_code(code):
    if len(code) != 6:
        return False
    if not code[:3].isupper() or not code[:3].isalpha():
        return False
    if not code[3:].isdigit():
        return False
    return True

#2
def valid_hex_color(color):
    if len(color) != 7 or color[0] != "#":
        return False
    
    hex_chars = "0123456789ABCDEFabcdef"
    for c in color[1:]:
        if c not in hex_chars:
            return False
    return True

#3
def sum_numbers(text):
    total = 0
    current = ""
    
    for char in text:
        if char.isdigit():
            current += char
        else:
            if current != "":
                total += int(current)
                current = ""
    
    if current != "":
        total += int(current)
    
    return total

#4
def redact_phone_numbers(text):
    words = text.split()
    result = []

    for word in words:
        if (word.isdigit() and len(word) == 10) or word.startswith("+84"):
            result.append("[REDACTED]")
        else:
            result.append(word)

    return " ".join(result)