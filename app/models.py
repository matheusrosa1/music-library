from multiprocessing import Value
import re
from bson import ObjectId
from pydantic import BaseModel, Field
from pymongo import ReturnDocument
from app.database import db
from app.main import update_song


class Music(BaseModel):
    name: str
    artist: str
    album: str
    release_year: str
    genre: str
    image: str


class MusicInDB(
    Music
):  # Essa classe existe para manuear as musicas no banco dados, pois no MongoDB o id é retornado como um ObjectId (que trata-se de uma instancia) e não como id normal
    id: str = Field(..., alias="_id")  # Facilitar o uso do id do banco de dados


class MusicLibrary:
    _collections = db["musics"]

    @classmethod
    def create(cls, music: Music):
        cls._collections.insert_one(music.__dict__)  # ou vars(music)
        return "Música cadastrada com sucesso"

    @classmethod
    def read(cls):
        for song in cls._collection.find():
            MusicInDB(
                _id=str(song.pop("_id")), **song
            )  # coleta o id do banco de dados, remove o id e retorna o id removido, então temos em mão o id do banco de dados e esse deve ser passado como string para o MusicInDB, além do restante dos dados (que nao precisam de nenhum tratamento)
            # [MusicInDB(_id=str(song.pop("_id")), **song) for song in cls._collection.find()] # outra forma de fazer a mesma coisa

    @classmethod
    def read_one(cls, song_id: str):
        found_song = cls._collection.find_one(
            {"_id": ObjectId(song_id)}
        )  # tem que procurar pelo id utilizando o _id, pois é assim que o MongoDB ele é armazenado como protegido
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
        return MusicInDB(_id=str(update_song.pop("_id")), **update_song)

    @classmethod
    def delete(cls, song_id: str):
        deleted_song = cls._collection.find_one_and_delete({"_id": ObjectId(song_id)})
        if deleted_song is None:
            raise ValueError("Música não encontrada")
        return "Música deletada com sucesso"
