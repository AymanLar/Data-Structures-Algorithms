# Python program to display all the prime numbers within an interval




lower = 10

upper = 1000


for num in range(lower ,upper+1):
    if num > 0:
        for i in range (2,num):
            if (num % i )== 0:
                break

        else :
            print(num)




















'''
low =0
up =20

for num in range(low ,up):
    if num > 0 :
        for i in range(2,num):
            if (num%i) == 0:
                break

        else:
            print(num) '''