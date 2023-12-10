numbers = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for number in numbers:
    if numbers.count(number) > 1:
        continue
    else:
        print(number, end=' ')

# Вариант 2
# already_checked = []
# for i in range(len(numbers)):
#     if numbers[i] not in already_checked:
#         if numbers[i] not in numbers[i + 1: len(numbers)]:
#             print(numbers[i], end=' ')
#         else:
#             already_checked.append(numbers[i])



