#!/usr/bin/python3
"""Initializes model package"""
from os import getenv
store_t = getenv('UPSELL_TYPE_STORAGE')

if store_t == "db":
    from models.engine.db import database
    storage = database()
    storage.reload()