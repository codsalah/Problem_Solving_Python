def alphabet_position(text):
    positions = []
    for char in text:
        if char.isalpha():
            positions.append(str(ord(char.lower()) - ord('a') + 1))
    return ' '.join(positions)