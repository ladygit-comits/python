#Break statement - Exits an entire loop

num = 20

while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

#Continue statement - Skips a loop

devices = ["laptop", "Phone", "Tablet"]
for device in devices:
    if device == "Phone":
        continue
    print(device)
