import instaloader

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login("akashshiva324@gmail.com", "akashshiva123!")        # (login)
L.interactive_login("akashshiva324@gmail.com")      # (ask password on terminal)
L.load_session_from_file(USER)