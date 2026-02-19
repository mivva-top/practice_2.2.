import json
import os
import urllib.request

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
SAVE_FILE = "save.json"

if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r") as f:
        groups = json.load(f)
else:
    groups = {}

print("Мониторинг валют")

while True:
    print("\n1. Все валюты")
    print("2. Валюта по коду")
    print("3. Создать группу и добавить валюты")
    print("4. Мои группы")
    print("5. Добавить валюту в существующую группу")
    print("6. Удалить валюту из группы")
    print("0. Выход")

    c = input("Выбор: ")

    if c == "1":
        try:
            response = urllib.request.urlopen(URL, timeout=5)
            data = json.loads(response.read().decode('utf-8'))
            print("\nДоступные валюты:")
            for code, val in data["Valute"].items():
                print(f"{code}: {val['Name']} - {val['Value']} руб.")
        except:
            print("Ошибка загрузки")

    elif c == "2":
        code = input("Код валюты: ").upper()
        try:
            response = urllib.request.urlopen(URL, timeout=5)
            data = json.loads(response.read().decode('utf-8'))
            if code in data["Valute"]:
                val = data["Valute"][code]
                print(f"\n{code}: {val['Name']}")
                print(f"Курс: {val['Value']} руб.")
                print(f"Номинал: {val['Nominal']}")
            else:
                print("Не найдено")
        except:
            print("Ошибка")

    elif c == "3":
        name = input("Название группы: ")

        if name in groups:
            print("Группа уже существует")
        else:
            groups[name] = []

            print("\nДобавить валюты в группу. Оставьте пустым для завершения.")

            while True:
                code = input("Код валюты для добавления (или Enter для завершения): ").upper()

                if not code:
                    break

                try:
                    response = urllib.request.urlopen(URL, timeout=3)
                    data = json.loads(response.read().decode('utf-8'))

                    if code in data["Valute"]:
                        if code not in groups[name]:
                            groups[name].append(code)
                            print(f"Добавлено: {code}")
                        else:
                            print(f"{code} уже есть в группе")
                    else:
                        print(f"{code} не найден")

                except:
                    print("Ошибка проверки валюты")

            with open(SAVE_FILE, "w") as f:
                json.dump(groups, f, indent=2)

            print(f"\nГруппа '{name}' создана")
            if groups[name]:
                print(f"Добавлено валют: {len(groups[name])}")
            else:
                print("Группа пустая")

    elif c == "4":
        if not groups:
            print("Нет созданных групп")
        else:
            print("\nВаши группы:")
            for name, codes in groups.items():
                print(f"\n{name}:")
                if codes:
                    try:
                        response = urllib.request.urlopen(URL, timeout=3)
                        data = json.loads(response.read().decode('utf-8'))

                        for code in codes:
                            if code in data["Valute"]:
                                val = data["Valute"][code]
                                print(f"  {code}: {val['Value']} руб.")
                            else:
                                print(f"  {code}: не найден")
                    except:
                        print(f"  {', '.join(codes)}")
                else:
                    print("  (пусто)")

    elif c == "5":
        if not groups:
            print("Нет созданных групп")
        else:
            print("\nВыберите группу:")
            group_list = list(groups.keys())
            for i, group_name in enumerate(group_list, 1):
                print(f"{i}. {group_name}")

            try:
                choice = int(input("Номер группы: "))
                if 1 <= choice <= len(group_list):
                    group_name = group_list[choice - 1]

                    code = input("Код валюты для добавления: ").upper()

                    try:
                        response = urllib.request.urlopen(URL, timeout=3)
                        data = json.loads(response.read().decode('utf-8'))

                        if code in data["Valute"]:
                            if code not in groups[group_name]:
                                groups[group_name].append(code)
                                with open(SAVE_FILE, "w") as f:
                                    json.dump(groups, f, indent=2)
                                print(f"Добавлено: {code}")
                            else:
                                print(f"{code} уже есть в группе")
                        else:
                            print(f"{code} не найден")

                    except:
                        print("Ошибка проверки валюты")
                else:
                    print("Неверный номер")
            except:
                print("Неверный ввод")

    elif c == "6":
        if not groups:
            print("Нет созданных групп")
        else:
            print("\nВыберите группу:")
            group_list = list(groups.keys())
            for i, group_name in enumerate(group_list, 1):
                print(f"{i}. {group_name}")

            try:
                choice = int(input("Номер группы: "))
                if 1 <= choice <= len(group_list):
                    group_name = group_list[choice - 1]

                    if not groups[group_name]:
                        print(f"Группа '{group_name}' пуста")
                    else:
                        print(f"\nВалюты в группе '{group_name}':")
                        for i, code in enumerate(groups[group_name], 1):
                            print(f"{i}. {code}")

                        try:
                            code_choice = int(input("Номер валюты для удаления: "))
                            if 1 <= code_choice <= len(groups[group_name]):
                                removed = groups[group_name].pop(code_choice - 1)
                                with open(SAVE_FILE, "w") as f:
                                    json.dump(groups, f, indent=2)
                                print(f"Удалено: {removed}")
                            else:
                                print("Неверный номер")
                        except:
                            print("Неверный ввод")
                else:
                    print("Неверный номер")
            except:
                print("Неверный ввод")

    elif c == "0":
        print("Выход")
        break
