beatles = []
print("Step 1:", beatles)

beatles.append("Lennon")
beatles.append("McCartney")
beatles.append("Harrison")
print("Step 2:", beatles)

members = [input("Enter 4th member: "), input("Enter 5th member: ")]

for i in members:
    beatles.append(i)
print("Step 3:", beatles)

del beatles[3]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(0, "Starr")
print("Step 5:", beatles)

print("The Fab", len(beatles))