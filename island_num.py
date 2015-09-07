__author__ = 'midorikawakeita'

"""
5 6 .#...####...#.####.....#.###..

5 6
.#...#
###...
#.####
.....#
.###..


10 10 .#...####...#.####...###.#...........##..#...####.###..##.#.#.#..##.#.#.##.##.#..#.........#...####.

.#...####.
..#.####..
.###.#....
.......##.
.#...####.
###..##.#.
#.#..##.#.
#.##.##.#.
.#........
.#...####.

準備１
１与えられた入力を行列にする

処理１
１左上からひとつずつ文字を読み込む
２読み込んだ文字が＃だったらカウントし＋に変換、処理２に移行

処理２
１左上からひとつずつ文字を読み込む
２＋を読み込んだら、その上下左右を読み込み＃なら＋に変換する
３＋の周りの＃がなくなるまで繰り返す
３処理３に移行

処理3
１左上からひとつずつ文字を読み込み
２読み込んだ文字が＋だったら．に変換
３処理１に戻る
"""

class my_island:

    """初期化メソッドheight(int),width(int),map(str)(list)を作成"""
    def __init__(self, input):
        self._input_list = input.split(" ")
        self.height = int(self._input_list[0])
        self.width = int(self._input_list[1])
        self.map_str = self._input_list[2]
        self.map_list=[]
        for i in range(len(self.map_str) // self.width):
            map_l=list(self.map_str[self.width*i:self.width*(i+1)])
            self.map_list.append(map_l)


    """処理１：リストを順に読み込み「#」を「+」に変換。変換後のリストを戻す"""
    def is_rec(self,map_list):
        for i in range(self.height):
            for j in range(self.width):
                masu = map_list[i][j]
                if masu == "#" :
                    map_list[i][j] = "+"
                    return map_list
        return 1

    """処理２：処理１で変換したリストを引数にとる。左上から順に読み込み、＋を読み込んだら左右上下の"#"を"+"に変換"""
    def left(self,map_list):
        while True:
            break_count=0
            for i in range(self.height):
                for j in range(self.width):
                    masu = map_list[i][j]
                    if masu == "+":
                        if j != (self.width - 1):
                            if map_list[i][j + 1] == "#":
                                map_list[i][j + 1] = "+"
                                break_count += 1
                        if i != self.height-1:
                            if map_list[i + 1][j] == "#":
                                map_list[i + 1][j] = "+"
                                break_count += 1
                        if j != 0:
                            if map_list[i][j - 1] == "#":
                                map_list[i][j - 1] = "+"
                                break_count += 1
                        if i != 0:
                            if map_list[i - 1][j] == "#":
                                map_list[i - 1][j] = "+"
                                break_count += 1
            if break_count == 0:
                break
        return map_list


    """処理3：処理３で変換したリストを引数にとる。左上から順に読み込み、＋を読み込んだら.に変換"""
    def is_del(self,map_list):
        for i in range(self.height):
            for j in range(self.width):
                if map_list[i][j] == "+":
                    map_list[i][j] = "."
        return map_list

    """処理１〜処理3までを組み合わせて、島の数をカウントする"""
    def main(self):
        count = 0
        map = self.map_list
        while True:
            map_a = self.is_rec(map)
            if map_a == 1:
                break
            map_b = self.left(map_a)
            map = self.is_del(map_b)
            count += 1
        return count





if __name__ == "__main__":
    island_init = my_island("10 10 .#...####...#.####...###.#...........##..#...####.###..##.#.#.#..##.#.#.##.##.#..#.........#...####.")
    num = island_init.main()
    print("島の数：{}".format(num))

