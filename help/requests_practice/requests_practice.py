import requests
from requests.exceptions import HTTPError

"""" 
Метод GET указывает на то, что происходит попытка извлечь данные из определенного ресурса. 
Для того, чтобы выполнить запрос GET, используется requests.get().
"""

responce = requests.get('https://api.github.com')

print(responce.status_code)  # получаем ответ от сервера

print(responce)

""""Проверяем ответ от сервера если 200 все хорошо,404 не найдено"""
if responce.status_code == 200:
    print('okay')
elif responce.status_code == 404:
    print('not okay')

# упростим

if responce:
    print('okay')
else:
    print('not okay')

# обработка ошибок

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        responce = requests.get(url)
        responce.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

# получаем данные в байтах
responce = requests.get('https://api.github.com')
byte_result = responce.content
print(byte_result)

# получаем данные в кодировке utf-8
responce = requests.get('https://api.github.com')
responce.encoding = 'utf-8'
text_result = responce.text
# преобразование полученной строки в json(словарь)
json_result = responce.json()
print(json_result)
print(text_result)
print(json_result.get("user_url"))

# Http заголовки

responce = requests.get('https://api.github.com')
headers = responce.headers
print(headers)

print(responce.headers['Content-Type'])

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()

repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# просмотр нового массива `text-matches` с предоставленными данными
# о поиске в пределах результатов
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

print('-' * 100)

print(requests.post('https://httpbin.org/post', data={'key': 'value'}))
print(requests.put('https://httpbin.org/put', data={'key': 'value'}))
print(requests.delete('https://httpbin.org/delete'))
print(requests.head('https://httpbin.org/get'))
print(requests.patch('https://httpbin.org/patch', data={'key': 'value'}))
print(requests.options('https://httpbin.org/get'))


responce = requests.post('https://httpbin.org/post', data={'key':'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])
