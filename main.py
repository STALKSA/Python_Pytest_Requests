import requests

# Базовый URL API
BASE_URL = 'https://api.pokemonbattle.ru/v2'

# Токен тренера (замените на ваш токен)
TRAINER_TOKEN = 'YOUR_TRAINER_TOKEN'

# Заголовки для запросов
headers = {
    "Content-Type": "application/json",
    "trainer_token": TRAINER_TOKEN  # Токен передается в заголовке
}

# 1. Создание покемона (POST /pokemons)
def create_pokemon():
    url = f"{BASE_URL}/pokemons"
    data = {
        "name": "Бульбазавр",
        "photo_id": 1  # ID фото покемона
    }
    try:
        response = requests.post(url, json=data, headers=headers, verify=False)  # Отключение SSL
        print("Создание покемона:")
        print(response.status_code)
        print(response.json())
        return response.json().get("id")  # Возвращаем ID созданного покемона
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

# 2. Изменение покемона (PATCH /pokemons)
def update_pokemon(pokemon_id):
    url = f"{BASE_URL}/pokemons"
    data = {
        "pokemon_id": pokemon_id,
        "name": "Бульбазаврррр",  # Новое имя покемона
        "photo_id": 2  # Новое фото покемона
    }
    try:
        response = requests.patch(url, json=data, headers=headers, verify=False)  # Отключение SSL
        print("Изменение покемона:")
        print(response.status_code)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")

# 3. Поймать покемона в покебол (POST /trainers/add_pokeball)
def catch_pokemon(pokemon_id):
    url = f"{BASE_URL}/trainers/add_pokeball"
    data = {
        "pokemon_id": pokemon_id
    }
    try:
        response = requests.post(url, json=data, headers=headers, verify=False)  # Отключение SSL
        print("Поймать покемона в покебол:")
        print(response.status_code)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    # Создаем покемона и получаем его ID
    pokemon_id = create_pokemon()

    if pokemon_id:
        # Меняем имя покемона
        update_pokemon(pokemon_id)

        # Ловим покемона в покебол
        catch_pokemon(pokemon_id)