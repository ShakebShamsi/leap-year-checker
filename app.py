def leap_year(year):
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It's a Leap Year")
            else:
                 print(" Not a Leap Year")
        else:
             print("Not a Leap Year")
    else: 
        print("Not a Leap Year")
print("")
leap_year("")
print("")