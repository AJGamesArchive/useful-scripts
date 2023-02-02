import os
from cryptography.fernet import Fernet

# Generate new encryption key
def generateKey():
    key = Fernet.generate_key()
    with open("./Python/Encryption/encryptionKey.key", "wb") as keyFile:
        keyFile.write(key)
    print("New Encryption Key Generated")
    getKey()

# Get encryption key from file
def getKey():
    global fernet
    global key
    with open("./Python/Encryption/encryptionKey.key", "rb") as k:
        key = k.read()
        fernet = Fernet(key)
    print("Encryption key is ready to use.")

#! Get all viewable directories and files and add them to a list
def getDirectories():
    global files
    files = []
    for file in os.listdir():
        if file == "Encrypt Data.py" or file == "encryptionKey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

#! Carry out a full encryption of the device
def fullEncryption():
    for file in files:
        with open(file, "r") as f:
            data = f.read()
        data = fernet.encrypt(data.encode())
        with open(file, "wb") as f:
            f.write(data)
    print(f"Your device is fully encrypted using the key: {str(key)}")

#! Carry out a full decryption of the device
def fullDecryption():
    for file in files:
        with open(file, "rb") as f:
            data = f.read()
        data = fernet.decrypt(data).decode()
        with open(file, "w") as f:
            f.write(data)
    print(f"Your device is fully decrypted using the key: {str(key)}")

# Encrypt Stuff
def fileEncryption():
    with open("./Python/Encryption/Data.txt", "r") as t:
        data = t.read()
    data = fernet.encrypt(data.encode())
    with open("./Python/Encryption/Data.txt", "wb") as t:
        t.write(data)
    print("Your data has been encrypted.")

# Decrypt Function
def fileDecryption():
    with open("./Python/Encryption/Data.txt", "rb") as t:
        data = t.read()
    data = fernet.decrypt(data).decode()
    with open("./Python/Encryption/Data.txt", "w") as t:
        t.write(data)
    print("Your data has been decrypted.")

getKey()

running = bool(True)

while running:
    selection = str(input("What would you like to do?\n1 = Encrypt Data\n2 = Decrypt Data\n3 = Generate a New Encryption Key\n4 - Fully Encrypt this Device\n5 - Fully Decrypt this Device\n6 - Exit\n: "))
    if selection == "1":
        fileEncryption()
    elif selection == "2":
        fileDecryption()
    elif selection == "3":
        generateKey()
    elif selection == "4":
        print("No!")
        # Insert full encryption function here
    elif selection == "5":
        print("No")
        # Insert full decryption function here
    elif selection == "6":
        running = False
    else:
        print("Please enter either 1, 2, or 3.")