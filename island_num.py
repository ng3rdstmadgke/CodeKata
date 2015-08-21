__author__ = 'midorikawakeita'

"""
5 6 ##...#|#.#...|#..###|.....#|.###..

5 6
##...#
#.#...
#..##.
...#..
.##...
"""
#与えられた標準入力をスペース区切りでリスト化しそれぞれheight,width,islandに代入する。
#islandをheight×widthの行列形式のリストにする。
#島かどうかの判断
    #自分自身が「#」でかつ、自分自身の上、右、下が「.」であったら島と判断
    #ただし1列に関しては、右と下のみでOK、最終列に関して右と上のみでOK
    #行末であったら、上と下のみでOK

if __name__=="__main__":
    input_text=input("地図を入力してください：")
    input_list=input_text.split(" ")
    height=int(input_list[0])
    width=int(input_list[1])
    my_map=input_list[2]
    print(height)
    print(type(height))
    print(width)
    print(type(width))
    print(my_map)
    print(type(my_map))
