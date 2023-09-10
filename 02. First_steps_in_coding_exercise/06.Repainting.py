nailon = 1.50
paint = 14.50
razreditel = 5

neobhodim_nailon = int(input())
neobhodimo_kolichestvo_boq = int(input())
kolichestvo_razreditel = int(input())
chasove = int(input())

suma_za_nailona = (neobhodim_nailon+2)*nailon
suma_za_boq = (neobhodimo_kolichestvo_boq+10/100*neobhodimo_kolichestvo_boq)*paint
suma_razreditel = kolichestvo_razreditel*razreditel
suma_za_torbi = 0.40

total = suma_za_nailona+suma_za_boq+suma_razreditel+suma_za_torbi
rabota = (30/100*total)*chasove
print(total+rabota)
