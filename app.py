"""
Vulnerable login server for the brute-force workshop.

This is INTENTIONALLY insecure. Run it ONLY on your own machine
(localhost) or your own Codespace. Never deploy this to the public
internet with a short password.

Run it:
    pip install -r requirements.txt
    python app.py

Then open http://localhost:5000 in a browser, or point bot.py at it.
"""

from flask import Flask, request
import secrets
import string

app = Flask(__name__)

# A "randomly generated" password. We keep it SHORT (4 characters,
# lowercase letters + digits) on purpose so the brute force actually
# finishes during the workshop. In the real world this is exactly the
# kind of password that makes a site crackable -- that's the lesson.
ALPHABET = string.ascii_lowercase + string.digits
PASSWORD = "".join(secrets.choice(ALPHABET) for _ in range(4))

# Printed to the instructor's console so you can verify the crack worked.
print("=" * 40)
print(f"Target password for this run: {PASSWORD}")
print("=" * 40)


PAGE = """
<!doctype html>
<title>Workshop Login</title>
<h1>Secret Area</h1>
<form method="post" action="/login">
  <input name="password" placeholder="password" autofocus>
  <button type="submit">Log in</button>
</form>
<p>{message}</p>
"""


@app.route("/")
def home():
    return PAGE.format(message="")


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
