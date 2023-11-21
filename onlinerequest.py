import requests

def get_online_currencies():
    # Здесь задается ключ API. Ключ берется непосредственно в самом API
    api_key = 'fca_live_hoLsuBp9C4Vr9uSmhr7JfXyJelREmwLberE5IBTv'

    # URL в котором передаются параметры.
    host = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies=EUR%2CUSD%2CRUB'

    # Отправляется GET-запрос к API.
    response = requests.get(host)

    # Проверяется статус ответа. Если статус 200 (ОК), то извлекаются данные в формате JSON.
    if response.status_code == 200:
        data = response.json().get("data")
        return data
    else:
        # Если статус ответа не 200, выводится сообщение об ошибке и возвращается None.
        print(f"Не удалось загрузить курсы валют. Статус код: {response.status_code}")
        return None

# Вызывается функция для получения данных о курсах валют.
currencies_data = get_online_currencies()

# Если данные успешно получены, они выводятся, в противном случае используются стандартные значения.
if currencies_data:
    print(currencies_data)
else:
    print("Используются стандартные значения.")
    currencies_data = {
        "EUR": 1.0,
        "USD": 1.0,
        "RUB": 1.0
    }

# Выводится результат.
print(currencies_data)
