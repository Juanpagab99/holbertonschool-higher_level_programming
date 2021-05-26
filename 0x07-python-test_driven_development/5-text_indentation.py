#!/usr/bin/python3
""" prints a text with 2 new lines
     after each of these
     characters: ., ? and :"""
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    length = len(text)
    for i in range(length):
        k = text[i - 1]
        q = text[i]
        if not (q == " " and (k == ":" or k == "." or k == "?" or k == ' ')):
            if q == ":" or q == "." or q == "?":
                print("{:s}\n".format(q))
            else:
                print(q, end="")
