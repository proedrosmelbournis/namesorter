#Panayiotis Koutos
#This code sorts names in groups alphabetically in groups


group_1_description = "Last names from A to F"
group_2_description = "Last names from G to L"
group_3_description = "Last names from M to R"
group_4_description = "Last names from S to Z"

names = []
for i in range(10):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

if names:
    group_1 = [name for name in names if name[0].upper() < 'F']
    group_2 = [name for name in names if name[0].upper() >= 'G' and name[0].upper() <= 'L']
    group_3 = [name for name in names if name[0].upper() >= 'M' and name[0].upper() <= 'R']
    group_4 = [name for name in names if name[0].upper() >= 'S']

    group_1.sort()
    group_2.sort()
    group_3.sort()
    group_4.sort()

    
    print(f"\n{group_1_description}:")
    for name in group_1:
        print(name)

    print(f"\n{group_2_description}:")
    for name in group_2:
        print(name)

    print(f"\n{group_3_description}:")
    for name in group_3:
        print(name)

    print(f"\n{group_4_description}:")
    for name in group_4:
        print(name)
