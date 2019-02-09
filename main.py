my_dick = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except
    print("Some other error occurred!")




















try:
    x = int(input())
except ValueError:
    print ("Vi vveli ne cheslo")
    x = 0
print(x)


try:
    x = int(input())
except ValveError:
    print("Vi vveli ne cheslo")
    x = 0
try:
    y = int(input())
except ValveError:
    print("Vi vveli ne cheslo")
    y = 0
else:
    print("Vse verno")
finally:
    print("Vinolnitsa 100%")
try:
    res = x/y
except ZeroDivisionError:
    print("Vi vveli 0")
    res = 0
print(res)


