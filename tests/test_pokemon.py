import requests


BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = 22038

# Тест для проверки GET /trainers
def test_get_trainers():
    """
    Проверяет, что запрос GET /trainers возвращает код 200.
    """
    url = f"{BASE_URL}/trainers"
    params = {
        "trainer_id": TRAINER_ID 
    }
    response = requests.get(url, params=params)
    assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"

# Тест для проверки имени тренера
def test_trainer_name():
    """
    Проверяет, что в ответе на запрос GET /trainers приходит имя тренера 'STALK'.
    """
    url = f"{BASE_URL}/trainers"
    params = {
        "trainer_id": TRAINER_ID  
    }
    response = requests.get(url, params=params)
    response_json = response.json()

 
    assert "data" in response_json, "Ключ 'data' отсутствует в ответе"
    assert response_json["data"], "Данные тренера отсутствуют в ответе"

    # Извлекаем данные тренера из массива data
    trainer_data = response_json["data"][0]  
    assert "trainer_name" in trainer_data, "Ключ 'trainer_name' отсутствует в данных тренера"

    # Проверяем, что имя тренера равно 'STALK'
    trainer_name = trainer_data["trainer_name"]
    assert trainer_name == "STALK", f"Имя тренера не совпадает. Ожидалось: STALK, получено: {trainer_name}"
