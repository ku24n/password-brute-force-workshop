# Password Brute-Force Workshop

A tiny, hands-on lab for beginners: build a brute-force bot, crack a weak
login, then add defenses and watch the bot fail.

> **Rules of the lab**
> Only ever point the bot at **your own** target running on **your own**
> machine or Codespace. Never attack a system you don't own or have written
> permission to test.

## What's here

| File | What it is |
|---|---|
| `app.py` | A deliberately insecure login server (the target). |
| `bot.py` | The brute-force bot (the attacker). |
| `requirements.txt` | Python dependencies. |

## Setup

### Option A — GitHub Codespaces (easiest for a class)
1. Click **Code → Codespaces → Create codespace**.
2. In the terminal: `pip install -r requirements.txt`
3. Keep the port **private** (the default). You'll attack `localhost`.

### Option B — Your own laptop
1. Install Python 3.
2. `pip install -r requirements.txt`

## Run it

**Terminal 1 — start the target:**
```
python app.py
```
It prints the randomly generated password so you (the instructor) can
verify the crack. Students don't need to look at it.

**Terminal 2 — run the bot:**
```
python bot.py
```
Watch it grind through the search space and recover the password. With a
3-lowercase-letter password this takes roughly half a minute.

## The real lesson: break your bot on purpose

After it works, make the login uncrackable and re-run the bot:

1. **Longer password + bigger character set.** In `app.py`, change the
   length from `3` to `12` and set `ALPHABET` to
   `string.ascii_letters + string.digits + string.punctuation`.
   Recompute the search space in `bot.py` — it's now infeasible.
2. **Rate limiting.** Add a small `time.sleep()` or a lockout after N failed
   attempts in `/login`. The bot slows to a crawl.
3. **Account lockout / CAPTCHA.** Discuss how real sites block automation.
4. **Hashing + salting.** Why stealing the password database still doesn't
   hand attackers the passwords.

That contrast — "I broke it, then I made it unbreakable" — is the whole point.

## Going further
- Swap the brute force for a **dictionary attack** using a wordlist; show
  it's far faster against human-chosen passwords.
- Try [TryHackMe](https://tryhackme.com), [PicoCTF](https://picoctf.org),
  and [OverTheWire Bandit](https://overthewire.org/wargames/bandit/).
- Read the [OWASP Top 10](https://owasp.org/www-project-top-ten/).
