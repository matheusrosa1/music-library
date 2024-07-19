from pydantic import BaseModel, Field
from app.database import db


class Music(BaseModel):
    name: str
    artist: str
    album: str
    release_year: str
    genre: str
    image: str


class MusicInDB(Music):
    id: str = Field(..., alias="_id")  # Facilitar o uso do id do banco de dados


class MusicLibrary:
    _collections = db["musics"]

    @classmethod
    def create(cls, music: Music):
        cls._collections.insert_one(music.__dict__)  # ou vars(music)
        return "Música cadastrada com sucesso"
