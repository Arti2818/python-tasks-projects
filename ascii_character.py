print("Program started!.")

print("Please enter an ASCII code:")
code = int(input())

if  code >= 32 and code <= 126:
    print(f"The character represented by the ASCII value {code} is:{chr(code)}")

else:
    print("The character should not be displayed!")

print("Program Ended!")

