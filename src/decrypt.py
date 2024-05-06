from cryptography.fernet import Fernet
import pandas as pd

# Load the encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Load the encrypted dataset
data = pd.read_csv("encrypted_dataset.csv")

# Decrypt UserID and MovieID columns
data['UserID'] = data['UserID'].apply(lambda x: cipher_suite.decrypt(x.encode()).decode())
data['MovieID'] = data['MovieID'].apply(lambda x: cipher_suite.decrypt(x.encode()).decode())

# Save the decrypted data
data.to_csv("decrypted_dataset.csv", index=False)

