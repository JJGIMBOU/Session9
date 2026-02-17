try:
    fd = open("text.txt") #use fd to do a file pointer
    print("File opened successfully")
    content = fd.read()
    print(content)
    fd.close() #close cuts the connectivity and saves it when you write in it
    print("File closed successfully")
except FileNotFoundError:
    print("File not found")

try:
    with open("text.txt") as fd:
        print("File opened successfully")
        content = fd.read()
        print(content)
    print("File closed successfully")
except FileNotFoundError:
    print("File not found")

# a safer way is to read the file line by line
with open("text.txt") as fd:
    for line in fd:
        line = line.upper()
        print(line)
        #to get rid of the extra paragraphs put print(line, end"") or line = line.strip() followed by a print(line)