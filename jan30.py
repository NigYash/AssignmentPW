#Write a program to accept percentage from the user and display the grade according to the following criteria:
n= float( input("Enter the percentage: "))
if n>=90:
    print("A")
elif n>=80:
    print("B")
elif n>=60:
    print("C")
elif n<60:
    print("D")

#Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
price= int(input("Enter the price of a bike: "))
if price>100000:
    print("15%")
elif price>50000:
    print("10%")
elif price<=50000:
    print("5%")    

#Write a program to accept ant city from the user and display monuments of that city.

city= str(input("Enter the name of the city: "))
if city== "Delhi":
   print("Red Fort")
elif city== "Agra":
   print("Taj Mahal")
elif city== "Jaipur":
   print("Jal Mahal")

#Check how many times a given number can be divided by 3 before it is less than or equal to 10.
def divide_by_3(num):
    count = 0
    while num > 10:
        num = num / 3
        count += 1
    return count

#Why and when to use While loop on python give a detailed description with example.
#It is used to repeatedly execute the block of code until and unless condition remains true.
while(True):
    inp= int(input("Enter a number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("try again\n")
        continue

#use nested while loop to print 3 different patterns:

i = 1
while i<=4:
    j= 1
    while j<=4:
        print("*", end="")
        j+=1
    print()
    i+=1    

i = 1
while i<=4:
    j= 1
    while j<=i:
        print("*", end="")
        j+=1
    print()
    i+=1    


#Reverse a while loop to display number 10 to 1
num=10
while num>=1:
    print (num)
    num-=1