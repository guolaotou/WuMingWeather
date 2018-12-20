import requests
from bs4 import BeautifulSoup

class Splider():
    def __init__(self):
        url = "https://tianqi.moji.com/weather/china/beijing/beijing"
        htmlData = requests.get(url).text
        soup = BeautifulSoup(htmlData, "lxml")
        weather = soup.find("div", attrs={"class": "wea_weather clearfix"})

        self.html_data = htmlData
        self.weather = weather

        # 天气预报 - 暂时返回当前的
        forecast = soup.find("div", attrs={"class": "forecast clearfix"})
        print("forecast: ", forecast)
        print("------forecast_today------------\n")
        forecast_today = soup.select(".forecast.clearfix > ul")[0]
        # print("forecast_today", forecast_today)

        print("------forecast_separate------------\n")
        # 气温
        temperature = forecast_today.select("li")[2].get_text()
        self.temprature = temperature
        print("temperature", temperature)

        # 风力
        wind_dir = forecast_today.select("li")[3].find("em").get_text()
        wind_power = forecast_today.select("li")[3].find("b").get_text()
        self.wind_dir = wind_dir
        self.wind_power= wind_power
        print("wind_dir", wind_dir)
        print("wind_power", wind_power)

        aqi = forecast_today.select("li")[4].find("strong").get_text().strip()
        self.aqi = aqi
        print("aqi", aqi)

        # 获取实时信息
        # AQI = soup.select(".wea_alert.clearfix > ul > li > a > em")[0].get_text()
        # print("AQI", AQI)

    def test(self):
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

    def get_aqi(self):
        return "空气质量：" + self.aqi

    def get_wind(self):
        return "风向：" + self.wind_dir + "\n" + "风力：" + self.wind_power

    def get_temperature(self):
        return "气温： " + self.temprature

if __name__ == "__main__":
    spider = Splider()
    temperature = spider.get_temperature()
    wind = spider.get_wind()
    aqi = spider.get_aqi()
    subject = "\n".join([temperature, wind, aqi])
    print(subject)
    # spider