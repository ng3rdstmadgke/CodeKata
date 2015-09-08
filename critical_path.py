__author__ = 'midorikawakeita'
"""
"7 9 A B 10 A C 3 B D 4 B E 7 C D 7 C F 9 D E 2 E G 1 F G 7"
1.入力された値をリスト化
    node = 7
    path = 9
    list = [[A,B,10],[A,C,3],[B,D,4],[B,E,7],[C,D,7],[C,F,9],[D,E,2],[E,G,1],[F,G,7]]

2.A = 0,B = 1,C = 2...というようなノードと数値の対応リストを作る

3.listを変数にあわせて置き換える
    list1 = [[0,1,10],[0,2,3],[1,3,4],[1,4,7],[2,3,7],[2,5,9],[3,4,2],[4,6,1],[5,6,7]]

4c_mapに変換
    1c_mapを生成するcritical_path = []
        init_num=0
    c_map = [[init_num for i in range(node)] for i in range(node)]
    2c_mapにlist1 + <前の経路の重み>を代入していく
    #最も重い経路と、list1[2]を足した値c_mapに代入していく作業をすべてのpathに対して行う
    for i in range(path):
        #出発地点の最も重い経路を算出
        node_weight_list = []
        for j in range(node):
            node_weight =c_map[j][list1[i][0]]
            node_weight_list.append(node_weight)
        max_node = max(node_weight_list)
        #最も重い経路と、list1[2]を足した値c_mapに代入する
    c_map[list1[i][0][list1[i][1]] = list1[i][2] + max_node
        #この作業を更新がなくなるまで続ける（while）

            0A 1B 2C 3D 4E 5F 6G　到着
        0A [ 0,10, 3, 0, 0, 0, 0]
        1B [ 0, 0, 0,14,17, 0, 0]
        2C [ 0, 0, 0,10, 0,12, 0]
        3D [ 0, 0, 0, 0,16, 0, 0]
        4E [ 0, 0, 0, 0, 0, 0,18]
        5F [ 0, 0, 0, 0, 0, 0,19]
        6G [ 0, 0, 0, 0, 0, 0, 0]
        出発


5c_map[i][node-1]から最大値とその座標を検出→さかのぼって最大のルートを検索
    num_list = []#ある到着地点におけるコストのリスト
    search_path = node-1#
    critical_path = []
    while True:
        for i in range(node):
            num_list.appendc_map[i][search_path])
        #到着点の最大値を求める
        critical_num = max(num_list)
        #座標を求める
        for i in range(node)
            ifc_map[i][search_path] == critical_num:
                critical_path.append(serach_path)
                serch_path = i
"""

class Critical:
    """初期化メソッド：変数node,path,を定め、list1c_mapを作成"""
    def __init__(self,strs):
        raw_list = strs.split(" ")
        self.node = int(raw_list[0])
        self.path = int(raw_list[1])
        pre_list = raw_list[2:]
        self.list = [pre_list[i * 3:i * 3 + 3] for i in range(self.path)]
        for i in range(self.path):
            self.list[i][0] = self.si_convert(self.list[i][0])
            self.list[i][1] = self.si_convert(self.list[i][1])
            self.list[i][2] = int(self.list[i][2])

        base_num = 0
        self.c_map = [[base_num for i in range(self.node)] for i in range(self.node)]

    """A-Zを0-25の数字に変換する関数"""
    def si_convert(self,i):
        if isinstance(i, int):
            return chr(i+65)
        if isinstance(i, str):
            return ord(i)-65

    """mapに経路のコストを代入する=>それぞれのノードへのコストが最大となっmapを返す"""
    def map_edit(self):
        #出発地点までの経路のコストと、到着地点のコストを足した値c_mapに代入していく
        while True:
            break_count = 0
            for i in range(self.path):
                node_cost_list = []
                #パス["A","B",10]の出発地点の最大コストを求める
                for j in range(self.node):
                    node_cost = self.c_map[j][self.list[i][0]]#c_map[0-6][0]
                    node_cost_list.append(node_cost)
                max_cost = max(node_cost_list)
                #出発地点の最大コスト + パスのコストが、現状のc_mapに出祭されているコストよりも大きかったらc_mapを更新する。
                if (max_cost + self.list[i][2]) > self.c_map[self.list[i][0]][self.list[i][1]]:#c_map[0][1]
                    self.c_map[self.list[i][0]][self.list[i][1]] = self.list[i][2] + max_cost
                    break_count += 1
            if break_count == 0:
                return self.c_map

    """クリティカルパスの値を計算する=>クリティカルパスのコストを返す"""
    def max_cost(self,cost_map):
        node_cost_list = []
        for i in range(self.node):
            node_cost = cost_map[i][self.node - 1]
            node_cost_list.append(node_cost)
            #print(node_cost_list)
        max_node = max(node_cost_list)
        return max_node

    """c_map[i][node-1]から最大値とその座標を検出さかのぼって最大のルートを検索する=>[クリティカルパスのノードのリストを返す]"""
    def critical_list(self,cost_map):
        search_path = self.node-1
        critical_path = []
        while True:
            cost_list = []#ある到着地点におけるコストのリスト
            for i in range(self.node):
                cost_list.append(cost_map[i][search_path])
            #到着点の最大値を求める
            critical_num = max(cost_list)
            #座標を求める
            for j in range(self.node):
                if cost_map[j][search_path] == critical_num:
                    critical_path.append(search_path)
                    search_path = j
                    break
            if search_path == 0:
                critical_path.append(0)
                for i in range(len(critical_path)):
                    critical_path[i] = self.si_convert(critical_path[i])
                return critical_path[::-1]

if __name__ == "__main__":
    input_str = input("パスを入力してください：")
    a = Critical(input_str)
    b = a.map_edit()
    c = a.max_cost(b)
    d = a.critical_list(b)
    d_a = "->".join(d)

    print("クリティカルパス：{}   コスト：{}".format(d_a,c))