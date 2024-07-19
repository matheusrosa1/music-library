from fastapi import FastAPI
from random import choice
from app.models import Music, MusicInDB, MusicLibrary

app = FastAPI(
    title="API de Músicas", description="API para cadastro de músicas", version="1.0.0"
)


@app.post("/songs", response_model=dict | str, status_code=201)
def create_song(music: Music):
    return MusicLibrary.create(music)


@app.get("/songs", response_model=list[MusicInDB])
def get_all_songs():
    return MusicLibrary.read()


@app.get("/songs/random", response_model=MusicInDB)
def get_random_song():
    all_songs = MusicLibrary.read()
    return choice(all_songs)


# Usar as rotas de get by id, depois das outras rotas de get, para evitar conflito de rotas, pois ele pode identificar uma palavra, como por exemplo random como um id
@app.get("/songs/{song_id}", response_model=MusicInDB)
def get_song_by_id(song_id: str):
    return MusicLibrary.read_one(song_id)


@app.put("/songs/{song_id}", response_model=MusicInDB)
def update_song(song_id: str, music: Music):
    try:
        return MusicLibrary.update(song_id, music)
    except ValueError:
        return "Música não encontrada"


@app.delete("/songs/{song_id}", response_model=dict | str)
def delete_song(song_id: str):
    try:
        return MusicLibrary.delete(song_id)
    except ValueError:
        return "Música não encontrada"
