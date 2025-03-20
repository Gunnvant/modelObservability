from __future__ import annotations
import urllib.parse
from pymongo import MongoClient
from abc import ABC, abstractmethod


class DBServiceInterface(ABC):
    @abstractmethod
    def init_client(self):
        raise NotImplemented

    @abstractmethod
    def close(self):
        raise NotImplemented
