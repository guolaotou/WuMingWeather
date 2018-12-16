import requests
from bs4 import BeautifulSoup

url = "https://tianqi.moji.com/weather/china/beijing/beijing"

htmlData = requests.get(url).text
# print("htmlData: ", htmlData)
soup = BeautifulSoup(htmlData, "lxml")
weather = soup.find("div", attrs={"class": "wea_weather clearfix"})
# print("weather: ", weather)

temp1 = weather.find("em").get_text()
temp2 = weather.find("b").get_text()

# print("temp1:", temp1)
# print("temp2:", temp2)

# 天气预报
forecast = soup.find("div", attrs={"class": "forecast clearfix"})

# print("weather: ", forecast)

forecast_tomorrow = forecast.find("li").get_text()
forecast_tomorrow = soup.select(".forecast.clearfix > ul")[1]
print("------forecast_tomorrow------------\n", forecast_tomorrow)
forecast_tomorrow = soup.select(".forecast.clearfix > ul")[1].select("li")[4].find("strong").get_text().strip()
print("------forecast_tomorrow22------------\n", forecast_tomorrow)
print(type(forecast_tomorrow))

AQI = soup.select(".wea_alert.clearfix > ul > li > a > em")[0].get_text()
print("AQI", AQI)
