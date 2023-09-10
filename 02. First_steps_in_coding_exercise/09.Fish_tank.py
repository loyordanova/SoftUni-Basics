daljina = int(input())
shirochina = int(input())
visochina = int(input())
procent = float(input())

obem = daljina*shirochina*visochina
litri = obem/1000
zaeto_prostranstvo = procent/100

total = litri*(1-zaeto_prostranstvo)

print(total)
