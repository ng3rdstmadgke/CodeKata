__author__ = 'midorikawakeita'
import random

if __name__ == "__main__":
    word_list = [chr(12354 + i) for i in range(83)]
    name_list = ["".join([random.choice(word_list) for i in range(2)]) for i in range(50)]
    [print(name_list[i],end=" , ") for i in range(50)]
