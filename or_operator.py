# ask user for the type of adventure
print("What type of adventure should I have?")
adventure_type = input()

# determine what message to display
if (adventure_type == "scary") or (adventure_type == "short"):
    print("Entering the dark forest !")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("taking the safe route!")
else:
    print("not sure which route to take.")

