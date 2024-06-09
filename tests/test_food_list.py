import requests

def test_food_list():
    url = "https://eten-api.vercel.app/api/foodList"
    headers = {
        "accept": "*/*",
       }

    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
