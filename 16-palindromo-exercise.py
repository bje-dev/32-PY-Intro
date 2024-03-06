def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(text):
    text_reverse = ""
    for char in text:
        text_reverse = char + text_reverse
    return text_reverse


def is_palindromo(text):
    text = no_space(text)
    text_reverse = reverse(text)
    print(text_reverse)
    return text.lower() == text_reverse.lower()


print(is_palindromo("come and hold my hand"))


