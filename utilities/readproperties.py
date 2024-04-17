import configparser

config = configparser.RawConfigParser()

config.read("C:\\CuraHeathcare\\configurations\\config.ini")



class Readconfig:

    @staticmethod
    def geturl():
        url = config.get("common info", "url")
        return url


    @staticmethod
    def getusername():
        Email = config.get("common info", "username")
        return Email

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password