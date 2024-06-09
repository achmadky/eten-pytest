import requests

def test_food_info():
    url = "https://eten-api.vercel.app/api/foodInfo?name=Egg"
    headers = {
        "accept": "application/json, text/plain, */*",
        "origin": "https://eten-ui.vercel.app",
        "referer": "https://eten-ui.vercel.app/",
}

    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "name" in data
    assert data["name"] == "Egg"
