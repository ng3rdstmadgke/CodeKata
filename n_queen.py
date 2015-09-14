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



    """0,1,3,5,6行目のどこにＱを入れるかをfor文で書く"""
    def set_queen(self,c_map):
        map_list = []
        num_list = []
        for a in [1,5,6]:
            for b in [4,5]:
                for c in [0,5,6]:
                    for d in [0,1,6]:
                        for e in [0,4]:
                            num_list.append([a,b,c,d,e])
        for i in range(len(num_list)):
            c_map[0][num_list[i][0]] = "Q"
            c_map[1][num_list[i][1]] = "Q"
            c_map[3][num_list[i][2]] = "Q"
            c_map[5][num_list[i][3]] = "Q"
            c_map[6][num_list[i][4]] = "Q"
            d_map = self.check(c_map)
            map_list.append("".join(["".join(i) for i in d_map]))
            c_map[0][num_list[i][0]] = "."
            c_map[1][num_list[i][1]] = "."
            c_map[3][num_list[i][2]] = "."
            c_map[5][num_list[i][3]] = "."
            c_map[6][num_list[i][4]] = "."
            #print(map_list[i])
        q_num_list = []
        for i in range(len(map_list)):
            q_num_list.append(map_list[i].count("q"))
        max_num = max(q_num_list)
        max_map_list = []
        for i in range(len(q_num_list)):
            if q_num_list[i] == max_num:
                max_map_list.append(map_list[i])

        #print(len(num_list))
        return max_map_list

if __name__ == "__main__":
    a = N_queen("....... ....... ..Q.... ....... ...Q... ....... .......")
    b = a.check(a.base_map)
    c = a.set_queen(b)
    for i in range(len(c)):
        for n in range(7):
            print(c[i][7 * n:7 * (n + 1)])
