#key that needs to be solved 
#cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

#guides for me
#A = 65
#Z = 90

#a = 97
#z = 122

def clear(key):
    #this is the cleaner, so that every character are in capital letters.
    split = [char for char in key]
    length = len(split)
    character = []
    for i in range (0, length):
        num = 0
        num = ord(split[i])
        if num >= 65 and num <= 90:
            character.append(chr(num))
        elif num >= 97 and num <= 122:
            num -= 32
            character.append(chr(num))
        else:
            continue
    return character

def rotate(character, rot):
    length = len(character)
    chars = []
    number = []
    for i in range (0, length):
        num = 0
        num = ord(character[i])
        num += rot
        if num > 90:
            #this here mod 91 is for the unicode after 90 (Z) 
            left = num % 91
            num = 65 + left
        number.append(num)
        chars.append(chr(num))
    #number is returned just in case if the number hold the real flag
    return chars, number

done = False
while done != True:
    try:
        key = str(input("Enter the string\n"))
        rot = int(input("Enter the rotation\n"))
        if rot == 99977:
            #printing rotation from 0 to 26 (start to finish)
            clear = clear(key)
            for i in range (27):
                result = rotate(clear, i)
                print("Result", i, ":", result, "\n")
            exit()
        else:
            rot = rot
        done = True
    except ValueError:
        print("Try again.\n\n")

clear = clear(key)
result = rotate(clear, rot) 
print("Result:", result)
