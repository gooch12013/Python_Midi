import pygame.midi
import time


#set PM_RECOMMENDED_OUTPUT_DEVICE=1

pygame.midi.init()

print (pygame.midi.get_device_info(4))
player = pygame.midi.Output(4)
player.set_instrument(6)
print("bank 1 scene 1")
player.note_on(0, velocity=127, channel = 0)
player.note_on(0, velocity=127, channel = 0)
time.sleep(3)


while (1 == 1):
    player.note_on(0, velocity=127, channel=0)
    time.sleep(1)
    player.note_on(1, velocity=127, channel=0)
    time.sleep(1)





#player.note_off(64, 127)
del player
pygame.midi.quit()
