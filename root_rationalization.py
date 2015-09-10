__author__ = 'midorikawakeita'
"""
１分母分子を初期化メソッドの引数にとる
２分母を因数分解し「素因数リスト」を作成
３「素因数リスト」の要素と要素の個数をまとめた「素因数・個数リスト」を作成
４「素因数・個数リスト」の中で要素数が奇数の数字を抜き出し、「ルート内数字リスト」を作成
５「素因数・個数リスト」の中で要素数が奇数の数字の要素数に+1する
６ルートをわかりやすく計算
７分子を因数分解「素因数リスト」を作成
８分子の「素因数リスト」に分母の「ルート内数字リスト」追加
９分子の素因数と、その個数をまとめた「素因数・個数リスト」を作成
１０ルートをわかりやすく計算
１１分子と分母の整数部分を約分
１３求めた積を分母、分子それぞれの整数部分に代入する
１４成形して出力

追加する関数
１分母の「素因数・個数リスト」の中で要素数が奇数の数字を抜き出し、「ルート内数字リスト」を作成
２分母の「素因数・個数リスト」の中で要素数が奇数の数字の要素数に＋１をする関数
"""


class Rationalization:
    """1~100までの素数のリストを返す"""

    def __init__(self):
        self.prime_list = [2]
        for i in [n for n in range(3, 101)]:  # 3以上の数字でforを回す
            count = 0
            for j in range(2, i):  # 2~(i-1)の中でiを割り切ることができるものがあるかどうかを調べる(なければiは素数)
                if i % j == 0:
                    count += 1
                    break
            if count == 0:
                self.prime_list.append(i)

    """与えられた数の「素因数リスト」を作成"""

    def prime_factor(self, n):
        pf_list = []
        while True:
            for i in self.prime_list:
                if n % i == 0:
                    pf_list.append(i)
                    n //= i
                    break
            if n == 1:
                return pf_list

    """「素因数リスト」の要素と要素の個数をまとめ、「素因数・個数リスト」を作成する"""

    def prime_and_number(self, pf_list):
        non_duplicate_list = []
        for i in pf_list:  # 重複の無い新しいリストを作る
            if not i in non_duplicate_list:
                non_duplicate_list.append(i)

        num_count_list = []
        for i in non_duplicate_list:
            count = pf_list.count(i)
            num_count_list.append(count)

        pf_num_list = []
        for i in range(len(non_duplicate_list)):
            pf_num_list.append([non_duplicate_list[i], num_count_list[i]])

        return pf_num_list

    """「素因数・個数リスト」の中で要素数が奇数の数字を抜き出し、「ルート内数字リスト」を作成"""

    def root_num(self, pf_num_list):
        root_list = []
        for i in pf_num_list:
            if i[1] % 2 == 1:
                root_list.append(i[0])
        return root_list

    """「素因数・個数リスト」の中で要素数が奇数の数字の要素数に＋１をする関数"""

    def num_plus(self, pf_num_list):
        for i in range(len(pf_num_list)):
            if pf_num_list[i][1] % 2 == 1:
                pf_num_list[i][1] = pf_num_list[i][1] + 1
        return pf_num_list

    """「素因数・個数リスト」を元にルートをわかりやすく計算"""

    def root_result(self, pf_num_list):
        f_num = 1
        b_num = 1
        for i in range(len(pf_num_list)):
            if pf_num_list[i][1] % 2 == 1:
                b_num *= pf_num_list[i][0]
            if pf_num_list[i][1] >= 2:
                n = pf_num_list[i][0] ** (pf_num_list[i][1] // 2)
                f_num *= n

        return [f_num, b_num]

    """２つの数字を最大公約数で割った数字を返す"""

    def reduction(self, nu, de):
        while True:
            count = 0
            for i in self.prime_list:
                if (nu % i == 0) and (de % i == 0):
                    nu //= i
                    de //= i
                    count += 1
                    break
            if count == 0:
                return [nu, de]

    """main"""

    def main_act(self, nu, de):
        de_pf_list = self.prime_factor(de)  # 分母の「素因数リスト」
        de_pf_num_list = self.prime_and_number(de_pf_list)  # 分母の「素因数・個数リスト」
        root_num_list = self.root_num(de_pf_num_list)  # 分母の「ルート内数字リスト」を作成
        de_pf_num_list_plus = self.num_plus(de_pf_num_list)  # 「素因数・個数リスト」の中で要素数が奇数の数字の要素数に+1する
        de_root_result = self.root_result(de_pf_num_list_plus)  # ルートをわかりやすく計算

        if nu == 1:
            nu_root_result = [1,de_root_result[0]]
        else:
            nu_pf_list = self.prime_factor(nu)  # 分子の「素因数リスト」
            nu_pf_list += root_num_list  # 分子の「素因数リスト」に分母の「ルート内数字リスト」を足す
            nu_pf_num_list = self.prime_and_number(nu_pf_list)  # 分子の「素因数・個数リスト」
            nu_root_result = self.root_result(nu_pf_num_list)  # 分子のルートをわかりやすく計算

        int_list = self.reduction(nu_root_result[0], de_root_result[0])
        nu_root_result[0] = int_list[0]
        de_root_result[0] = int_list[1]

        return nu_root_result[0],nu_root_result[1], de_root_result[0],de_root_result[1]

if __name__ == "__main__":
    a=Rationalization()
    for nu in range(1,101):
        for de in range(2,101):
            ni,nr,di,dr = a.main_act(nu,de)
            if nr == 1:
                x = "{}".format(ni)
            elif ni == 1:
                x = "√{}".format(nr)
            else:
                x = "{}√{}".format(ni,nr)

            if (ni == di) and (nr == dr):
                print("√{}/√{}=>1".format(nu,de,x,di),end = " , ")
            else:
                print("√{}/√{}=>{}/{}".format(nu,de,x,di),end = " , ")
            if de % 10 == 0:
                print("")