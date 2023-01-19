import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)       #r.text is a string, it is convenient to transform that into a list
    categories = r.json()
    for category in categories:
        print(category["name"])