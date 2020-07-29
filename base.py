#-*- encoding: utf-8 -*-
import base64

def encode(plain):
    return base64.b64encode(str(plain).encode())

def decode(code):
    return base64.b64decode(bytes(code).decode())
