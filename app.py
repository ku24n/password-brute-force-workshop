"""
Vulnerable login server for the brute-force workshop.

This is INTENTIONALLY insecure. Run it ONLY on your own machine
(localhost) or your own Codespace. Never deploy this to the public
internet with a short password.

Run it:
    pip install -r requirements.txt
    python app.py

Then point bot.py at it.
"""

from flask import Flask, request
import logging
import secrets
import string

app = Flask(__name__)

# Silence Werkzeug's per-request logging. Without this the server prints
# a line for every single guess -- thousands of them -- which floods the
# terminal and actually slows the whole demo down.
logging.getLogger("werkzeug").setLevel(logging.ERROR)

# A "randomly generated" password. We keep it SHORT (3 lowercase letters)
# on purpose so the brute force actually finishes during the workshop. In
# the real world this is exactly the kind of password that makes a site
# crackable -- that's the lesson.
ALPHABET = string.ascii_lowercase
PASSWORD = "".join(secrets.choice(ALPHABET) for _ in range(3))

# Printed to the instructor's console so you can verify the crack worked.
print("=" * 40)
print(f"Target password for this run: {PASSWORD}")
print("=" * 40)


@app.route("/login", methods=["POST"])
def login():
    guess = request.form.get("password", "")
    if guess == PASSWORD:
        return "FLAG{you_got_in}", 200
    return "Wrong password", 403


if __name__ == "__main__":
    # host="0.0.0.0" lets other laptops on the SAME local network reach it.
    # Use host="127.0.0.1" instead if you want it reachable only from this
    # machine. In a Codespace, leave it as is and attack http://localhost:5000.
    app.run(host="0.0.0.0", port=5000)
