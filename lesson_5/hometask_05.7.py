# Task 7 Подсмотрел, не сам решил.

import json

with open("task_7.json", "w", encoding="utf-8") as t7_json:
    with open("task_7.txt", "r", encoding="utf-8") as t7:
        firm_all = {a.split()[0]: int(a.split()[2]) - int(a.split()[3]) for a in t7}
        aver_profit = [firm_all, {f'average_profit': round(sum([int(i) for i in firm_all.values() if int(i) > 0]) /
                                                           len([int(i) for i in firm_all.values() if int(i) > 0]))}]
    json.dump(aver_profit, t7_json)