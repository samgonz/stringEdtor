def stringEdtor(uneditedString):
    new_string = ""
    split_string = uneditedString.split("cats")
    separator = "dogs"
    new_string = separator.join(split_string)
    return new_string

# This is the string that will be edited in python.
newString = stringEdtor("I love cats. Did you know cats are my favorite animal?")

print(newString)
