weekOne = open('path to practice file', 'r')

lines = weekOne.readlines()
# open the practice file

while lines:
    print("Learn this: ", lines)
    lines = weekOne.readlines()

# print each line/word every time the user presses enter

weekOne.close()
