import pygame
import random


def randomString(n):
    result = ""
    for i in range(n):
        randChar = chr(random.randint(ord('a'), ord('z')))
        if i != 0:
            result += "  "
        result += randChar
    return result

def clear(s):
    screen.fill("white")
    for y in range(100, 751, 50):
        pygame.draw.line(surface=s, color=(0, 0, 0), start_pos=(10, y), end_pos=(590, y), width=3)
        font = pygame.font.Font(None, 75)
        text_surface = font.render(randomString(10), True, (120, 120, 120))
        screen.blit(text_surface, (600 // 2 - text_surface.get_width() // 2, y - 50))


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
clear(screen)
running = True
prevCircle = None
s = pygame.display.get_surface()
text = randomString(10)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user drawing with mouse.
    bP = pygame.mouse.get_pressed(num_buttons=3)
    if bP[0]:
        pos = pygame.mouse.get_pos()

        if prevCircle != None and prevCircle != pos:
            # print("debug")
            pygame.draw.line(surface=s, color=(0, 0, 0), start_pos=prevCircle, end_pos=pos, width=5)
        pygame.draw.circle(surface=s, center=pos, radius=1, color=(0, 0, 0))
        prevCircle = pos
    else:
        prevCircle = None
    # Handle clearing whiteboard
    kP = pygame.key.get_pressed()
    if kP[pygame.K_c]:
        clear(screen)
    pygame.display.flip()
    clock.tick(60)


