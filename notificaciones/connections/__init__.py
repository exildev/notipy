#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file = os.path.join(BASE_DIR, 'connections/connections.json')

HOST = ''
IO_PORT = ''
WEB_PORT = ''

with open(file, 'r') as content_file:
    content = content_file.read()
    obj = json.loads(content)
    HOST = obj['host']
    IO_PORT = obj['io_port']
    WEB_PORT = obj['web_port']