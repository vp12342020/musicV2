"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = "9717749"
API_HASH = "9736a4b1994124eeb304ed47fce1bd07"
BOT_TOKEN = "6275219924:AAHMJb34ejMLb-lDj6LoAqEStMjmVpESO_Q"
SESSION_STRING = "AQAiSttYZEfhOhUC19MdvfJ9M7_DcBjGoWA3aZaFBijEbpPXwVPbQcLnojNz7pOhR7N260HUkM0NHca2OuAS1X69XEE6i9VtgvoJQv_jfqIPHrsJnwyY9cGiLqshGERhe-DQJtNEJr0P4XdkIzTZf_gHUVYCr6Xa59T3ZOXd1N4kBm8eURzbJ55fKhdvsdkca5mZpCzriNnT_icr83kE3wEPeCK__pi8WHYhgsgY4P0w5ABSVSfc6T-McAd_MLgnagIjqUgpq0Wlj2423LUVX3FEkoZ2GGn4eD-ZzZT_x5xh_V9oVF2eRXeBHlwr3whLIPjbUAuotDMiTKIsp6cB00z4AAAAASp103UA"
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
ASSISTANT_NAME = "ssmusicassist"
SUDO_USERS = list("1008157909")
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")

# API_ID = int(getenv("API_ID", ""))
# API_HASH = getenv("API_HASH", "")
# BOT_TOKEN = getenv("BOT_TOKEN", "")
# SESSION_STRING = getenv("SESSION_STRING", "")
# SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
# UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
# ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
# SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
