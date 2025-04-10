from decouple import config
from telethon.tl.types import InputWebDocument

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1287276743  # Replace with your DEV ID
    OWNER = config("OWNER")
    
    # Watermark settings
    WATERMARK_TEXT = config("WATERMARK_TEXT", default="Team Warlords")
    WATERMARK_POSITION = config("WATERMARK_POSITION", default="top_right")
    WATERMARK_FONT_SIZE = config("WATERMARK_FONT_SIZE", default=20, cast=int)
    WATERMARK_COLOR = config("WATERMARK_COLOR", default="white")
    
    # Default FFmpeg code with watermark support
    ffmpegcode = [
        "-preset faster -c:v libx265 -s {resolution} -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' "
        "-vf \"drawtext=text='{watermark_text}':fontsize={font_size}:fontcolor={font_color}:"
        "x={x_pos}:y={y_pos}\" "
        "-metadata 'title=Encoded By TG-videoCompress' "
        "-pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"
    ]
    
    THUMB = config("THUMBNAIL")
    
    # Notification settings
    NOTIFICATION_CHAT_ID = config("NOTIFICATION_CHAT_ID", default=OWNER)
    
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
