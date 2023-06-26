import tempfile
from typing import List

from fastapi import FastAPI, UploadFile
from minio import Minio
from dotenv import load_dotenv
import os
from PIL import Image
from kafka.producer import KafkaProducer
import app.main as ma
import app.schemas as schemas
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')



topic = "my-notifications"





prod = FastAPI(


)

load_dotenv()
LOCAL_FILE_PATH = os.environ.get('LOCAL_FILE_PATH')
MINIO_API_HOST = "http://localhost:9000"
MINIO_CLIENT = Minio("localhost:9000", secure=False)
@prod.post('/file')
def send_img(file: UploadFile):
    image = Image.open(file.file)
    new_image = image.resize((500, 500))
    with tempfile.NamedTemporaryFile() as temp_file:
        new_image.save(temp_file.name + '.jpg')
    found = MINIO_CLIENT.bucket_exists("bucket-my")
    if not found:
       MINIO_CLIENT.make_bucket("bucket-my")
    else:
       print("Bucket already exists")
    MINIO_CLIENT.fput_object("bucket-my", file.filename, temp_file.name + '.jpg')

    print("It is successfully uploaded to bucket")





