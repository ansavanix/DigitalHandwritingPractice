import pygame
import random


def randomString(n):
    result = ""
    for i in range(n):
        randChar = chr(random.randint(ord('a'), ord('z')))
        if i != 0:
            result += " "
        result += randChar
    return result


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
screen.fill("white")
running = True
prevCircle = None
s = pygame.display.get_surface()

while running:
    for y in range(100, 751, 50):
        pygame.draw.line(surface=s, color=(0, 0, 0), start_pos=(10, y), end_pos=(590, y), width=3)
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
        screen.fill("white")
    pygame.display.flip()
    clock.tick(60)


