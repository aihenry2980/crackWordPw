import msoffcrypto
import io
from itertools import product
from tqdm import tqdm
import time


def try_password(file_path, password):
    try:
        # Open encrypted file
        file = msoffcrypto.OfficeFile(open(file_path, "rb"))

        # Create a temporary file object
        decrypted = io.BytesIO()

        # Try to decrypt with the password
        file.load_key(password=str(password))
        file.decrypt(decrypted)

        return True
    except:
        return False


def brute_force_word(file_path):
    # Calculate total combinations for progress bar
    total_combinations = 1000000  # 000000 to 999999

    print("Starting brute force attack...")
    print("This might take a while depending on your computer's speed.")

    # Try all 6-digit combinations
    for digits in tqdm(product(range(10), repeat=6), total=total_combinations):
        password = ''.join(map(str, digits))

        if try_password(file_path, password):
            print(f"\nPassword found: {password}")
            return password

    print("\nPassword not found")
    return None


def main():
    # Get file path from user
    file_path = input("Enter the path to your Word document: ")

    # Record start time
    start_time = time.time()

    try:
        # Attempt to crack password
        password = brute_force_word(file_path)

        # Calculate and display elapsed time
        elapsed_time = time.time() - start_time
        print(f"\nTime elapsed: {elapsed_time:.2f} seconds")

        if password:
            print("\nYou can now open your document using this password!")

    except FileNotFoundError:
        print("\nError: File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    main()