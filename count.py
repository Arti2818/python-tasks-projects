print("How many cables should I avoided?")
cables_to_avoid = int(input())

cables_avoided = 0

print()

while cables_avoided < cables_to_avoid:
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} cables avoided.")