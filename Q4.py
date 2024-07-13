# print numbers from 10 to 20 and then from 10 to 20 with a step of 2, separated by commas
print("Printing numbers from 10 to 20:")
for num in range(10, 21):
    if num < 20:
        print(num, end=", ")
    else:
        print(num)

print("\nPrinting numbers from 10 to 20 with a step of 2:")
for num in range(10, 21, 2):
    print(num, end=", ")

# Prints numbers from 10 to 20 with a user-defined gap:
gap: int = int(input("\nPlease insert gap to the series sir:"))
print(f"Printing numbers from 10 to 20 with a gap of {gap}:")
for num in range(10, 21, gap):
    if num < 20 - gap:
        print(num, end=", ")
    else:
        print(num)

# Prints numbers from 10 to 20 with a user-defined gap, end and start:
start_point: int = int(input("\n\nPlease enter the start point:"))
end_point: int = int(input("Please enter the end point:"))
gap: int = int(input("Please enter the gap:"))
print(f"Printing numbers from 10 to 20 with a step of {gap}:")
for num in range(start_point, end_point + 1, gap):
    print(num, end=", ")

