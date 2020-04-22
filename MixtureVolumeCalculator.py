import pygame
pygame.init()
run = True
window_x = 1000
window_y = 800
window = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("First_Game")
white = (255,255,255)
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (135,206,235)
brown = (185,122,87)
temp = 460
k = 5.8
msg_x = 130
VSolid = int(input("Enter the volume of solid in cm^3: "))
VLiquid = int(input("Enter the volume of liquid in cm^3: "))
spacePercetage = int(input("Enter the percentage value of space in the solid: "))
VTotal = int((VSolid - (VSolid * (spacePercetage / 100 )) + VLiquid));
print("Total Volume of the mixture: ", VTotal)
Solid_height = k * VSolid
Solid_y = 600 - Solid_height
Liquid_height = k * VLiquid
Liquid_y = (600 - Solid_height) - Liquid_height
New_Liquid_height = k * (VTotal - VSolid)
New_Liquid_y = (600 - Solid_height) - New_Liquid_height
font = pygame.font.SysFont(None, 25)
def write(msg,color):
    screen_text = font.render(msg,True,color)
    window.blit(screen_text, [300,temp])
def write2(msg,color):
    screen_text = font.render(msg,True,color)
    window.blit(screen_text, [300+300,temp])
def write3(msg,color):
    screen_text = font.render(msg,True,color)
    window.blit(screen_text, [msg_x,temp])
def write4(msg,color):
    screen_text = font.render(msg,True,color)
    window.blit(screen_text, [msg_x+300+20,temp])
while (run):
    pygame.time.delay(100)
    for user_events in pygame.event.get():
        if user_events.type == pygame.QUIT:
            run = False
    window.fill(white)
    position_set = [542, 484, 426, 368, 310, 252, 194, 136, 78, 20]
    pygame.draw.rect(window, black, (100,12,15,588))
    pygame.draw.rect(window, black, (265,12,15,588))
    pygame.draw.rect(window, black, (100,600,180+19,15))
    pygame.draw.rect(window, black, (100+300,12,15,588))
    pygame.draw.rect(window, black, (265+300,12,15,588))
    pygame.draw.rect(window, black, (100+300,600,180+19,15))
    Range = int(len(position_set))
    for i in range(0,Range):
        temp = int(position_set[i])
        pygame.draw.rect(window, black, (273,temp,25,15))
        pygame.draw.rect(window, black, (273+300,temp,25,15))
        write(str((i + 1) * 10), red)
        write2(str((i + 1) * 10), red)
    temp = 600
    write(str(0), red)
    write2(str(0), red)
    temp = 0
    write3("At the begining", red)
    write4("At the end", red)
    pygame.draw.rect(window, brown, (115,(Solid_y),150,(Solid_height)))
    pygame.draw.rect(window, blue, (115,(Liquid_y),150,(Liquid_height)))
    pygame.draw.rect(window, brown, (115+300,(Solid_y),150,(Solid_height)))
    pygame.draw.rect(window, blue, (115+300,(New_Liquid_y+1),150,(New_Liquid_height)))
    pygame.display.update() 
pygame.quit()
