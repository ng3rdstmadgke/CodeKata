__author__ = 'midorikawakeita'
"""
入力例 20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  出力例 0
入力例 12 10 10 10 10 10 10 10 10 10 10 10 10 出力例 300
入力例 19 6 2 0 3 5 5 0 8 10 1 9 3 6 6 4 10 5 5 3 出力例 124
入力例 21 1 9 1 9 1 9 1 0 1 9 1 9 1 9 0 1 1 9 1 9 4 出力例 92
入力例 20 1 9 2 8 3 7 4 6 10 0 0 6 4 7 3 8 2 9 1 2 出力例 135
入力例 20 1 9 2 8 3 7 4 6 10 0 0 6 4 7 3 8 2 7 1 出力例
*+*+ルール+*+*
１ゲーム１０フレーム構成
１フレームで倒せるピンは１０本まで
１フレームに２回ボールを投げることができる
ストライクの場合、次の２投の合計＋１０を加算する
スペアの場合、次の１投＋１０を加算する
それ以外の場合は、１フレーム中で倒した本数を単純に数える
１０フレーム目は、スペアかストライクを出すと３投目が投げられる。
１０フレーム目の得点は倒したピンの数をそのまま加算
*+*+*+*+*+*+*
入力値を、投数(int)と倒したピンの数(list)に分ける
"10"の次に"0"を挿入
リストを２個ずつのフレームに分割。１０フレーム目のみ１フレーム乗リストに数字を３つ入れる
得点を計算する関数
    通常:i,i+1,i+2の３つを引数に取る
    第9フレーム：９フレームと１０フレームを引数に取る
    第１０フレーム：１０フレームを引数に取る
main関数１
    得点の合計を出力
main関数２
    フレームごとの得点を表示する
"""
class My_Bowling:
    """投球回数とフレームごとのリストを作成"""
    def __init__(self,input):
        a = input.split(" ")
        self.throw = int(a[0])
        self.raw_score = []
        for i in a[1:]:
            self.raw_score.append(int(i))

        self.ps_score = []
        cnt = 0
        flame = 0
        while True:
            if (self.raw_score[cnt] != 10) and (flame < 9):
                self.ps_score.append([self.raw_score[cnt],self.raw_score[cnt + 1]])
                cnt += 2
                flame += 1
            elif (self.raw_score[cnt] == 10) and (flame < 9):
                self.ps_score.append([self.raw_score[cnt],0])
                cnt += 1
                flame += 1
            elif flame == 9:
                if self.raw_score[cnt] + self.raw_score[cnt + 1] >= 10:
                    self.ps_score.append([self.raw_score[cnt],self.raw_score[cnt + 1],self.raw_score[cnt + 2]])
                    flame += 1
                elif self.raw_score[cnt] + self.raw_score[cnt + 1] < 10:
                    self.ps_score.append([self.raw_score[cnt],self.raw_score[cnt + 1],0])
                    flame += 1
            if flame == 10:
                break

    """1~8投目までのスコア計算"""
    def normal_score(self,one,two,three):
        if one[0] == 10:#ストライクの時
            if two[0] == 10:#ダブルの場合
                return 20 + three[0]
            else:#２フレーム目通常
                return 10 + two[0] + two[1]
        elif one[0] + one[1] == 10:#1フレーム目スペアの場合
            return 10 + two[0]
        else:#通常
            return one[0] + one[1]

    """9投目のスコア計算"""
    def nine_score(self,nine,ten):
        if nine[0] == 10:#９フレーム目ストライク
            return 10 + ten[0] + ten[1]
        elif nine[0] + nine[1] == 10:#９フレーム目スペア
            return 10 + ten[0]
        else:#９フレーム目通常
            return nine[0] + nine[1]

    """10投目のスコア計算"""
    def ten_score(self,ten):
        return ten[0] + ten[1] + ten[2]

    """得点の合計のみを出す"""
    def main_1(self):
        score = 0
        for i in range(10):
            if i < 8:
                a = self.normal_score(self.ps_score[i],self.ps_score[i + 1],self.ps_score[i + 2])
                score += a
            elif i == 8:
                b = self.nine_score(self.ps_score[i],self.ps_score[i + 1])
                score += b
            elif i == 9:
                c = self.ten_score(self.ps_score[i])
                score += c
        return score

    """フレームごとの得点を出す"""
    def main_2(self):
        score_list = []
        score = 0
        for i in range(10):
            if i < 8:
                a = self.normal_score(self.ps_score[i],self.ps_score[i + 1],self.ps_score[i + 2])
                score += a
                score_list.append(score)
            elif i == 8:
                b = self.nine_score(self.ps_score[i],self.ps_score[i + 1])
                score += b
                score_list.append(score)
            elif i == 9:
                c = self.ten_score(self.ps_score[i])
                score += c
                score_list.append(score)
        return score_list


if __name__ == "__main__":

    a = My_Bowling("19 6 2 0 3 5 5 0 8 10 1 9 3 6 6 4 10 5 5 3")
    b = a.main_1()
    c = a.main_2()
    print(b)
    [print(str(i),end=" ") for i in c]