def Checkifnum(text):
    if len(text) != 12:
        print("step 1")
        print(len(text))
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            print("step 2")
            print(text[i])
            return False
    if text[3] != '-':
        print("step 3")
        print(text[3])
        return False
    for i in range(4,6):
        if not text[i].isdecimal():
            print("step 4")
            print(text[i])
            return False
    if text[7] != '-':
        print("step 5")
        print(text[7])
        return False
    for i in range(9,12):
        if not text[i].isdecimal():
            print("step 6")
            print(text[i])
            return False

print('The phone number is 415-555-4242')
answer = Checkifnum('415-555-4242')
print(answer)