
#黒：１　白：ー１
BLACK=1
WHITE=-1
BLANK=0

#盤
import numpy as np

ban=np.zeros((8,8))
ban[3][3]=ban[4][4]=BLACK
ban[3][4]=ban[4][3]=WHITE

#反転用ヘルパー関数:数の大きさを1にする
def normalize(x:int):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    return 1

#画像化
def render():
    print("⁑"*17)
    for y in ban:
        for x in y:
            if x == BLANK:
                print(" - ",end=" ")
            elif x == BLACK:
                print(" ● ",end=" ")
            elif x == WHITE:
                print(" ○ ",end=" ")
        print("
")
render()

#コマ反転（前提）
class vector2:
    x=0
    y=0

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __sub__(self,other):
        self.x -= other.x
        self.y -= other.y
        return self

    def normalRaw(self):
        result = vector2(self.x,self.y)
        result.x = 0 if result.x == 0 else -1 if result.x < 0 else 1
        result.y = 0 if result.y == 0 else -1 if result.y < 0 else 1

        return result
    
def changestone(start,end,koma):
    if start.x > end.x:
     start.x,end.x = end.x,start.x
    if start.y > end.y:
     start.y,end.y=end.y,start.y

    #斜め
    tmp = (end - start).normalRaw()
    # dx,dy=normalize(start.x-end.x),normalize(start.y-end.y)
    dx, dy = tmp.x, tmp.y
    #print(f"start: {start.x}, {start.y}")
    #print(f"end: {end.x}, {end.y}")
    #print(f"dx, dy : {dx}, {dy}")
    
    if dx * dy == 0:
        print("縦横起動")
        #横
        changeStoneHorizontal(start, end, koma, dx)
    
        #縦
        changeStoneVertical(start, end, koma, dy)
        return
    
    print("斜め起動")
    
    for y_t in range(start.y, end.y, dy):
        for x_t in range(start.x, end.x, dx):
            return    
    for x_t,y_t in zip(range(start.x,end.x,dx),range(start.y,end.y,dy)):
        ban[y_t][x_t]=koma

def changeStoneHorizontal(start: vector2, end: vector2, koma, dx):
    if dx == 0:
        return
    
    #横
    for x in range(start.x,end.x, dx):
        print("横反転詳細"+f"ban[{start.y}][{x}]")
        ban[start.y][x]=koma

def changeStoneVertical(start, end, koma, dy):
    if dy == 0:
        return
    
    #縦
    for y in range(start.y,end.y, dy):
        print("縦反転詳細"+f"ban[{y}][{start.x}]")
        ban[y][start.x]=koma

#コマ設置
def setstone(x,y,koma):
    ban[y][x]=koma
    overturn(x, y, koma)
        
#コマ反転
def overturn(x, y, koma):
        print("縦横反転起動")
#横
        for x1 in range(x+1,8):
            if ban[y][x1]==koma:
                changestone(vector2(x,y),vector2(x1,y),koma)
                break
            if ban[y][x1]==BLANK:
                break
        for x2 in range(x-1,0,-1):
            if ban[y][x2]==koma:
                changestone(vector2(x,y),vector2(x2,y),koma)
                break
            if ban[y][x2]==BLANK:
                break
#縦       
        for y1 in range(y+1,8):
            if ban[y1][x]==koma:
            # ここ怪しい
                print(f"x {x}")
                changestone(vector2(x,y), vector2(x,y1), koma)
                print(f"x {x}")
                break
            if ban[y1][x]==BLANK:
                break

        for y2 in range(y-1,0,-1):
            if ban[y2][x]==koma:
                changestone(vector2(x,y),vector2(x,y2),koma)
                break
            if ban[y2][x]==BLANK:
                break
#斜め                
        for i in range(8):
            x_t=x+i+1
            y_t=y+i+1
            if x_t < 0 or 7 < x_t or y_t < 0 or 7 < y_t:    
                print("斜め探査起動")
                break
            if ban[y_t][x_t]==BLANK:
                break
            if ban [y_t][x_t]==koma:
                if (x_t-x)*(y_t-y)!=0:
                    print("斜め反転起動")    
                    print(f"ban[{y_t}][{x_t}] == koma({koma})")    
                    print(f"start {x}, {y}")
                    changestone(vector2(x,y),vector2(x_t,y_t),koma)
                    break
            
                
#テスト＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊


setstone(2,3,WHITE)
render()
setstone(3,3,WHITE)
render()
setstone(2,2,BLACK)
render()

