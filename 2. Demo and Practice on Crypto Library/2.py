from cryptography.fernet import Fernet

# Step 1: Generate a key
key = Fernet.generate_key()
print("Generated Key:", key.decode())

# Step 2: Create a Fernet cipher object
cipher = Fernet(key)

# Step 3: Take input message
message = input("Enter the message to encrypt: ").encode()

# Step 4: Encrypt the message
encrypted_text = cipher.encrypt(message)
print("\nEncrypted Text:", encrypted_text.decode())

# Step 5: Decrypt the message
decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted Text:", decrypted_text.decode())
