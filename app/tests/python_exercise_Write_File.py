# create localy a file 
f = open('test_write.csv', 'w') # <-- w means write mode, if file exists it will be overwritten, if not it will be created
f.write("abc,def,ghi\n")
f.write("123,456,789\n")
f.close()

with open('test_write.csv', 'r') as f:
    print(f.readlines())

data = ['line1', 'line2', 'line3']
with open('test_write.csv', 'w') as f:
    f.writelines(data) # writelines does not add new line characters, so we need to add them manually

with open('test_write.csv', 'r') as f:
    print(f.readlines())

#TO FIX the problem above, we can add new line characters to each line in the data list before writing to the file:
data = ['line1\n', 'line2\n', 'line3\n']
with open('test_write.csv', 'w') as f:
    f.writelines(data)

with open('test_write.csv', 'r') as f:
    print(f.readlines()) #But we have issue here with \n