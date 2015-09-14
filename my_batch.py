__author__ = 'midorikawakeita'
"""
123456789
N**ON*O*O*
*ON***N*N
NONONONON
NNONO*ONON
文字列が偶数か奇数かを判断
偶数だった場合は文字列を２分する
奇数だった場合は、真ん中の文字列を残し、文字列を２分する

後ろの文字列を反転しする。以降、前側の文字列をa、後側の文字列をbとする

aとbの文字列を照合する
    aがＯ
        bがＯ：そのまま
        bがＮ：終了
        bが*：bをＯに変換
    aがＮ
        bがＯ：終了
        bがＮ：そのまま
        bが*：bをＮに変換
    aが*
        bがＯ：aをＯに変換
        bがＮ：aをＮに変換
        bが*：aとbをＮに変換
後半を反転して出力
"""
class Batch_form:
    def __init__(self,input):
        self.b_list = list(input)
        self.length = len(self.b_list)
        if self.length % 2 == 0:
            self.forward = self.b_list[:self.length // 2]
            self.backward = self.b_list[self.length // 2:]
        else:
            self.forward = self.b_list[:self.length // 2]
            self.backward = self.b_list[self.length // 2 + 1:]
            self.center = [self.b_list[self.length // 2]]

    def make_batch(self):
        fore = self.forward
        back = self.backward[::-1]
        cost = 0
        for i in range(len(fore)):
            if fore[i] == "O":
                if back[i] == "*":
                    back[i] = "O"
                    cost += 15
                elif back[i] == "N":
                    return self.b_list,-1
            elif fore[i] == "N":
                if back[i] == "O":
                    return self.b_list,-1
                elif back[i] == "*":
                    back[i] = "N"
                    cost +=10
            else:
                if back[i] == "O":
                    fore[i] = "O"
                    cost += 15
                elif back[i] == "N":
                    fore[i] = "N"
                    cost +=10
                else:
                    fore[i] = "N"
                    back[i] = "N"
                    cost += 20
        if self.length % 2 == 0:
            whole_list = fore + back[::-1]
            return whole_list,cost
        else:
            if self.center[0] == "*":
                self.center[0] = "N"
                cost += 10
            whole_list = fore + self.center + back[::-1]
            return whole_list,cost

if __name__ == "__main__":
    input_str = input("文字列を入力:")
    a=Batch_form(input_str)
    list_item,cost = a.make_batch()
    print(["".join(list_item),cost])



