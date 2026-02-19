import urllib.request
import json

print("Github API клиент")

while True:
    print("\n1. Профиль пользователя")
    print("2. Репозитории пользователя")
    print("3. Поиск репозиториев")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        username = input("Имя пользователя: ")
        url = f"https://api.github.com/users/{username}"

        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urllib.request.urlopen(req, timeout=5)
            data = json.loads(response.read().decode('utf-8'))

            print(f"\n{data.get('name', username)}")
            print(f"Профиль: {data.get('html_url')}")
            print(f"Репозитории: {data.get('public_repos')}")
            print(f"Подписчики: {data.get('followers')}")
            print(f"Подписки: {data.get('following')}")
            print(f"Локация: {data.get('location', 'Не указана')}")

        except Exception as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        username = input("Имя пользователя: ")
        url = f"https://api.github.com/users/{username}/repos"

        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urllib.request.urlopen(req, timeout=5)
            repos = json.loads(response.read().decode('utf-8'))

            print(f"\nРепозитории {username} ({len(repos)}):")
            for repo in repos:
                print(f"\n{repo['name']}")
                print(f"  Ссылка: {repo['html_url']}")
                print(f"  Язык: {repo.get('language', 'Не указан')}")
                print(f"  Звёзд: {repo['stargazers_count']}")
                print(f"  Форков: {repo['forks_count']}")

        except Exception as e:
            print(f"Ошибка: {e}")

    elif choice == "3":
        query = input("Поиск репозиториев: ")
        url = f"https://api.github.com/search/repositories?q={query}"

        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urllib.request.urlopen(req, timeout=5)
            data = json.loads(response.read().decode('utf-8'))

            print(f"\nНайдено: {data['total_count']}")
            for repo in data['items'][:10]:  
                print(f"\n{repo['full_name']}")
                print(f"  {repo.get('description', 'Нет описания')}")
                print(f"  Язык: {repo.get('language', 'Не указан')}")
                print(f"  Звёзд: {repo['stargazers_count']}")

        except Exception as e:
            print(f"Ошибка: {e}")

    elif choice == "0":

        break
