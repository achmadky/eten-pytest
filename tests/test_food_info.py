import requests

def test_food_info():
    url = "https://eten-api.vercel.app/api/foodInfo?name=Egg"
    headers = {
        "accept": "application/json, text/plain, */*",
}

    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}. Response: {response.text}"
    data = response.json()
    assert "food" in data, f"Expected 'food' in response, but got {data}"
    assert "name" in data["food"], f"Expected 'name' in 'food' data, but got {data['food']}"
    assert data["food"]["name"] == "Egg", f"Expected food name to be 'Egg', but got {data['food']['name']}"

    # Check the calories and cholesterol for Egg
    assert data["food"]["calories"] == 78, f"Expected 78 calories, but got {data['food']['calories']}"
    assert data["food"]["cholesterol"] == 186, f"Expected 186 cholesterol, but got {data['food']['cholesterol']}"

def test_food_info_nonexistent():
    url = "https://eten-api.vercel.app/api/foodInfo?name=NonExistentFood"
    headers = {
        "accept": "application/json, text/plain, */*",
}

    response = requests.get(url, headers=headers)
    
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}. Response: {response.text}"
    

def test_food_info_invalid_request():
    url = "https://eten-api.vercel.app/api/foodInfo"
    headers = {
        "accept": "application/json, text/plain, */*",
 }

    response = requests.get(url, headers=headers)
    
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}. Response: {response.text}"
