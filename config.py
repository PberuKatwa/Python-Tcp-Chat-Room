from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    HOST=os.getenv("HOST")
    PORT=int( os.getenv("PORT") )
