from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key="AIzaSyA-bF7gPRQgSWq3pxfnjixAUEUYamYJSPg")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Describe this title in english dhankawdi sahkarnagar kshetriy karyala antargat kai.vishnu urf annnasaheb jagtap jaltaran talaw v vyayamshala v kai.abhijit patangarao kadam bahuddeshiy krida sankul ya thikani stapty vishyak durustichi kame karane"
)
print(response.text)