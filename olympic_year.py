__author__ = 'midorikawakeita'

if __name__ == "__main__":
    year = [(1896 + 4 * i) for i in range(31)]
    year.insert(3,1906)

    num = ["第{}回".format(i + 1) for i in range(30)]
    num.insert(3,"特別")

    place = "アテネ,パリ,セントルイス,アテネ,ロンドン,ストックホルム,中止,アントワープ,パリ,アムステルダム," \
            "ロサンゼルス,ベルリン,中止,中止,ロンドン,ヘルシンキ,メルボルン ストックホルム,ローマ,東京," \
            "メキシコシティー,ミュンヘン,モントリオール,モスクワ,ロサンゼルス,ソウル,バルセロナ,アトランタ," \
            "シドニー,アテネ,北京,ロンドン"
    place_list = place.split(",")

    [print("{} {}年 {}".format(num[i],year[i],place_list[i])) for i in range(31)]