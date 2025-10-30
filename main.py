#Created by Anshul
#GitHub - @AnshulXDev


#ask for unit
print("Select the unit you want to convert to:\n"
"1. Kilometer to Mile\n"
"2. Mile to Kilometer\n"
"3. Celsius to Fahrenheit\n"
"4. Fahrenheit to Celsius\n"
"5. Celsius to Kelvin\n"
"6. Kelvin to Celsius\n"
"7. Fahrenheit to Kelvin\n"
"8. Kelvin to Fahrenheit\n"
"9. Gram to Kilogram\n"
"10. Kilogram to Gram\n"
"11. Second to Minute\n"
"12. Minute to Hour")
unit=int(input("Choose an option (1-12): "))
#conversion
if unit==1:  #Km to M
    km=float(input("Enter value in Kilometer: "))
    mile=km*0.62137119
    print(f"{km} Kilometer(s) is equal to {mile} Mile(s)")
elif unit==2:  #M to Km
    mile=float(input("Enter value in Mile: "))
    km=mile/0.62137119
    print(f"{mile} Mile(s) is equal to {km} Kilometer(s)")
elif unit==3:  #C to F
    celsius=float(input("Enter value in Celsius: "))
    fahrenheit=(celsius*9/5)+32
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
elif unit==4:  #F to C
    fahrenheit=float(input("Enter value in Fahrenheit: "))
    celsius=5/9*(fahrenheit-32)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
elif unit==5:  #C to K
    celsius=float(input("Enter value in Celsius: "))
    kelvin=celsius+273.15
    print(f"{celsius} Celsius is equal to {kelvin} ")
elif unit==6:  #K to C
    kelvin=float(input("Enter value in Kelvin: "))
    celsius=kelvin-273.15
    print(f"{kelvin} Kelvin is equal to {celsius} Celsius")
elif unit==7:  #F to K
    fahrenheit=float(input("Enter value in Fahrenheit: "))
    kelvin=(fahrenheit-32)*5/9+273.15
    print(f"{fahrenheit} Fahrenheit is equal to {kelvin} Kelvin")
elif unit==8:  #K to F
    kelvin=float(input("Enter value in Kelvin: "))
    fahrenheit=(kelvin-273.15)*9/5+32
    print(f"{kelvin} Kelvin is equal to {fahrenheit} Fahrenheit")
elif unit==9:  #G to Kg
    gram=float(input("Enter value in Gram(s): "))
    kg=gram/1000
    print(f"{gram} gram(s) is equal to {kg} kilogram(s)")
elif unit==10:  #Kg to g
    kg=float(input("Enter value in Kilogram(s): "))
    g=kg*1000
    print(f"{kg} kilogram(s) is equal to {g} gram(s)")
elif unit==11:  #second(s) to minutes(s)
    sec=float(input("Enter value in second(s): "))
    min=sec/60
    print(f"{sec} Second(s) is equal to {min} Minute(s)")
elif unit==12: #min to hrs
    min=float(input("Enter value in Minute(s): "))
    hrs=min/60
    print(f"{min} Minute(s) is equal to {hrs} Hour(s)")
else:
    print("Invalid option!")