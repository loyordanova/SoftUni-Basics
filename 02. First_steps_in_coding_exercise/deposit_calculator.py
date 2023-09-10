amount = float(input())
period = int(input())
procent = float(input())
deposit = amount*(procent/100)
month = deposit/12
final = amount+period*month

print(final)