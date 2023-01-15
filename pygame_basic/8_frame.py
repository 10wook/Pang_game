import pygame
#########################################################################
#기본 초기화 (반드시 해야하는 일들)
pygame.init()#파이썬 초기회
 
# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Pang Game") # 원하는 게임 이름 적기


#FPS
clock = pygame.time.Clock()
########################################################################




# 1. 사용자 게임 초기화 (배걍 화면, 게임 이미지, 좌표, 속도, 폰트 등 )
#폰트 정의 
game_font = pygame.font.Font(None,40)

#2. 이벤트 루프 만들기/ 이게 돌고 있어야 파이게임이 꺼지지 않고 실행된다.
running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임수
    #일어난 이벤트 들을 모두 읽는 명령어라고 보면 된다.
    #이 부분 때문에 캐릭터의 이동속도가  달라지면 안되서 이걸 잘 설정 해야 한다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 이벤트가 발생하였는지?
            running = False #게임이 진행 중이 아니라고 알려준다
            
#3. 게임 캐릭터 위치 정의 
    #4.충돌 처리

    
    #5. 화면에 그리기         
  
        
    pygame.display.update()      


pygame.time.delay(2000) 

#게임이 종료 되면 종료
pygame.quit()