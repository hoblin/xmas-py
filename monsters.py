import os
import time

os.system("mpg123 /home/pi/pi-lightorgan-read-only/audio/monsters.mp3 & > /dev/null")
time.sleep(0.6)

os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/audio/monsters.mid > /dev/null")