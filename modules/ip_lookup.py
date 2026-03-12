import requests

def lookup(ip):

    url = f"https://ipinfo.io/{ip}/json"
    data = requests.get(url).json()

    return data
