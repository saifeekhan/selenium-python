from jproperties import Properties

class ConfigDataProvider():
    def __init__(self):
        self.p = Properties()
        with open("C:/Users/saif.khan/PycharmProjects/MyFramework/Config/config.properties", "rb") as f:
            self.p.load(f, "utf-8")

    def getBrowser(self):
        return self.p["browser"].data

    def getBaseUrl(self):
        return self.p["baseUrl"].data

