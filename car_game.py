#khai bao thu vien
import pygame
from pygame.locals import *
import random 
pygame.init()
# Khởi tạo âm thanh
pygame.mixer.init()
# Tải file nhạc
pygame.mixer.music.load('nhac.wav')
# Bắt đầu phát nhạc (lặp vô hạn)
pygame.mixer.music.play(-1)
#mau nen
gray=(100,100,100)
green=(0,95,105)
orange=(242,111,51)
yellow=(255,232,0)
red=(200,0,0)
white=(255,255,255)
#tao cua so game
width=800
height=500
screen_size=(width,height)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption('Game đua cơ sở UEH')
#khoi tao bien
gameover=False
speed=2
score=0
#duong chay
road_width=300
street_width=10
street_height=50
#lane duong
land_left=150
land_center=250
land_right=350
lanes=[land_left,land_center,land_right]
lane_move_y=0
#road va edge
road=(100,0,road_width,height)
left_edge=(95,0,street_width,height)
right_edge=(395,0,street_width,height)
#vi tri ban dau xe player
player_x=250
player_y=400
#doi tuong xe khac
class Vehicle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        #scale images   
        image_scale=45/ image.get_rect().width
        new_width= image.get_rect().width* image_scale
        new_heigt= image.get_rect().height* image_scale
        self.image = pygame.transform.scale(image,(new_width,new_heigt))
        self.rect= self.image.get_rect()
        self.rect.center=[x,y]
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image= pygame.image.load('images/car.png')
        super().__init__(image,x,y)
#sprite groups
player_group = pygame.sprite.Group()
Vehicle_group= pygame.sprite.Group()
# tao xe nguoi choi
player= PlayerVehicle(player_x,player_y)
player_group.add(player)
# load xe khac
image_name=['ueh.png','3i.png']
vehicle_images=[]
for i in image_name:
    image= pygame.image.load('images/'+ i)
    vehicle_images.append(image)
#load hinh va cham
crash= pygame.image.load('images/crash.png')
crash_rect=crash.get_rect()
#cai dat fps
clock=pygame.time.Clock()
fps= 120
#vong lap xu li game
running=True
while running:
    # chinh frame hinh tren giay
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        #dieu khien xe
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > land_left:
                player.rect.x -=100
            if event.key == K_RIGHT and player.rect.center[0] < land_right:
                player.rect.x +=100
        #check va cham
        for vehicle in Vehicle_group:
            if pygame.sprite.collide_rect(player,vehicle):
                gameover=True
    # check va cham
    if pygame.sprite.spritecollide(player,Vehicle_group,True):
        gameover=True
        crash_rect.center= [player.rect.center[0],player.rect.top]
    #ve dia hinh co
    screen.fill(green)
    # ve road
    pygame.draw.rect(screen,gray,road)
    #ve edge-hanh lang duong
    pygame.draw.rect(screen,orange,left_edge)
    pygame.draw.rect(screen,orange,right_edge)
    #ve lane duong
    lane_move_y += speed * 2
    if lane_move_y >= street_height * 2:
        lane_move_y=0
    for y in range(street_height* -2,height,street_height*2):
        pygame.draw.rect(screen,white,(land_left+45,y+ lane_move_y,street_width,street_height))
        pygame.draw.rect(screen,white,(land_center+45,y+ lane_move_y,street_width,street_height))
    #ve xe player
    player_group.draw(screen)
    #ve phuong tien khac
    if len(Vehicle_group) <2:
        add_vehicle = True
        for vehicle in Vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            lane= random.choice(lanes)
            image= random.choice(vehicle_images)
            vehicle= Vehicle(image,lane,height/ -2)
            Vehicle_group.add(vehicle)
    # cho xe khac chay
    for vehicle in Vehicle_group:
        vehicle.rect.y += speed
        # remove vehicle
        if vehicle.rect.top >= height:
            vehicle.kill()
            score +=1
            # tang toc do kho 
            if score > 0 and score % 5 ==0:
                speed +=2
    # ve nhom xe cong cong
    Vehicle_group.draw(screen)
    #ve hien thi them
    font= pygame.font.Font(pygame.font.get_default_font(),16)
    text=font.render(f'Score: {score}',True,white)
    text_rect= text.get_rect()
    text_rect.center=(50,40)
    screen.blit(text,text_rect)
    # chen hình ảnh với những số điểm khác nhau
    if score >= 0:
        original_special_image = pygame.image.load('images/9.png')
        resized_special_image = pygame.transform.scale(original_special_image, (350,350)) 
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  
        screen.blit(resized_special_image, special_rect)
    if score >= 5:
        special_image = pygame.image.load('images/csN1.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  
        screen.blit(resized_special_image, special_rect)
    if score >= 10:
        special_image = pygame.image.load('images/3.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  
        screen.blit(resized_special_image, special_rect)
    if score >= 15:
        special_image = pygame.image.load('images/4.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  # Adjust the position as needed
        screen.blit(resized_special_image, special_rect)
    if score >= 20:
        special_image = pygame.image.load('images/7.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  # Adjust the position as needed
        screen.blit(resized_special_image, special_rect)
    if score >= 25:
        special_image = pygame.image.load('images/6.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  # Adjust the position as needed
        screen.blit(resized_special_image, special_rect)
    if score >= 30:
        special_image = pygame.image.load('images/8.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  # Adjust the position as needed
        screen.blit(resized_special_image, special_rect)
    if score >= 35:
        if score % 2 == 0:
            special_image = pygame.image.load('images/1.png')
        else:
            special_image = pygame.image.load('images/2.png')
        resized_special_image = pygame.transform.scale(special_image, (350, 350))
        special_rect = resized_special_image.get_rect()
        special_rect.topright = (width - 10, 10)  
        screen.blit(resized_special_image, special_rect)
    # thong bao điểm và kiểm tra người chơi có muốn tiếp tục chơi hay thoát game :
    if gameover :
        screen.blit(crash,crash_rect)
        pygame.draw.rect(screen,red,(0,50,width,100))
        font= pygame.font.Font(pygame.font.get_default_font(),16)
        text = font.render(f'Game over! Score: {score} . Play again? (Y/N)', True, white)
        text_rect= text.get_rect()
        text_rect.center=(width/2,100)
        screen.blit(text,text_rect)
    
    pygame.display.update()
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover= False
                running = False
            if event.type == KEYDOWN:
                if event.key == K_y:
                    #reset game
                    gameover= False
                    score=0
                    speed=2
                    Vehicle_group.empty()
                    player.rect.center = [player_x,player_y]
                elif event.key == K_n:
                    #exit game 
                    gameover= False
                    running= False
pygame.quit()
                                  


