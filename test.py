# Example file showing a basic pygame "game loop"
import pygame

# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((360, 720))
clock = pygame.time.Clock()
running = True
dt = 0
tablero = [[0 for j in range(10)] for i in range(20)]


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
posbot = 50
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Recorrer la matriz
    for i in range(20):
        posy = 50+i*17
        for j in range(10):
            posx = 100+j*17
            pygame.draw.rect(screen,"blue",(posx,posy,15,15))

    if(player_pos.x<250 and player_pos.x>100 and player_pos.y<372 and player_pos.y>50):
        print(player_pos)    
        pygame.draw.rect(screen,"green",(player_pos.x,player_pos.y,15,15))
    # pygame.draw.circle(screen, "red", player_pos, 15)

    pygame.draw.rect(screen, "black", [98, 48, 172, 342], 2)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 2500

pygame.quit()