__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-
import datetime
def constellation(month,day):
    date=datetime.date(2000,month,day)
    my_cons="牡羊座,牡牛座,双子座,蟹座,獅子座,乙女座,天秤座,さそり座,射手座,山羊座,水瓶座,魚座".split(",")
    #print(my_cons)
    if date>=datetime.date(2000,3,21) and date<=datetime.date(2000,4,20):
        return my_cons[0]
    elif date>=datetime.date(2000,4,21) and date<=datetime.date(2000,5,20):
        return my_cons[1]
    elif date>=datetime.date(2000,5,21) and date<=datetime.date(2000,6,21):
        return my_cons[2]
    elif date>=datetime.date(2000,6,22) and date<=datetime.date(2000,7,23):
        return my_cons[3]
    elif date>=datetime.date(2000,7,24) and date<=datetime.date(2000,8,23):
        return my_cons[4]
    elif date>=datetime.date(2000,8,24) and date<=datetime.date(2000,9,23):
        return my_cons[5]
    elif date>=datetime.date(2000,9,24) and date<=datetime.date(2000,10,23):
        return my_cons[6]
    elif date>=datetime.date(2000,10,24) and date<=datetime.date(2000,11,22):
        return my_cons[7]
    elif date>=datetime.date(2000,11,23) and date<=datetime.date(2000,12,22):
        return my_cons[8]
    elif (date>=datetime.date(2000,12,23) and date<=datetime.date(2000,12,31)) or (date>=datetime.date(2000,1,1) and date<=datetime.date(2000,1,20)):
        return my_cons[9]
    elif date>=datetime.date(2000,1,21) and date<=datetime.date(2000,2,19):
        return my_cons[10]
    elif date>=datetime.date(2000,2,20) and date<=datetime.date(2000,3,20):
        return my_cons[11]


if __name__=="__main__":
    month=int(input("月を入力してください："))
    day=int(input("日にちを入力してください"))
    print(constellation(month,day))

#月日を入力

