import pygame

pygame.init()#파이썬 초기회
 
# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Pang Game")

#FPS
clock = pygame.time.Clock()


#이미지 불러오기
background = pygame.image.load("/Users/hanyoungwook/2023-1/Pang_game/pygame_basic/background.jpeg")  

#캐릭터 (스프라이트) 불러오기
character =  pygame.image.load("/Users/hanyoungwook/2023-1/Pang_game/pygame_basic/char.png")  
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height
character_speed = 0.6

#이동할 좌표 
to_x = 0
to_y = 0

#적 만들기
enemy =  pygame.image.load("/Users/hanyoungwook/2023-1/Pang_game/pygame_basic/enemy.png")  
enemy_size = enemy .get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = screen_height/2 -enemy_height/2
enemy_speed = 0.6


#폰트 정의 
game_font = pygame.font.Font(None,40)

#총시간
total_time = 10
#시작시간 정보
start_ticks = pygame.time.get_ticks()



#이벤트 루프 만들기/ 이게 돌고 있어야 파이게임이 꺼지지 않고 실행된다.
running = True
while running:
    dt = clock.tick(120)#게임화면의 초당 프레임수
    #일어난 이벤트 들을 모두 읽는 명령어라고 보면 된다.
    #이 부분 때문에 캐릭터의 이동속도가  달라지면 안되서 이걸 잘 설정 해야 한다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 이벤트가 발생하였는지?
            running = False #게임이 진행 중이 아니라고 알려준다
            
        if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: #키에서 손을 떼면 이제 끝!
            if event.key == pygame.K_RIGHT:
                to_x = 0 
            if event.key == pygame.K_LEFT:
                to_x = 0
            if event.key == pygame.K_UP:
                to_y = 0
            if event.key == pygame.K_DOWN:
                to_y = 0
        
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 처리
    if character_y_pos <  + character_height:
        character_y_pos = + character_height
    elif character_y_pos > screen_height :
        character_y_pos = screen_height 
        
    #충돌 처리

    #일단 이 친구의 값을 계속 업데이트 하고 있는 상태라고 보면 된다.  
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    #캐릭터가 적이랑 충돌했냐?
    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False
    #배경 그리기            
    screen.blit(background, (0, 0)) 
    #screen.fill((0, 0, 255)) #혹은 배경 채우기
    #캐틱터 그리기
    screen.blit(character,(character_x_pos ,character_y_pos))
    #적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    
    #타이머 넣기
    #경과 시간 계산
    elapsed_time  = (pygame.time.get_ticks()- start_ticks)/1000 
    #시간 경과 나타내기
    #천으로 나누어서 초 단위로 표시함
    
    
    #출력해주는 부분
    #설정
    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    #보이기
    screen.blit(timer,(10, 10))
    
    if total_time - elapsed_time <= 0:
        time_over = game_font.render("TIME OVER!!",True,(0, 0, 0))
        screen.blit(time_over,(screen_width/2 -70,screen_height/2))
        #print("시간초과")
     
    if total_time - elapsed_time <= -2:   
        running = False
    pygame.display.update()      
    

#게임이 종료 되면 종료
pygame.quit()