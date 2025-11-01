# password_demo.py
import bcrypt
import time

# --- Step A: Create (store) a hashed password (demo only) ---
test_password = "kartik123"      # <-- demo password (change if you want)
salt = bcrypt.gensalt()        # bcrypt automatically salts (safe)
hashed = bcrypt.hashpw(test_password.encode(), salt)
print("Stored hash (keep secret in real systems):", hashed.decode())

# --- Step B: Small candidate list (demo wordlist) ---
candidates = ["1234", "password", "pass123", "admin", "hello","kartik123"]

# --- Step C: Attempt to find the password by checking each candidate ---
print("\nStarting controlled candidate-checking...")
start = time.time()
found = None
for guess in candidates:
    if bcrypt.checkpw(guess.encode(), hashed):
        found = guess
        print(f"Match found: {guess}")
        break
    else:
        print(f"Tried: {guess}  -> Not a match")

end = time.time()
print("\nFinished. Time elapsed: {:.4f} seconds".format(end - start))
if not found:
    print("No match found in the small demo list.")
