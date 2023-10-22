from fastapi import FastAPI, WebSocket, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
from typing import List

app = FastAPI()

# SQLAlchemy
DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Define Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    swipes = relationship("Swipe", back_populates="user")


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Swipe(Base):
    __tablename__ = "swipes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user = relationship("User", back_populates="swipes")


Base.metadata.create_all(bind=engine)


# Pydantic Models
class UserCreate(BaseModel):
    username: str


class SwipeCreate(BaseModel):
    user_id: int
    movie_id: int


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/signup/")
async def signup(user: UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return {"username": user.username, "id": db_user.id}


@app.post("/login/")
async def login(username: str):
    # actual login logic will go here
    return {"message": f"Logged in as {username}"}


@app.get("/movies/")
async def get_movies():
    # Stub; I'll replace this with a real movie list, probably fetched from an external API
    return [{"id": 1, "name": "Inception"}, {"id": 2, "name": "The Matrix"}]


@app.post("/swipe/")
async def create_swipe(swipe: SwipeCreate, db: SessionLocal = Depends(get_db)):
    db_swipe = Swipe(**swipe.dict())
    db.add(db_swipe)
    db.commit()
    return {"message": "Swipe recorded"}


@app.get("/match/")
async def get_match():
    # Implement match finding logic here
    return {"message": "No matches found"}


@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Implement real-time matching logic here
        await websocket.send_text(f"Message text was: {data}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
