f = open("read_write_file\\poem.txt", "r")
total = 0
for line in f:
    token = line.split(" ")
    total += len(token)
print(total)
    