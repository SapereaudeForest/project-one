###OPENING / CLOSING A FILE IN PYTHON ###

file_name = "./app/tests/DEXUSEU.csv"
file_demo = "./app/tests/demo.csv"

file = open(file_name, "r")
print(file.name)
#print(file.readable())
#print(file.writable())
data = file.readlines()
print(data)
file.close()
print("File is closed? : ", file.closed)

file = open(file_name)
for line in file:
    print(line,sep=":",end="")

print("\n")
print("File is closed? : ", file.closed)
file.close()

print("File is closed now? : ", file.closed)

#what could go wrong?

file = open(file_name, "r")
print(next(file))
print(next(file))
print(next(file))  # --> what if something goes wrong here? like an exception? the file will not be closed and we will have a resource leak
file.close()

#solution to the problem above is to use a context manager (with statement) that will automatically close the file even if an exception occurs
print("\nUsing context manager (with statement):")
with open(file_name, "r") as file:
    print(next(file))
    print(next(file))
    print(next(file))  # if an exception occurs here, the file will still be closed            
    print(file.closed)
print("File is closed? : ", file.closed)
#or Try/Finally which is more verbose but also works


file = open(file_name)
try:
    for line in file:
        print(line, sep=":", end="")
        raise ValueError("Something went wrong, forcing an exception")  # simulating an exception
except ValueError as e:
    print("Exception caught:", e)
finally:
    print("Closing the file in finally block")
    file.close()
    print("File is closed? : ", file.closed)

# Ciekawostka: kod sie nie wykonuje po raise ValueError, ale plik jest zamykany w finally block, więc nie ma wycieku zasobów. Ponizej przyklad nie wykonania kodu. Rozwiazanie : dodac except VallueError, aby przechwycic wyjatek i zamknac plik w finally block.
with open(file_demo) as f:
    headers = next(f)
    for row in f:
        row = row.strip()
        date, code, rate, volume = row.split(",")
        try:
            rate = float(rate)
            data.append((date, code, rate, volume))
        except ValueError as e:
            print(f"Error converting rate or volume for row: {row}. Error: {e}")
            pass
print(data)  # Skip this row and continue with the next one      
print(date)
