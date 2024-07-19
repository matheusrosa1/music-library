from bson import ObjectId
from pydantic import BaseModel, Field
from pymongo import ReturnDocument
from app.database import db


class Music(BaseModel):
    name: str
    artist: str
    album: str
    release_year: int
    genre: str
    image: str


class MusicInDB(Music):
    id: str = Field(alias="_id")


class MusicLibrary:
    _collection = db["musics"]

    @classmethod
    def create(cls, music: Music):
        cls._collection.insert_one(music.__dict__)  # ou vars(music)
        return "Música cadastrada com sucesso"

    @classmethod
    def read(cls):
        return [
            MusicInDB(_id=str(song.pop("_id")), **song)
            for song in cls._collection.find()
        ]  # coleta o id do banco de dados, remove o id e retorna o id removido, então temos em mão o id do banco de dados e esse deve ser passado como string para o MusicInDB, além do restante dos dados (que nao precisam de nenhum tratamento)

    @classmethod
    def read_one(cls, song_id: str):
        found_song = cls._collection.find_one({"_id": ObjectId(song_id)})
        if found_song is not None:
            return MusicInDB(
                _id=str(found_song.pop("_id")), **found_song
            )  # CONVERSAO DO ID PARA PODER ADICIONAR O VALOR DO ID AO NOSSO ATRIBUTO DA CLASSE MusicInDB
        else:
            raise ValueError("Música não encontrada")

    @classmethod
    def update(cls, song_id: str, music: Music):
        updated_song = cls._collection.find_one_and_update(  # o find_one_and_update permite que você atualize um documento e retorne o documento antes ou depois da atualização
            {"_id": ObjectId(song_id)},
            {"$set": music.__dict__},
            return_document=ReturnDocument.AFTER,
        )
        if updated_song is None:
            raise ValueError("Música não encontrada")
        return MusicInDB(_id=str(updated_song.pop("_id")), **updated_song)

    @classmethod
    def delete(cls, song_id: str):
        deleted_song = cls._collection.find_one_and_delete({"_id": ObjectId(song_id)})
        if deleted_song is None:
            raise ValueError("Música não encontrada")
        return "Música deletada com sucesso"
