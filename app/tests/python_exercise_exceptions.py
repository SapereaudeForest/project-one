# Below code generate a exception and stopped the scripts   

a = 1
b = 0
# result = a/b
# print(result)

try:
    result = a/b
except ZeroDivisionError as ex:
    print(f'Exception occured: {ex}')
    result = 0
print(result)

ex = ValueError("This is a ValueError function raised after dividing by 0")

print(type(ex)) #<- jaka to klasa?

print(ex)# <- reprezentacja dla uzytkownika + ekstrakt samej wartosci ValueError()

print(repr(ex)) # <- reprezentacja dla programisty

print(type(repr(ex)))
print(type(str(ex)))


def read_config(path_file):
    if not isinstance(path_file, str) or not path_file:
        raise ValueError("Ścieżka do pliku musi być niepustym stringiem.")

    file = None
    try:
        file = open(path_file, encoding="utf-8")
        return file.read()
    except FileNotFoundError:
        print(f"Plik nie istnieje: {path_file}")
        return None
    except (OSError, UnicodeError) as ex:
        print(f"Wystąpił problem z odczytem pliku: {ex}")
        return None
    finally:
        if file is not None:
            file.close()

read_config("demo.csv")
print("cos poszlo nie tak ale script dalej dziala")