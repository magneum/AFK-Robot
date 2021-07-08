import json
import os

class Config(object):
    LOGGER = True
    API_ID =  6372795 
    API_HASH = "4b7731b0a6d8e15bef82863887feb293"
    TOKEN = "1825575975:AAESpVD0Q4spSGZmz1J1aDeeOpjRLGu0DcE"  
    OWNER_ID = 1836310130  
    OWNER_USERNAME = "@hypevoidsoul"
    SQLALCHEMY_DATABASE_URI = "postgresql://jttrtiadnflnpo:5f277b7428e3eb1d5faf750cc94b3d6101ad6791524ce740c34cdc59badba4d5@ec2-34-232-191-133.compute-1.amazonaws.com:5432/ddlot51iq9tl5k"
    LOAD = []
    NO_LOAD = []
    WORKERS = 8

class Development(Config):
    LOGGER = True