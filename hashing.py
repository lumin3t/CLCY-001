import hashlib

def hash_input(input_string):
    # Create a SHA-256 hash of the input string
    return hashlib.sha256(input_string.encode()).hexdigest()
    #Digest to give the output
# User input for password
input_string = input("Enter the input to hash: ")
print(hash_input(input_string))


