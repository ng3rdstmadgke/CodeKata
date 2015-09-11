__author__ = 'midorikawakeita'
import random
"""
....... ....... ..Q.... ....... ...Q... ....... .......

#.###..
####..#
##Q####
######.
###Q###
..####.
.###.##

#Q#####
#######
##Q####
######Q
###Q###
Q######
####Q##
※Qが入っているマスの上下左右斜めにはおけない
１リストからQを検索する
２Qを見つけたら、その上下左右斜めのマスを#に変換
３
"""
class N_queen:
    def __init__(self,input):
        self.base_map  = input.split(" ")
        for i in range(len(self.base_map)):
            self.base_map [i] = list(self.base_map[i])
        self.width = len(self.base_map[0])
        self.height = len(self.base_map)

    """Qを探してQが動く範囲をぬりつぶす"""
    def check(self,mapping):
        for i in range(self.height):
            for n in range(self.width):
                if mapping[i][n] == "Q":
                    #左右を＃に置換
                    mapping[i] = list("#" * self.width)
                    #上下を＃に置換
                    for h in range(self.height):
                        mapping[h][n] = "#"
                    #斜めを＃に置換
                    y = 1
                    x = 1
                    while True:
                        count = 0
                        if ((i - y) >= 0) and ((n + x) <= self.width - 1):#右斜め上
                            mapping[i - y][n + x] = "#"
                            count += 1
                        if ((i + y) <= (self.height - 1)) and ((n + x) <= (self.width - 1)):#右斜め下
                            mapping[i + y][n + x] = "#"
                            count += 1
                        if ((i - y) >= 0) and ((n - x) >= 0):#左斜め上
                            mapping[i - y][n - x] = "#"
                            count += 1
                        if ((i + y) <= (self.height -1)) and ((n -x) >= 0):#左斜め下
                            mapping[i + y][n - x] = "#"
                            count += 1
                        y += 1
                        x += 1
                        if count == 0:
                            mapping[i][n] = "q"
                            break
        return mapping

    """ランダムで１００回"""
    def search_path(self,c_map):
        map_list = []
        qnn = 0
        for e in range(5):
            for n in [0,1,3,5,6]:
                count_1 = []
                for i in range(self.width):
                    if c_map[n][i] == ".":
                        count_1.append(i)
                if count_1:
                    num = random.choice(count_1)
                    c_map[n][num] = "Q"
                else:
                    pass
            random_map = self.check(c_map)
            map_list += "".join(["".join(i) for i in random_map])
        for i in range(len(map_list)):
            qn = map_list[i].count("q")
            if qn > qnn:
                qnn = qn
                i_num = i
        return map_list[i_num]





