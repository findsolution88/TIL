lotto_num = [1,2,3,4,5,6]
bonus_num = 7
my_num = set([2,3,4,5,6,7])
lotto_bonus_num = set(lotto_num.append(bonus_num))
lotto_num = set(lotto_num)

rank=''
if my_num == lotto_num :
    rank='1등'
elif len(my_num.intersection(lotto_bonus_num))==6 :
    rank='2등'

print(rank)