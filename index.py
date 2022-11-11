# import the pygame module
import pygame
import pygame
import pandas as pd 
import numpy as np 
import time 
#cores
cor_bg = (10,10,10) 
cor_grid = (40,40,40)
cor_morreu = (170,170,170) 
cor_vivo = (255,255,255)




def update(screen, celula, tamanho, progresso = False):
    updated_celula = np.zeros((celula.shape[0], celula.shape[1]))

    for row, col in np.ndindex(celula.shape):
        alive = np.sum(celula[row-1:row+2, col-1:col+2]) - celula[row,col]
        color = cor_bg if celula[row, col] == 0 else cor_vivo

        if celula[row, col] == 1:
            
            if alive < 2 or alive > 3:
                if progresso:
                    color = cor_morreu
            elif 2 <= alive <= 3:
                updated_celula[row, col]  = 1
                if progresso:
                    color = cor_vivo
        else:
            if alive == 3:
                updated_celula[row, col] = 1
                if progresso:
                    color = cor_vivo
        pygame.draw.rect(screen, color, (col*tamanho, row*tamanho, tamanho-1, tamanho-1) )

    return updated_celula

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    celula = np.zeros((60, 80))
    screen.fill(cor_grid)
    update(screen, celula, 10)

    pygame.display.flip()
    pygame.display.update()
    
    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, celula, 10)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                celula[pos[1] // 10, pos[0] // 10] = 1
                update(screen, celula, 10)
                pygame.display.update()
        screen.fill(cor_grid)

        if running:
           celula = update(screen, celula, 10, progresso=True)
           pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()

