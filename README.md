# Brute-Force Workshop 🤩

## **RULE!!!** only attack your own target, on your own machine or Codespace!!!

## Files
- `app.py` — the login server (target)
- `bot.py` — the brute-force bot (attacker)

## Setup (Codespaces)
1. **Code → Codespaces → Create codespace**
2. `pip install -r requirements.txt`

## Run
Terminal 1: python app.py
Terminal 2: python bot.py

The bot cracks the password in under a minute.

## How to stop the bot from hacking you???
1. **Longer password** — in `app.py`, change `3` to `12`. Search space explodes.
2. **Rate limiting** — in `app.py`, add these lines at the top:

```
import time
fails = 0
```
then, swap the login functions to this:

```
@app.route("/login", methods=["POST"])
def login():
    global fails
    guess = request.form.get("password", "")
    if guess == PASSWORD:
        return "FLAG{you_got_in}", 200
    fails += 1
    if fails > 5:
        time.sleep(2)   # after 5 wrong guesses, slow every attempt down
    return "Wrong password", 403
```
Real sites use CAPTCHA to block these kinds of automated attacks.
