from sys import breakpointhook


print()
print("*** Coffee Order Demo ***")
print()

keep_going = ""
while keep_going == "":

    want_coffee = input("Do you want coffee? ").lower()
    if want_coffee != "yes":
        print("Wrong answer, You always want coffee")
        print()
        continue

    else:
        print("Good Choice")
        break

print()
print("End of Program")
print()