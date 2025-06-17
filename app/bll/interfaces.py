from abc import ABC, abstractmethod
from typing import List, Optional
from .models import User, Game, Review, PlaySession, Genre

class IUserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]: ...

class IGameRepository(ABC):
    @abstractmethod
    def get_game(self, game_id: int) -> Optional[Game]: ...

class IGenreRepository(ABC):
    @abstractmethod
    def get_genre(self, genre_id: int) -> Optional[Genre]: ...

class IPlaySessionRepository(ABC):
    @abstractmethod
    def get_sessions_by_user(self, user_id: int) -> List[PlaySession]: ...

    @abstractmethod
    def create_session(self, user_id: int, game_id: int): ...

class IReviewRepository(ABC):
    @abstractmethod
    def get_review(self, review_id: int) -> Optional[Review]: ...

    @abstractmethod
    def create_review(self, user_id: int, game_id: int, score: int, comment: str): ...
