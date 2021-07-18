import os
from dotenv import load_dotenv
load_dotenv()    # take environment variables from .env.
API_KEY = os.getenv('API_KEY')    #API_KEY放在env裡面讓getenv拿到
