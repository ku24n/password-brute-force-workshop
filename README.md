# Password Brute-Force Workshop

A small lab for beginners: build a bot that cracks a weak login, then add
defenses and watch it fail.

**Rule:** only attack your own target, on your own machine or Codespace.

## Files
- `app.py` - the login server (target)
- `bot.py` - the brute-force bot (attacker)

## Setup (Codespaces)
1. **Code -> Codespaces -> Create codespace**
2. `pip install -r requirements.txt`

## Run
Terminal 1:
```
python app.py
```
Terminal 2:
```
python bot.py
```
The bot cracks the password in under a minute.

## Add a defense, re-run the bot, watch it fail
1. **Longer password** - in `app.py`, change `3` to `12`. Search space explodes.
2. **Rate limiting** - add a delay or lockout in `/login`. The bot crawls.
3. **Lockout / CAPTCHA** - how real sites block automation.

## Going further
TryHackMe - PicoCTF - OverTheWire Bandit - OWASP Top 10
