from cryptography.fernet import Fernet
import pandas as pd

# Load your dataset
data = pd.read_csv("rating.csv")

# Find unique UserIDs and MovieIDs
unique_user_ids = data['UserId'].unique()
unique_movie_ids = data['movieId'].unique()

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt UserIDs
user_id_map = {user_id: cipher_suite.encrypt(str(user_id).encode()).decode() for user_id in unique_user_ids}
data['UserId'] = data['UserId'].map(user_id_map)

# Encrypt MovieIDs
movie_id_map = {movie_id: cipher_suite.encrypt(str(movie_id).encode()).decode() for movie_id in unique_movie_ids}
data['movieId'] = data['movieId'].map(movie_id_map)

# Save the encrypted data
data.to_csv("encrypted_dataset.csv", index=False)

# Save the encryption key for future decryption
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)
