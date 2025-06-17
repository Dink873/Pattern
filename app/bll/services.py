from app.bll.interfaces import IUserRepository, IGameRepository, IReviewRepository, IPlaySessionRepository

class SteamService:
    def __init__(self, user_repo: IUserRepository, game_repo: IGameRepository,
                 review_repo: IReviewRepository, session_repo: IPlaySessionRepository):
        self.user_repo = user_repo
        self.game_repo = game_repo
        self.review_repo = review_repo
        self.session_repo = session_repo

    def play_game(self, user_id: int, game_id: int):
        self.session_repo.create_session(user_id, game_id)

    def review_game(self, user_id: int, game_id: int, score: int, comment: str):
        self.review_repo.create_review(user_id, game_id, score, comment)
