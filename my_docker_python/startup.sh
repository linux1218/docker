#!/bin/bash

sleep 1

echo "pip install pymysql"
pip install pymysql

sleep 1
echo "python -u -m db_handle.py"
python -u -m db_handle.py
sleep 1