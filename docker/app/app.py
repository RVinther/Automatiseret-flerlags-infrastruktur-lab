from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
    )

@app.get("/")
def index():
    return {"msg": "App is running!"}

@app.get("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"database": "connected", "version": version[0]})
    except Exception as e:
        return jsonify({"database": "error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)