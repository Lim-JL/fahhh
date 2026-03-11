from pynput import keyboard
from pygame import mixer

# you can realistically put any sound file here
SOUND_PATH = "fahhhhhhhhhhhhhh.wav" 
mixer.init()
fahhh = mixer.Sound(SOUND_PATH)
fahhh.set_volume(0.3)


def on_press(key):
	if key == keyboard.Key.esc:
		return False
	else:
		fahhh.play()

with keyboard.Listener(on_press=on_press) as listener:
	listener.join()