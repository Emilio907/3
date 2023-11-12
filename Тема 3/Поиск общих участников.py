# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    participants_first_set = set(participants_first_group.split(delimiter))
    participants_second_set = set(participants_second_group.split(delimiter))
    common_participants = sorted(participants_first_set.intersection(participants_second_set))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(common_participants)  # Вывод: ['Петров', 'Сидоров']
# TODO Провеьте работу функции с разделителем отличным от запятой
