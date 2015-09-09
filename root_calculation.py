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
        prime_factor_list = [n]
        while True:
            for i in p_list:
                if n % i == 0:
                    prime_factor_list.append(i)
                    n //= i
                    break
            if n == 1:
                return prime_factor_list

    """素因数リストの中に重複している数字があるかどうかを判定する"""
    def duplicate_check(self,pf_list):
        s = set()
        duplicate_num = []
        for i in pf_list[1:]:
            if i in s:
                duplicate_num.append(i)
            s.add(i)
        if duplicate_num:
            pass



        else:
            return [pf_list[1]]

