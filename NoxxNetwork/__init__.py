from NoxxNetwork.core.bot import RAUSHAN
from NoxxNetwork.core.dir import dirr
from NoxxNetwork.core.git import git
from NoxxNetwork.core.userbot import Userbot
from NoxxNetwork.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAUSHAN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
