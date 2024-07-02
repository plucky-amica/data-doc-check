import requests

def extract_data():
    url = "https://api.example.com/data"
    response = requests.get(url)
    data = response.json()
    print("Data extracted:", data)
    return data
    #adding a dev comment to this repo in the dev-data instance

if __name__ == "__main__":
    extract_data()
