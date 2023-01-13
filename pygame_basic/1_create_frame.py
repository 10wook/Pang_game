import pygame

pygame.init()#파이썬 초기회

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("Nado Pang Game")


#이벤트 루프 만들기/ 이게 돌고 있어야 파이게임이 꺼지지 않고 실행된다.
running = True
while running:
    #일어난 이벤트 들을 모두 읽는 명령어라고 보면 된다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 이벤트가 발생하였는지?
            running = False #게임이 진행 중이 아니라고 알려준다
            


#게임이 종료 되면 종료
pygame.quit()
 