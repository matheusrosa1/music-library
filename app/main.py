from fastapi import FastAPI

from app.models import Music, MusicLibrary

app = FastAPI(title="Music API", description="API for music", version="1.0.0")


@app.post("/songs", response_model=dict | str)
def create_song(music: Music):
    return MusicLibrary.create(music)


@app.get("/songs")
def get_songs(): ...


@app.get("/songs/{song_id}")
def get_song_by_id(song_id: int): ...


@app.get("/songs/random")
def get_random_song(): ...


@app.put("/songs/{song_id}")
def update_song(song_id: int): ...


@app.delete("/songs/{song_id}")
def delete_song(song_id: int): ...
