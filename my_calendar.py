__author__ = 'midorikawa.keita'
import datetime
# -*- coding: utf-8 -*-
#入力年月の日数を求める関数
def days(year,month):
    if month==12:
        date_1=datetime.date(year,month,1)
        date_2=datetime.date(year+1,1,1)
    else:
        date_1=datetime.date(year,month,1)
        date_2=datetime.date(year,month+1,1)
    month_days=date_2-date_1
    return month_days.days

#カレンダーリストを作る関数
def calendar_list(days,weekday):
    a=[]
    for i in range(1,days+1):
        if i<10:
            a.append(" "+str(i))
        else:
            a.append(str(i))
    b=[]
    for i in range(weekday):
        b.append("  ")
    b.extend(a)
    for i in range(42-len(b)):
        b.append("  ")
    return b

if __name__=="__main__":
    #求めたいカレンダーの年と月を入力
    year=int(input("西暦を入力してください："))
    month=int(input("月を入力してください："))
    date=datetime.date(year,month,1)

    #入力年月の日数を計算する(関数で作成)
    days=days(year,month)
    #print(days)

    #入力年月の1日の曜日を求める
    weekday=date.weekday()
    #print(weekday)

    #カレンダーリストを作成(関数で作成)
    calendar_list=calendar_list(days,weekday)
    #print(calendar_list)

    #カレンダーの整形
    print("\n{}年{}月のカレンダー".format(year,month))
    print("月 火 水 木 金 土 日")
    calendar=[]
    for i in range(6):
        calendar_str = ""
        for j in calendar_list[7*i:7*(i+1)]:
            calendar_str += j + " "
        #カレンダーの表示
        print(calendar_str)
