from pygame import init, mixer_music, event
init()
mixer_music.load('mk.mp3')
# Não ser animal denovo e colocar o "mk.mp3" como nome de arquivo, porem se for colocar coloque "mk.mp3.mp3"
mixer_music.play()
input()
event.wait()