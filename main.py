import threading
from pynput import keyboard
from pygame import mixer

SOUND_PATH = "fahhhhhhhhhhhhhh.mp3" 
# you can realistically put any sound file here
def play_sound():
	mixer.init()
	mixer.music.load(SOUND_PATH)
	mixer.music.set_volume(0.3)
	mixer.music.play()

def on_press(key):
	if key == keyboard.Key.esc:
		return False
	else:
		threading.Thread(target=play_sound).start()

with keyboard.Listener(on_press=on_press) as listener:
	listener.join()