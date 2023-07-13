import requests


if __name__ == "__main__":
    response = requests.get("https://www.google.com")
    print(response.status_code)