import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API
API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Bot Details
OWNER_USERNAME = getenv("OWNER_USERNAME", "TOXIC_HARRY")
BOT_USERNAME = getenv("BOT_USERNAME", "HarryXMuzicbot")
BOT_NAME = getenv("BOT_NAME", "HarryXMuzic")

# Database
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Logger
LOGGER_ID = int(getenv("LOGGER_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", 6020886539))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Repo
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/system78600/NoxxMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HARRY_UPDATES")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/HARRY_SUPPORT0")

# Assistant Join Link (Fix for InviteHashExpired)
ASSISTANT_JOIN = getenv("ASSISTANT_JOIN", "")
AUTO_LEAVING_ASSISTANT = False
# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist Limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# File Size Limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Assistant Sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot Lists
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/327ook.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/z7a93l.jpg"
)
PLAYLIST_IMG_URL = "https://ibb.co/N2Z5dkLR"
STATS_IMG_URL = "https://ibb.co/N2Z5dkLR"
TELEGRAM_AUDIO_URL = "https://ibb.co/N2Z5dkLR"
TELEGRAM_VIDEO_URL = "https://ibb.co/N2Z5dkLR"
STREAM_IMG_URL = "https://ibb.co/N2Z5dkLR"
SOUNCLOUD_IMG_URL = "https://ibb.co/4RkjhyZ5"
YOUTUBE_IMG_URL = "https://ibb.co/N2Z5dkLR"
SPOTIFY_ARTIST_IMG_URL = "https://ibb.co/N2Z5dkLR"
SPOTIFY_ALBUM_IMG_URL = "https://ibb.co/N2Z5dkLR"
SPOTIFY_PLAYLIST_IMG_URL = "https://ibb.co/N2Z5dkLR"
STREAM_IMG_URL = "https://files.catbox.moe/abz5qj.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/abz5qj.jpg"

# Duration Limit
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL Validation
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL url must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHAT url must start with https://"
        )
