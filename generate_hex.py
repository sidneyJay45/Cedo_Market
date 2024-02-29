import os

# Generate 12 bytes of random data and convert it to a hex string
random_hex = os.urandom(12).hex()

print(random_hex)
