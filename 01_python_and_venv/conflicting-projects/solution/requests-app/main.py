import requests

if requests.__version__ != "2.31.0":
    raise ValueError("wrong version of requests installed")

if __name__ == "__main__":
    response = requests.get("https://www.google.com")
    print(response.status_code)