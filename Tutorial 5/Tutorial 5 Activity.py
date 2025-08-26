c = 10

print("Celsius\tFahrenheit")

while c <= 30:
    f = (9/5 * c) + 32
    print(c, "\t", round(f, 2))
    c += 5  
