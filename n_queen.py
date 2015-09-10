__author__ = 'midorikawakeita'
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

    def search_q(self,mapping):
        for i in range(self.height):
            for n in range(self.width):
                if mapping[i][n] == "Q":
                    mapping[i][n] = "A"
                    #左右を＃に置換
                    mapping[i] = list("#" * self.width)
                    #上下を＃に置換
                    for h in range(self.height):
                        mapping[h][n] = "#"
                    #右斜めを＃に置換
                    while True:
                        y = 1
                        x = 1
                        if ((i - y) >= 0) and ((n + x) <= self.width):#右斜め上
                            mapping[i - y][n + x]
                    #左斜めを＃に置換
                    return i,n





