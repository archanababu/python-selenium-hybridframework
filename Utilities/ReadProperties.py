import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod # Static method means this method can be access by using class name. No need to create an object
    def getApplicationURL(self):
        return config.get('test','baseURL')
    
    @staticmethod # Static method means this method can be access by using class name. No need to create an object
    def getEmail(self):
        return config.get('test','email')
    
    @staticmethod # Static method means this method can be access by using class name. No need to create an object
    def getPassword(self):
        return config.get('test','password')
        

