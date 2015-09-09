__author__ = 'midorikawakeita'
"""
１　１００００までのすべての素数をリストにする
２　対象の数を素因数分解し、結果をリストで返す
３　素因数を重複しているものと、そうでないもののリストに分ける
４　重複しているリストは重複を取り除き、リスト内の数字をすべてかけ合わせる
５　重複してないリストは、そのままリスト内の数字をすべてかけ合わせる。
６　成形して表示する
"""
class Root_form:
    def __init__(self,n):
        self.num = [(i + 1) for i in range(n)]

    """リストから、素数のみを抜き出し、素数のリストを返す"""
    def prime_list(self):
        prime_list = [2]
        for i in self.num[2:]:#3以上の数字でforを回す
            count = 0
            for j in range(2,i):#2~(i-1)の中でiを割り切ることができるものがあるかどうかを調べる(なければiは素数)
                if i % j == 0:
                    count +=1
                    break
            if count == 0:
                prime_list.append(i)
        return prime_list

    """対象の数を素因数分解し、結果をリストで返す"""
    def prime_factor(self,n,p_list):
        prime_factor_list = []
        while True:
            for i in p_list:
                if n % i == 0:
                    prime_factor_list.append(i)
                    n //= i
                    break
            if n == 1:
                return prime_factor_list

    """素因数分解したリストの要素と要素の個数をまとめたリストを作成する"""
    def duplicate_check(self,pf_list):
        non_duplicate_list = []
        for i in pf_list:#重複の無い新しいリストを作る
            if not i in non_duplicate_list:
                non_duplicate_list.append(i)

        num_count_list = []
        for i in non_duplicate_list:
            count = pf_list.count(i)
            num_count_list.append(count)

        return_list = []
        for i in range(len(non_duplicate_list)):
            return_list.append([non_duplicate_list[i],num_count_list[i]])

        return return_list

    """要素と要素の個数をまとめたリストを元にルートを計算"""
    def root_result(self,return_list):
        f_num = 1
        b_num = 1
        for i in range(len(return_list)):
            if return_list[i][1] % 2 == 1:
                b_num *= return_list[i][0]
            if return_list[i][1] >= 2:
                n = return_list[i][0] ** (return_list[i][1] // 2)
                f_num *= n

        return [f_num,b_num]

    def main(self):
        pl = self.prime_list()
        print("√1 -> 1",end=" , ")
        for i in self.num[1:]:
            pf = self.prime_factor(i,pl)
            dc = self.duplicate_check(pf)
            rr = self.root_result(dc)
            if rr[0] == 1:
                print("√{} -> √{}".format(i,rr[1]),end=" , ")
            elif rr[1] == 1:
                print("√{} -> {}".format(i,rr[0]),end=" , ")
            else:
                print("√{} -> {}√{}".format(i,rr[0],rr[1]),end=" , ")
            if i % 10 == 0:
                print("")


if __name__ == "__main__":
    a = Root_form(10000)
    a.main()