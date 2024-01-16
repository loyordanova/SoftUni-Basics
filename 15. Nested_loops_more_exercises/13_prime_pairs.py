start_first_pair = int(input())
start_second_pair = int(input())
diff_start_finish_first_pair = int(input())
diff_start_finish_second_pair = int(input())

diff_start_finish_first_pair += start_first_pair
diff_start_finish_second_pair += start_second_pair
for a in range(start_first_pair, diff_start_finish_first_pair + 1):
    count1 = 0
    for i in range(2, a):
        if a % i == 0:
            count1 += 1

    if count1 == 0:
        for b in range(start_second_pair, diff_start_finish_second_pair + 1):
            count2 = 0
            for x in range(2, b):
                if b % x == 0:
                    count2 += 1
            if count2 == 0:
                print(f'{a}{b}')