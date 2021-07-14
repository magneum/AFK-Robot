import json
import os

class Config(object):
    LOGGER = True
    API_ID =  637
    API_HASH = "4b7731b0"
    TOKEN = "1825575975:AAESpVD"  
    SSQLALCHEMY_DATABASE_URI = "postgresql:/"
    LOAD = []
    NO_LOAD = []
    WORKERS = 8

class Development(Config):
    LOGGER = True
