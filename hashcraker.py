import hashlib


"""
Attempts to find the password corresponding to a given SHA-256 hash.

Args:
- target_hash  (str): The SHA-256 hash of the password to find.
- file_path (str): Path to the file containing a list of potential passwords.


Returns:
- str: A message indicating whether the password was found and what it is if found.
"""
def crack_hash(target_hash, file_path):
    try:
        with open(file_path, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                guess_hash = hashlib.sha256(password.encode()).hexdigest()

                if guess_hash == target_hash:
                    return "Password found: {}".format(password)
        
        return "Password not found in dictionary."
    except FileNotFoundError:
        return "Password file not found."

if __name__ == '__main__':
    target_hash = 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'
    file_path = '10-million-password-list-top-10000.txt'
    result = crack_hash(target_hash, file_path)
    print(result)