import pygame, sys
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        #screen.fill("light pink")
        mole_pos = (0, 0)
        mole_rect = mole_image.get_rect(topleft=mole_pos)
        running = True
        while running:
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         running = False
            #screen.fill("light green")
            # pygame.display.flip()
            # clock.tick(60)
            # mole_pos = (0, 0)
            # mole_rect = mole_image.get_rect(topleft=mole_pos)
            screen.fill("light pink")
            screen.blit(mole_image, mole_rect)
            for i in range(1, 17):
                pygame.draw.line(screen, "black", (0, i*32), (640, i*32))
            for i in range(1, 21):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        mole_pos = (random.randrange(20) * 32, random.randrange(16) * 32)
                        mole_rect.topleft = mole_pos
                    # x, y = event.pos
                    # if x <= 32 and y <= 32:
                    #     a = random.randrange(32, 641)
                    #     b = random.randrange(32, 513)
                    #     screen.blit(mole_image, mole_image.get_rect(center=(a, b)))

            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
