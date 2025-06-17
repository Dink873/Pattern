from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.bll.models import Base, User, Game, Genre, PlaySession, Review
from app.bll.database import get_db
from pathlib import Path
import csv

app = FastAPI()

DATABASE_URL = "sqlite:///steam_app.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/import_data/")
def import_data(db: Session = Depends(get_db)):
    import_order = [
        ("users.csv", User),
        ("genres.csv", Genre),
        ("games.csv", Game),
        ("playsessions.csv", PlaySession),
        ("reviews.csv", Review),
    ]
    results = {}
    try:
        for filename, model in import_order:
            path = Path(__file__).parent.parent / "data" / filename
            if not path.exists():
                raise HTTPException(400, detail=f"Файл {filename} не знайдено")

            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                objects = [model(**row) for row in reader]
                db.bulk_save_objects(objects)
                db.commit()
                results[filename] = len(objects)

        return {"message": "Дані імпортовано", "imported": results}
    except Exception as e:
        db.rollback()
        raise HTTPException(404, detail=f"Помилка імпорту: {str(e)}")


@app.get("/games/")
def get_all_games(db: Session = Depends(get_db)):
    try:
        games = db.query(Game).all()
        return {"games": games}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні ігор: {str(e)}")

@app.get("/games/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        if not game:
            raise HTTPException(404, detail="Гру не знайдено")
        return {"game": game}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні гри: {str(e)}")

@app.get("/genres/")
def get_all_genres(db: Session = Depends(get_db)):
    try:
        genres = db.query(Genre).all()
        return {"genres": genres}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні жанрів: {str(e)}")

@app.get("/genres/{genre_id}")
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    try:
        genre = db.query(Genre).filter(Genre.id == genre_id).first()
        if not genre:
            raise HTTPException(404, detail="Жанр не знайдено")
        return {"genre": genre}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні жанру: {str(e)}")

@app.get("/playsessions/")
def get_all_playsessions(db: Session = Depends(get_db)):
    try:
        sessions = db.query(PlaySession).all()
        return {"playsessions": sessions}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні сесій: {str(e)}")

@app.get("/playsessions/{session_id}")
def get_playsession(session_id: int, db: Session = Depends(get_db)):
    try:
        session = db.query(PlaySession).filter(PlaySession.id == session_id).first()
        if not session:
            raise HTTPException(404, detail="Сесію не знайдено")
        return {"playsession": session}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні сесії: {str(e)}")

@app.get("/reviews/")
def get_all_reviews(db: Session = Depends(get_db)):
    try:
        reviews = db.query(Review).all()
        return {"reviews": reviews}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні оглядів: {str(e)}")

@app.get("/reviews/{review_id}")
def get_review(review_id: int, db: Session = Depends(get_db)):
    try:
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            raise HTTPException(404, detail="Огляд не знайдено")
        return {"review": review}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні огляду: {str(e)}")

@app.get("/users/{user_id}/playsessions")
def get_user_sessions(user_id: int, db: Session = Depends(get_db)):
    try:
        sessions = db.query(PlaySession).filter(PlaySession.user_id == user_id).all()
        return {"playsessions": sessions}
    except Exception as e:
        raise HTTPException(404, detail=f"Помилка при отриманні сесій користувача: {str(e)}")
