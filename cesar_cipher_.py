

#function prints welcome message
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

#function gets mode from user like to encrypt  or decrypt 
def enter_message():
    while True: #loop runs until valid input is recieved 
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        
#check for valid input error handling 
        if mode not in ['e', 'd']: 
            print("Invalid Mode")
            continue
        message = input("What message would you like to " + ("encrypt: " if mode == 'e' else "decrypt: "))
        message = message.upper()
        while True:
            try:
                shift = int(input("What is the shift number: "))
                break #break loop if input is valid 
            except ValueError: #hanles exception if input is number
                print("Invalid Shift")
        return mode, message, shift

#function to encrypt message 
def encrypt(message, shift):
    result = "" #initalize result 
    for i in range(len(message)): #loop runs for each character
        char = message[i]
        if char.isalpha(): #check character is alphabet 
            ascii_offset = 65 if char.isupper() else 97 #determine the ASCII offset based on the case of the character 
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset) #encrypt the character and ass it to result 
        else:
            result += char
    return result.upper()

#function to decrypt message 
def decrypt(message, shift):
    return encrypt(message, -shift) #decrypt the message by encrypting it with a negative shift 

#main function of program 
def main():
    welcome() #print welcome message
    while True: #loop runs until user choose to exit 
        mode, message, shift = enter_message()
        
        #condition check for encrypt or decrypt message
        if mode == 'e':
            result = encrypt(message, shift)
        else:
            result = decrypt(message, shift)
        print(result)

        #ask user to continue and ask for next encryption or decryption or to end program 
        repeat = input("Would you like to encrypt or decrypt another message? (y/n): ")
        if repeat.lower() != 'y':
            break
        
# check if this file is main program and run the main function 
if __name__ == "__main__":
    main()
