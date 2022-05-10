/'''


문제

로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 북쪽에서부터 r번째, 서쪽에서부터 c번째로 위치한 칸은 (r, c)로 나타낼 수 있다.

로봇 청소기는 다음과 같이 작동한다.

    현재 위치를 청소한다.
    현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
        현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
        1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.

입력

첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

출력

로봇 청소기가 청소하는 칸의 개수를 출력한다.


'''/

import sys
place={}

north_wall=0
east_wall=0
south_wall=0
west_wall=0

north_clean=0
east_clean=0
south_clean=0
west_clean=0

N, M=list(map(int,input().split()))
A, B, C=list(map(int,input().split()))
for i in range(N):
    place[i]=sys.stdin.readline().strip().split()
    
    
class vacuum:

    def __init__(self, r, c, d):
        self.r=r
        self.c=c
        self.d=d

        self.north_wall=north_wall
        self.east_wall=east_wall
        self.south_wall=south_wall
        self.west_wall=west_wall
        
        self.north_clean=north_clean
        self.east_clean=east_clean
        self.south_clean=south_clean
        self.west_clean=west_clean
    def d(self):
        return self.d  

    
    def front_wall(self):
        if self.d==0:
            if self.north_wall==1:
                return 1
            elif self.north_wall==0:
                return 0
        elif self.d==1:
            if self.east_wall==1:
                return 1
            elif self.east_wall==0:
                return 0
        elif self.d==2:
            if self.south_wall==1:
                return 1
            elif south_wall==0:
                return 0
        elif self.d==3:
            if self.west_wall==1:
                return 1
            elif self.west_wall==0:
                return 0




    def front_clean(self):
        if self.d==0:
            if self.north_clean==1:
                return 1
            elif self.north_clean==0:
                return 0
        elif self.d==1:
            if self.east_clean==1:
                return 1
            elif east_clean==0:
                return 0
        elif self.d==2:
            if self.south_clean==1:
                return 1
            elif south_clean==0:
                return 0
        elif self.d==3:
            if self.west_clean==1:
                return 1
            elif self.west_clean==0:
                return 0





    def left_clean(self):
        if self.d==0:
            if self.west_clean==1:
                return 1
            elif self.west_clean==0:
                return 0
        elif self.d==1:
            if self.north_clean==1:
                return 1
            elif self.north_clean==0:
                return 0
        elif self.d==2:
            if self.east_clean==1:
                return 1
            elif self.east_clean==0:
                return 0
        elif self.d==3:
            if self.south_clean==1:
                return 1
            elif self.south_clean==0:
                return 0        



    def left_clean(self):
        if self.d==0:
            if self.west_clean==1:
                return 1
            elif self.west_clean==0:
                return 0
        elif self.d==1:
            if self.north_clean==1:
                return 1
            elif self.north_clean==0:
                return 0
        elif self.d==2:
            if self.east_clean==1:
                return 1
            elif self.east_clean==0:
                return 0
        elif self.d==3:
            if self.south_clean==1:
                return 1
            elif self.south_clean==0:
                return 0  



    def left_wall(self):
        if self.d==0:
            if self.west_wall==1:
                return 1
            elif west_wall==0:
                return 0
        elif self.d==1:
            if self.north_wall==1:
                return 1
            elif self.north_wall==0:
                return 0
        elif self.d==2:
            if self.east_wall==1:
                return 1
            elif self.east_wall==0:
                return 0
        elif self.d==3:
            if self.south_wall==1:
                return 1
            elif self.south_wall==0:
                return 0        

    
    def back(self):
        if self.d==0:
            if self.south_wall==1:
                return 1
            elif self.south_wall==0:
                return 0
        elif self.d==1:
            if self.west_wall==1:
                return 1
            elif self.west_wall==0:
                return 0
        elif self.d==2:
            if self.north_wall==1:
                return 1
            elif self.north_wall==0:
                return 0
        elif self.d==3:
            if self.east_wall==1:
                return 1
            elif self.east_wall==0:
                return 0
    
    
    
    
    def clean_current_place(self):
        place[self.r][self.c]='*'

        

    def turn_left(self):
        if self.d==0:
            self.d=3
        elif self.d==1:
            self.d=0
        elif self.d==2:
            self.d=1
        elif self.d==3:
            self.d=2
            

    def go_front(self):
        if self.d==0:
            self.r=self.r-1
        elif self.d==1:
            self.c=self.c+1
        elif self.d==2:
            self.r=self.r+1
        elif self.d==3:
            self.c=self.c-1


    def go_back(self):
        if self.d==0:
            self.r=self.r+1
        elif self.d==1:
            self.c=self.c-1
        elif self.d==2:
            self.r=self.r-1
        elif self.d==3:
            self.c=self.c+1
            

    def check_clean(self):
        if place[self.r-1][self.c]=='*':
            self.north_clean=1
        else:
            self.north_clean=0
        if place[self.r][self.c+1]=='*':
            self.east_clean=1
        else:
            self.east_clean=0
        if place[self.r+1][self.c]=='*':
            self.south_clean=1
        else:
            self.south_clean=0
        if place[self.r][self.c-1]=='*':
            self.west_clean=1
        else:
            self.west_clean=0


    def check_wall(self):
        if place[self.r-1][self.c]=='1':
            self.north_wall=1
        else:
            self.north_wall=0
        if place[self.r][self.c+1]=='1':
            self.east_wall=1
        else:
            self.east_wall=0
        if place[self.r+1][self.c]=='1':
            self.south_wall=1
        else:
            self.south_wall=0
        if place[self.r][self.c-1]=='1':
            self.west_wall=1
        else:
            self.west_wall=0



    

shaomi=vacuum(A, B, C)
    
while True:
    shaomi.clean_current_place()
    shaomi.check_wall()
    shaomi.check_clean()






    if (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0):        
        shaomi.go_back()



    
    elif (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==1)\
    or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==1):        
        break
    else:   
        while True:
            shaomi.turn_left()
            if shaomi.front_wall()==0 and shaomi.front_clean()==0:
                shaomi.go_front()
                break
            elif (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_clean==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_clean==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_clean==1 and shaomi.west_wall==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_clean==1 and shaomi.back()==0)\
            or (shaomi.north_wall==1 and shaomi.east_wall==1 and shaomi.south_wall==1 and shaomi.west_wall==1 and shaomi.back()==0):        
                break





ans=0
for i in range(N):
    ans=ans+place[i].count('*')
print(ans)