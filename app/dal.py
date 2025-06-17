from sqlalchemy.orm import Session
from app.bll.models import User, Game, Genre, PlaySession, Review
from app.bll.interfaces import IUserRepository, IGameRepository, IGenreRepository, IPlaySessionRepository, IReviewRepository

class DataAccessLayer(IUserRepository, IGameRepository, IGenreRepository, IPlaySessionRepository, IReviewRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_game(self, game_id: int) -> Game:
        return self.db.query(Game).filter(Game.id == game_id).first()

    def get_genre(self, genre_id: int) -> Genre:
        return self.db.query(Genre).filter(Genre.id == genre_id).first()

    def get_sessions_by_user(self, user_id: int):
        return self.db.query(PlaySession).filter(PlaySession.user_id == user_id).all()

    def create_session(self, user_id: int, game_id: int):
        session = PlaySession(user_id=user_id, game_id=game_id)
        self.db.add(session)
        self.db.commit()

    def get_review(self, review_id: int) -> Review:
        return self.db.query(Review).filter(Review.id == review_id).first()

    def create_review(self, user_id: int, game_id: int, score: int, comment: str):
        review = Review(user_id=user_id, game_id=game_id, score=score, comment=comment)
        self.db.add(review)
        self.db.commit()
