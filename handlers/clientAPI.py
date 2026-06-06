import requests

def requestSpaceData():
    url = 'http://api.open-notify.org/astros.json'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"NASA server error. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None