import urllib.request
import urllib.error

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

print("Проверка доступности сайтов")

for url in urls:
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()

            if 200 <= status_code < 300:
                availability = "доступен"
            elif status_code == 401 or status_code == 403:
                availability = "вход запрещен"
            elif status_code == 404:
                availability = "не найден"
            elif 500 <= status_code < 600:
                availability = "ошибка сервера"
            else:
                availability = "не доступен"

            print(f"{url} – {availability} – {status_code}")

    except urllib.error.HTTPError as e:
        status_code = e.code
        if status_code == 401 or status_code == 403:
            availability = "вход запрещен"
        elif status_code == 404:
            availability = "не найден"
        elif 500 <= status_code < 600:
            availability = "ошибка сервера"
        else:
            availability = "не доступен"
        print(f"{url} – {availability} – {status_code}")

    except urllib.error.URLError:
        print(f"{url} – не доступен – N/A")
    except Exception:
        print(f"{url} – ошибка – N/A")

print("Проверка завершена")