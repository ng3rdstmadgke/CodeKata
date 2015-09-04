__author__ = 'midorikawakeita'

"""
5 6 ##...##.#...#..###.....#.###..

5 6
##...#
#.#...
##.##.
...##.
.##...
.#..##
.....#
"""
"""
準備１
１与えられた入力を行列にする

処理１
１左上からひとつずつ文字を読み込む
２読み込んだ文字が＃だったらカウントし＋に変換、処理２に移行

処理２
１左上からひとつずつ文字を読み込む
２＋を読み込んだら、その上下左右を読み込み＃なら＋に変換する
３処理３に移行

処理３
１右下からひとつずつ文字を読み込む
２＋を読み込んだら、その上下左右を読み込み＃なら＋に変換する
３処理４に移行

処理４
１左上からひとつずつ文字を読み込み
２読み込んだ文字が＋だったら．に変換
３処理１に戻る
"""
# 与えられた標準入力をスペース区切りでリスト化しそれぞれheight,width,islandに代入する。
# islandをheight×widthの行列形式のリストにする。
# 「#」に出会ったら、隣接している島を「+」に変換し
class my_island:
    # 初期化メソッドheight(int),width(int),map(str)(list)を作成
    def __init__(self, input):
        self._input_list = input.split(" ")
        self.height = int(self._input_list[0])
        self.width = int(self._input_list[1])
        self.map_str = self._input_list[2]
        self.map_list=[]
        for i in range(len(self.map_str) // self.width):
            map_l=list(self.map_str[self.width*i:self.width*(i+1)])
            self.map_list.append(map_l)













if __name__ == "__main__":
    my_str = "ABCDEFGHIJKL"
    ll = []
    for i in range(len(my_str) // 3):
        st=i * 3
        ed=(i + 1) * 3
        ll.append(my_str[st:ed])
    my_list = list(my_str)
    my_list[3] = 5
    print(my_str)
    print(my_list)
    print(ll)
