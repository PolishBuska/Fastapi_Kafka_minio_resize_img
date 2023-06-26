import asyncio

from fastapi import FastAPI
from kafka import KafkaConsumer

from json import loads

from pydantic import BaseModel
from typing import List, Dict, Any
from app.producer import prod
import app.schemas as schemas
app = FastAPI(

)
app.mount("/producer", prod)

topic = "my-notifications"


@app.get('/get_data')
def root():
    return poll_messages(topic)


def poll_messages(topic):
    print("Started polling from topic:", topic)
    consumer = KafkaConsumer(
        topic,
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        auto_offset_reset='latest',
        group_id="main",
        enable_auto_commit=True,
    )

    messages = consumer.poll(timeout_ms=1000)
    records = []
    for tp, msgs in messages.items():
        for msg in msgs:
            record = schemas.ConsumerRecord(**msg._asdict())
            return record



