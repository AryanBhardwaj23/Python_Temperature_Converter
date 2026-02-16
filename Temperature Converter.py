while True:
    print("\n1.Enter C for Celsius\n2.Enter F for Fahrenheit\n3.Enter K for Kelvin")
    o1=input("Enter temperature to convert from : ")
    o2=input("Enter temperature to convert to : ")
    temp = float(input("Enter your input: "))
    if o1 == "C" and o2 == "F":
        temp=(temp*9/5)+32
        print(f"New temperature is {temp} {o2}")
    elif o1 == "C" and o2 == "K":
        temp=temp+273.15
        print(f"New temperature is {temp} {o2}")
    elif o1 == "F" and o2 == "C":
        temp=round((temp-32)*5/9,2)
        print(f"New temperature is {temp} {o2}")
    elif o1 == "F" and o2 == "K":
        temp=round(((temp-32)*5/9)+273.15,2)
        print(f"New temperature is {temp} {o2}")
    elif o1 == "K" and o2 == "C":
        temp=temp=273.15
        print(f"New temperature is {temp} {o2}")
    elif o1 == "K" and o2 == "F":
        temp=round(((temp-273.15)*9/5)+32,2)
        print(f"New temperature is {temp} {o2}")
    else:
        print("INVALID INPUT")