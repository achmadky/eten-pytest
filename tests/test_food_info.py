import requests

def test_food_info():
    url = "https://eten-api.vercel.app/api/foodInfo?name=Egg"
    headers = {
        "accept": "application/json, text/plain, */*",

}

    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert "food" in data
    assert "name" in data["food"]
    assert data["food"]["name"] == "Egg"
