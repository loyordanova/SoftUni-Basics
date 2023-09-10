yearly_fee = int(input())

shoes = yearly_fee-40/100*yearly_fee
clothes = shoes-20/100*shoes
ball = clothes/4
acc = ball/5

equipment = shoes+clothes+ball+acc

total = equipment+yearly_fee

print (total)
