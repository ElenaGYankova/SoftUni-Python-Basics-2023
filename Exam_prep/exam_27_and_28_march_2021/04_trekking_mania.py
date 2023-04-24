groups = int(input())
musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k_2_count = 0
everest_count = 0
all_people_in_groups = 0


for group in range(groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala_count += people_in_group
        all_people_in_groups += people_in_group
    elif people_in_group <= 12:
        montblanc_count += people_in_group
        all_people_in_groups += people_in_group
    elif people_in_group <= 25:
        kilimanjaro_count += people_in_group
        all_people_in_groups += people_in_group
    elif people_in_group <= 40:
        k_2_count += people_in_group
        all_people_in_groups += people_in_group
    else:
        everest_count += people_in_group
        all_people_in_groups += people_in_group

musala_percent = musala_count / all_people_in_groups * 100
montblanc_percent = montblanc_count / all_people_in_groups * 100
kilimanjaro_percent = kilimanjaro_count / all_people_in_groups * 100
k_2_percent = k_2_count / all_people_in_groups * 100
everest_percent = everest_count / all_people_in_groups * 100

print(f'{musala_percent:.2f}%')
print(f'{montblanc_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k_2_percent:.2f}%')
print(f'{everest_percent:.2f}%')