import pygame

pygame.init()#파이썬 초기회
 
# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Pang Game")
#이미지 불러오기
background = pygame.image.load("/Users/hanyoungwook/2023-1/Pang_game/pygame_basic/background.jpeg")  

#캐릭터 (스프라이트) 불러오기
character =  pygame.image.load("/Users/hanyoungwook/2023-1/Pang_game/pygame_basic/char.png")  
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height


#이벤트 루프 만들기/ 이게 돌고 있어야 파이게임이 꺼지지 않고 실행된다.
running = True
while running:
    #일어난 이벤트 들을 모두 읽는 명령어라고 보면 된다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 이벤트가 발생하였는지?
            running = False #게임이 진행 중이 아니라고 알려준다
    
    screen.blit(background, (0, 0))  #배경 그리기
    #screen.fill((0, 0, 255)) #혹은 배경 채우기
    
    screen.blit(character,(character_x_pos - character_width/2 ,character_y_pos - character_height))
    pygame.display.update()      
    

#게임이 종료 되면 종료
pygame.quit()