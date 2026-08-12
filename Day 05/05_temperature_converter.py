def convert_temperature(temp, unit):
    test = unit.upper()
    if test == "C":
       p = (temp * 9/5) + 32
       return p, "F"
    elif test == "F":
       q = (temp - 32) * 5/9
       return q, "C" 
    else:
           return print("Invalid unit")
x = float(input("Enter the temperature: "))
y = input("Enter the unit (C/F): ")
t, u = convert_temperature(x, y)
print(f"The converted temperature is: {t} degree {u}")
   
