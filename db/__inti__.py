import os
import psycopg2

CONNECTION_STRING = os.getenv("CONNECTION_STRING")
conn = psycopg2.connect(CONNECTION_STRING)


