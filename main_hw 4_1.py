#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
from HW_les4 import my_mod_hw4_1

try:
    file, output, rate, prize = sys.argv
except ValueError:
    print("Ошибка")
    exit()

print(my_mod_hw4_1.salary(int(output), int(rate), int(prize)))
