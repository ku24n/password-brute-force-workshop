

from flask import Flask, request
import logging
import secrets
import string

app = Flask(__name__)
logging.getLogger("werkzeug").setLevel(logging.ERROR)

# A randomly generated password. We keep it short (3 lowercase letters)
# on purpose so the brute force actually finishes during the workshop. In
# the real world this is exactly the kind of password that makes a site
# crackable 😳 ayo
ALPHABET = string.ascii_lowercase
PASSWORD = "".join(secrets.choice(ALPHABET) for _ in range(3))

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
    app.run(host="127.0.0.1", port=5000)
