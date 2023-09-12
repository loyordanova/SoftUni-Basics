import phonenumbers

number = +359876763444
ch_number = phonenumbers.parse(number, "CH")
print(ch_number)

ch_number = phonenumbers.parse(number)
time_zone = timezone.time_zone_for_number()
