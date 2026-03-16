# Write a program to find the greatest of four numbers entered by user.

number = []
greatest = 0

for i in range(4):
    number.append(int(input("Enter four numbers: ")))

for num in number:
    if(num > greatest):
        greatest = num

print(greatest)