class Solution(object):
    def addDigits(self, num):
        while num > 9:                      # dokud nebude číslo jednociferné
            last_digit = num % 10           # zjistíme poslední cifru
            num -= last_digit               # odečteme poslední cifru  
            num = num / 10                  # poté zmenšíme o 1 desetinou čárku
            num += last_digit               # sečteme novou cifru s minulou, poté opakujeme pokud je výsledek větší než 9 (čili dvojciferné), nebo vracíme jednociferný součet číslic
        return num
            