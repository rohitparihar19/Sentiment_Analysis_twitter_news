# Importing api key file 
import configparser 

def upload():
    config = configparser.RawConfigParser() 
    config.read(filenames = 'Twitter.txt')
    return config