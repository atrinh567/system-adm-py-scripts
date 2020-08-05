import os

print(os.getcwd())
print(os.listdir(os.getcwd()))

lorem = open('./basic-scripting/sample_text.txt', 'r')
# print(lorem.read())

for line in lorem:
    print(line, end="")

lorem.seek(0)

lorem.close()

lorem = open('./basic-scripting/sample_text.txt', 'w')

lorem.write("Lorem fake ipsum\n")

lorem.close()