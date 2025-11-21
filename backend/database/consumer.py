import json

import mysql.connector
from confluent_kafka import Consumer
from producer import host

consumer = Consumer(
    {
        "bootstrap.servers": host,
        "security.protocol": "SSL",
        "ssl.ca.location": "ca.pem",
        "ssl.certificate.location": "service.cert",
        "ssl.key.location": "service.key",
        "group.id": "ride_group",
        "auto.offset.reset": "earliest",
    }
)
