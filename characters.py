print("What strange markings do you see?")
markings = input()

# Identify markings
print("\nIdentifying...\n")

for count in range(0, len(markings), 1):
    print(f"index{count}:", markings[count])

