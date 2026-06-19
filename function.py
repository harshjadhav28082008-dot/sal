# def number_pattern_for(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# n = int(input("Enter the number of rows: "))
# number_pattern_for(n)


def star_pattern_for(rows):
    for i in range(1, rows + 1):
        print("* " * i)

n = int(input("Enter the number of rows: "))
star_pattern_for(n)