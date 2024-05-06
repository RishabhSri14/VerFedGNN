from cryptography.fernet import Fernet
import pandas as pd

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Load your dataset
data = pd.read_csv("rating.csv")

# Encrypt UserID and MovieID columns
data['UserID'] = data['UserID'].apply(lambda x: cipher_suite.encrypt(str(x).encode()).decode())
data['MovieID'] = data['MovieID'].apply(lambda x: cipher_suite.encrypt(str(x).encode()).decode())

# Save the encrypted data
data.to_csv("encrypted_dataset.csv", index=False)

# Save the encryption key for future decryption
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)
