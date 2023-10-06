from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    url = f'https://www.google.com/search?q={city}&hl=en'
    res = requests.get(url, headers=headers)
    print("Searching......\n")
    soup = BeautifulSoup(res.text, 'html.parser')

    # Updated selectors
    location = soup.select('.BNeawe.iBp4i.AP7Wnd')[0].text
    time = soup.select('.BNeawe.tAd8D.AP7Wnd')[0].text
    info = soup.select('.BNeawe.tAd8D.AP7Wnd')[1].text
    temperature = soup.select('.BNeawe.iBp4i.AP7Wnd')[1].text

    print(location)
    print(time)
    print(info)
    print(temperature)

def main():
    city = input("Enter the Name of Any City >>  ")
    city = city + " weather"
    weather(city)

if __name__ == '__main__':
    main()
