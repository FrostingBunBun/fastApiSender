from fastapi import FastAPI
import sqlite3
from typing import List, Dict, Any

app = FastAPI()
DB_PATH = "C:\Users\Halof\Desktop\AssSetToes\Assetto Corsa Dedicated Server\Stracker\stracker.db3"

def fetch_all(query: str) -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/laps")
def get_laps():
    return fetch_all("SELECT * FROM LapTimes")

@app.get("/sessions")
def get_sessions():
    return fetch_all("SELECT * FROM Session")

@app.get("/players")
def get_players():
    return fetch_all("SELECT * FROM Players")

@app.get("/cars")
def get_cars():
    return fetch_all("SELECT * FROM Cars")

@app.get("/tracks")
def get_tracks():
    return fetch_all("SELECT * FROM Tracks")

@app.get("/player-in-session")
def get_player_in_session():
    return fetch_all("SELECT * FROM PlayerInSessionView")
