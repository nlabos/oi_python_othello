# 黒：１　白：ー１
BLACK = 1
WHITE = -1
BLANK = 0

# 盤
import numpy as np

ban = np.zeros((8, 8))
ban[3][3] = ban[4][4] = BLACK
ban[3][4] = ban[4][3] = WHITE

# 画像化
def render():
    print("⁑" * 17)
    for y in ban:
        for x in y:
            if x == BLANK:
                print(" - ", end=" ")
            elif x == BLACK:
                print(" ● ", end=" ")
            elif x == WHITE:
                print(" ○ ", end=" ")
        print("\n")

# コマ反転（前提）
class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return vector2(self.x - other.x, self.y - other.y)

    def normalize(self):
        return vector2(normalize_scalar(self.x), normalize_scalar(self.y))

def normalize_scalar(x: int):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    return 1


def changestone(start, end, koma):
    diff = (end - start).normalize()
    dx, dy = diff.x, diff.y

    x, y = start.x, start.y
    while True:
        ban[y][x] = koma
        x += dx
        y += dy
        if x == end.x and y == end.y:
            break



# コマ設置
def setstone(x, y, koma):
    if ban[y][x] != BLANK:
        return  # すでにコマが置いてある場合は何もしない

    ban[y][x] = koma
    overturn(x, y, koma)

# コマ反転
def overturn(x, y, koma):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 全方向

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        flipped = []  # 反転させるコマの位置を保存するリスト

        while 0 <= nx < 8 and 0 <= ny < 8:
            if ban[ny][nx] == BLANK:
                flipped = []  # 空白マスに到達したら反転をキャンセル
                break
            elif ban[ny][nx] == koma:
                for fx, fy in flipped:  # 反転処理
                    ban[fy][fx] = koma
                break
            else:
                flipped.append((nx, ny))  # 反転予定のリストに追加
            nx += dx
            ny += dy


# テスト
render()
setstone(2, 3, WHITE)
render()
setstone(3, 2, WHITE) # <- ここ修正。3,3だとすでにコマがあるので変更されない
render()
setstone(2, 2, BLACK)
render()
setstone(4,2,BLACK) #追加テスト
render()
setstone(5,2,BLACK) #追加テスト
render()
