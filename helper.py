# Add your utilities or helper functions to this file.
import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                         
# the format for that file is (without the comment)                                                                           
# API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())
        
def get_together_api_key():
     load_env()
     together_api_key = os.getenv("TOGETHER_API_KEY")
     return together_api_key