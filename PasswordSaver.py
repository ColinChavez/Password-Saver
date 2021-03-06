import csv
import sys

# The password list - We start with it populated for testing purposes
passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]


# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the caesar cypher
encryptionKey = 16


def passwordEncrypt(unencryptedMessage, key):
    """
    Caesar Cyper Encryption
    """

    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage


def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print(" 7. Delete Password")
    print("Please enter a number (1-7)\n")
    choice = input()

    if(choice == '1'):  # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'):  # Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        ####### YOUR CODE HERE ######
        # You will need to find the password that matches the website
        # You will then need to decrypt the password

        # 1. Create a loop that goes through each item in the password list
        #  You can consult the reading on lists in Week 5 for ways to loop through a list
        #
        # 2. Check if the name is found.  To index a list of lists you use 2 square backet sets
        #   So passwords[0][1] would mean for the first item in the list get it's 2nd item (remember, lists start at 0)
        #   So this would be 'XqffoZeo' in the password list given what is predefined at the top of the page.
        #   If you created a loopv using the syntax described in step 1, then i is your 'iterator' in the list so you
        #   will want to use i in your first set of brackets.
        #
        # 3. If the name is found then decrypt it.  Decrypting is that exact reverse operation from encrypting.  Take a look at the
        # caesar cypher lecture as a reference.  You do not need to write your own decryption function, you can reuse passwordEncrypt
        #
        #  Write the above one step at a time.  By this I mean, write step 1...  but in your loop print out every item in the list
        #  for testing purposes.  Then write step 2, and print out the password but not decrypted.  Then write step 3.  This way
        #  you can test easily along the way.
        #

        def passwordLookup():
            """
            Finds the password that matches the website.
            """

            global message

            for password in range(len(passwords)):
                for item in range(len(passwords)):  # Step 1: Loop through each value in the 2D List.
                    print(end="")
                if passwordToLookup == passwords[password][0]:  # Step 2: Checks if password is found.
                    message = passwords[password][1]
                    print()
                    print("The Encrypted Password is: " + message)
                    return message
        passwordLookup()

        def passwordDecrypt(encryptedMessage, key):
            """
            Decrypt's the user's password.
            """

            decryptedMessage = ''

            # For each symbol in the encryptedMessage we will add an encrypted symbol into the encryptedMessage
            for symbol in encryptedMessage:
                if symbol.isalpha():
                    num = ord(symbol)
                    num += key

                    if symbol.isupper():
                        if num > ord('Z'):
                            num -= 26
                        elif num < ord('A'):
                            num += 26
                    elif symbol.islower():
                        if num > ord('z'):
                            num -= 26
                        elif num < ord('a'):
                            num += 26

                    decryptedMessage += chr(num)
                else:
                    decryptedMessage += symbol
            print("The Decrypted Password is: " + decryptedMessage)
            return decryptedMessage
        passwordDecrypt(message, -16)

        ####### YOUR CODE HERE ######

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        ####### YOUR CODE HERE ######
        # You will need to encrypt the password and store it in the list of passwords

        # The encryption function is already written for you
        # Step 1: You can say encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)]
        # the encryptionKey variable is defined already as 16, don't change this
        # Step 2: create a list of size 2, first item the website name and the second item the password.
        # Step 3: append the list from Step 2 to the password list

        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)

        def savePassword(encryptedPassword):

            """
            Encrypts the user's password and stores it in the passwords list.
            """
            global passwords
            user_list = []
            user_list.append(website)
            user_list.append(encryptedPassword)
            passwords.append(user_list)
            for keyvalue in passwords:
                print(', '.join(keyvalue))
            print("\nSuccessfully Updated list of Passwords!")
        savePassword(encryptedPassword)
        ####### YOUR CODE HERE ######

    if(choice == '4'):  # Save the passwords to a file
            savePasswordFile(passwords, passwordFileName)

    if(choice == '5'):  # print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '6'):  # quit our program
        sys.exit()

    if(choice == '7'):  # Delete Password
        print("Which website do you want to lookup the password for?")
        print("NOTE: You can only delete the last website and password that you saved.")
        print("FOR EX. If you want to delete \"yahoo\" You will have to delete every password after yahoo first.\n")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        def deletePassword():
            """
            Allows the user to delete a website and password from the end of the list.
            """
            for i in range(len(passwords)):
                for x in range(len(passwords)):
                    print(end="")
                if passwordToLookup == passwords[i][0]:
                    print("Website and Encrypted Password [" + ', '.join(passwords[x]) + "] has been removed! \n")
                    passwords.remove(passwords[x])
                    print("Updated List of Websites and Passwords: ")
                    print(passwords)
        deletePassword()

    print()
    print()
