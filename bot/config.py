from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1287276743
    OWNER = config("OWNER")
    
    # Watermark Defaults
    WATERMARK = {
        "text": "Team Warlords",
        "fontsize": 20,
        "position": "top_right"
    }
    
    # Resolution Profiles
    RESOLUTION_PROFILES = {
        "480p": "-s 854x480",
        "720p": "-s 1280x720", 
        "1080p": "-s 1920x1080",
        "custom": ""
    }
    
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TG-videoCompress' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    
    THUMB = config("THUMBNAIL")
    
except Exception as e:
    LOGS.info("Environment vars Missing")
    exit(1)
