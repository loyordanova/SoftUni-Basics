juniors = int(input())
seniors = int(input())
trace_type = input()

tax_collected = 0

if trace_type == "trail":
    tax_collected += juniors * 5.50
    tax_collected += seniors * 7

elif trace_type == 'cross-country':
    tax_collected += juniors * 8
    tax_collected += seniors * 9.50
    if juniors + seniors >= 50:
        tax_collected = tax_collected - tax_collected * 0.25

elif trace_type == "downhill":
    tax_collected += juniors * 12.25
    tax_collected += seniors * 13.75

elif trace_type == 'road':
    tax_collected += juniors * 20
    tax_collected += seniors * 21.50

tax_collected = tax_collected - tax_collected * 0.05

print(f'{tax_collected:.2f}')
