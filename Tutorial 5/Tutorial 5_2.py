num = 5
while True:
    num = 2 * num
    if num % 4 == 0:
        break
print(num)


oceans = ["Atlantic", "Pacific", "Indian", "Arctic", "Antarctic"]
i = len(oceans) - 1
while i >= 0:
    if len(oceans[i]) < 7:
        del oceans[i]
    i = i - 1
print(", ".join(oceans))

