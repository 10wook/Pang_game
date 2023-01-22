
import pygame
import os 
pygame.init()#파이썬 초기화
 
# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption("Nado Pang Game")

#FPS
clock = pygame.time.Clock()


#이미지 불러오기
current_path = os.path.dirname(__file__)#현재 파일 위치 반환
image_path = os.path.join(current_path,"images")


#배경 만들기
background = pygame.image.load(os.path.join(image_path,"background.jpeg"))  
#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.jpeg"))  
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 위에 다가 캐릭터를 두기 위해서 사용

#캐릭터 (스프라이트) 불러오기
character =  pygame.image.load(os.path.join(image_path, "missile.png")).convert_alpha()  
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height
character_speed = 0.6


#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "shoot.png")).convert_alpha()
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러개 발사 가능
weapons = []
#무기 이동 속도
weapon_speed = 10

#돌만들기 (4개 크기에 대해서 다르게 처리)
stone_images = [
    pygame.image.load(os.path.join(image_path, "stone1.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "stone2.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "stone3.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "stone4.png")).convert_alpha()]   


#돌크기에 따른 최초 스피드

stone_speed_y = [-18,-15,-12,-9] #index 0,1,2,3에 해당
#돌 관리
stones = []
#최초 동 추가
stones.append({"pos_x":50,#x좌표
               "pos_y":50, #y좌표
               "img_idx": 0,#공 이미지 인덱스
               "to_x":3, #x축 이동 방향 -3 이면 왼쪽 3이면 오른쪽
               "to_y":-6,#y축 이동 방향
               "init_spd_y": stone_speed_y[0] #y축의 최초 속도
               })
    

#사라질 무기, 돌 정보 저장 변수
weapon_to_remove = -1
stone_to_remove = -1


#이동할 좌표 
to_x_left = 0
to_x_right = 0



#폰트 정의 
game_font = pygame.font.Font(None,40)
game_result = "Game Over"
#총시간
total_time = 100
#시작시간 정보
start_ticks = pygame.time.get_ticks()



#이벤트 루프 만들기/ 이게 돌고 있어야 파이게임이 꺼지지 않고 실행된다.
running = True
while running:
    dt = clock.tick(30)#게임화면의 초당 프레임수
    #일어난 이벤트 들을 모두 읽는 명령어라고 보면 된다.
    #이 부분 때문에 캐릭터의 이동속도가  달라지면 안되서 이걸 잘 설정 해야 한다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 이벤트가 발생하였는지?
            running = False #게임이 진행 중이 아니라고 알려준다
            
        if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
            if event.key == pygame.K_RIGHT:
                to_x_right += character_speed
            elif event.key == pygame.K_LEFT:
                to_x_left -= character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        if event.type == pygame.KEYUP: #키에서 손을 떼면 이제 끝!
            if event.key == pygame.K_RIGHT:
                to_x_right = 0
            elif event.key == pygame.K_LEFT :
                to_x_left = 0 
            
        
    character_x_pos += (to_x_left+to_x_right)*dt
    ##이 부분이 수정해서 버그 수정을 조금한 부분이다.
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 처리
    if character_y_pos <   0:
        character_y_pos =  0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height
        
    #무기 위치 관리
    
    weapons = [[w[0],w[1]-weapon_speed] for w in weapons]

    #공 움직임 관리
    for  stone_idx, stone_val in enumerate(stones):
        stone_pos_x = stone_val["pos_x"]
        stone_pos_y = stone_val["pos_y"]
        stone_img_idx = stone_val["img_idx"]

        stone_size = stone_images[stone_img_idx].get_rect().size
        stone_width = stone_size[0]
        stone_height = stone_size[1]
        
        #가로 벽에 닿았을시 공 이동 방향 변경
        if stone_pos_x < 0 or stone_pos_x > screen_width - stone_width:
            stone_val["to_x"] = stone_val["to_x"] * -1
            
            
        #세로 위치    
        if stone_pos_y >= screen_height - stage_height - stone_height:
            stone_val["to_y"] = stone_val["init_spd_y"] #  중력 가속도를 준다는 생각으로 만들면 된다.
        else:
            stone_val["to_y"] += 0.5
            
        stone_val["pos_x"] += stone_val["to_x"]
        stone_val["pos_y"] += stone_val["to_y"]
        
        
    #배경 그리기            
    screen.blit(background, (0, 0)) 
    screen.blit(stage,(0, screen_height- stage_height))

    #무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    
    #공 그리기
    for idx,val in enumerate(stones):
        stone_pos_x = val["pos_x"]
        stone_pos_y = val["pos_y"]
        stone_img_idx = val["img_idx"]
        
        screen.blit(stone_images[stone_img_idx],(stone_pos_x, stone_pos_y))
        
    #캐틱터 그리기
    screen.blit(character,(character_x_pos ,character_y_pos))
    
    #천장에 닿은 친구 빼주기
    weapons = [ [w[0],w[1]] for w in weapons if w[1]>0]
    
    stone_idx
    #### 충돌 처리 캐릭터와 공#########################
    #캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    #공 정보 업데이트
    for  stone_idx, stone_val in enumerate(stones):
        stone_pos_x = stone_val["pos_x"]
        stone_pos_y = stone_val["pos_y"]
        stone_img_idx = stone_val["img_idx"]
         
        #공 rect 정보 업데이트
        stone_rect = stone_images[stone_img_idx].get_rect()
        stone_rect.left = stone_pos_x
        stone_rect.top = stone_pos_y
        stone_mask =  pygame.mask.from_surface(stone_images[stone_img_idx])
        weapon_mask = pygame.mask.from_surface(weapon)
        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(stone_rect):
            
            running = False
            break
        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]
            
            #무기 rect 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos
            weapon_mask = pygame.mask.from_surface(weapon)
            
            
            
            #if pygame.sprite.collide_mask(weapon_mask,stone_mask):
            if weapon_rect.colliderect(stone_rect):
                #만약 닿는 다면 공과 무기가 없어진다.
                weapon_to_remove = weapon_idx
                stone_to_remove = stone_idx
                #여기서 공은 없어지고 가장 작은 공이 아닌 경우 새로운 작은 공 두개를 추가해 주어야 한다.
                if stone_img_idx < 3:
                    #현재 공 크기 정보 가져오기
                    stone_width = stone_rect.size[0]
                    stone_height = stone_rect.size[1]
                    
                    #나눠진 공 정보
                    small_stone_rect = stone_images[stone_img_idx+1].get_rect()
                    small_stone_width = small_stone_rect.size[0]
                    small_stone_height = small_stone_rect.size[1]
                    
                    
                    #왼쪽으로 튕기는 돌
                    stones.append({"pos_x":stone_pos_x + stone_width/2 - small_stone_width/2,#x좌표
                                    "pos_y": stone_pos_y + stone_height/2 - small_stone_height/2, #y좌표
                                    "img_idx": stone_img_idx + 1,#공 이미지 인덱스
                                    "to_x": -3, #x축 이동 방향 -3 이면 왼쪽 3이면 오른쪽
                                    "to_y": -6,#y축 이동 방향
                                    "init_spd_y": stone_speed_y[stone_img_idx+1]#y축의 최초 속도
                                    })
                    
                    #오른쪽으로 튕기는 돌
                    stones.append({"pos_x":stone_pos_x + stone_width/2 - small_stone_width/2,#x좌표
                                    "pos_y": stone_pos_y + stone_height/2 - small_stone_height/2, #y좌표
                                    "img_idx": stone_img_idx + 1,#공 이미지 인덱스
                                    "to_x": 3, #x축 이동 방향 -3 이면 왼쪽 3이면 오른쪽
                                    "to_y": -6,#y축 이동 방향
                                    "init_spd_y": stone_speed_y[stone_img_idx+1]
                                    })
                    break
        else:
            continue
                
        break
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    #충돌된 공 혹은 무기 없애기
    if stone_to_remove > -1:
        del stones[stone_to_remove]
        stone_to_remove = -1
        
    
        
    #모든 공이 없어졌다면 게임 클리어!
    if len(stones)==0:
        game_result = "MISSION COMPLETE"
        running = False
        
    #타이머 넣기
    #경과 시간 계산
    elapsed_time  = (pygame.time.get_ticks()- start_ticks)/1000 
    #시간 경과 나타내기
    #천으로 나누어서 초 단위로 표시함
    
    
    #출력해주는 부분
    #설정
    timer = game_font.render("Time: {}".format(str(int(total_time - elapsed_time))),True,(255,255,255))
    #보이기
    screen.blit(timer,(10, 10))
    
    if total_time - elapsed_time <= 0:
        game_result = "Time over"
        
         
        running = False
     
    #if total_time - elapsed_time <= -2:   
    #    running = False
        
        
    pygame.display.update()      

msg = game_font.render(game_result,True,(255,255,0))
msg_rect = msg.get_rect(center = (int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()
pygame.time.delay(2000) 




#게임이 종료 되면 종료
pygame.quit()