from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/post/players/", response_model=schemas.player)
def create_player(player: schemas.playerCreate, db: Session = Depends(get_db)):
    db_player = crud.get_player_by_email(db, email=player.email)
    if db_player:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_player(db=db, player=player)


@app.post("/post/country/", response_model=schemas.country)
def create_country(country: schemas.countryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db, country=country)


@app.post("/post/club/", response_model=schemas.club)
def create_country(club: schemas.clubCreate, db: Session = Depends(get_db)):
    return crud.create_club(db, club=club)


@app.get("/country/name/", response_model=schemas.country)
def read_users(country_name: str,db: Session = Depends(get_db)):
    return crud.get_country(db=db, country_name=country_name)


@app.get("/players/{player_id}", response_model=schemas.player)
def read_user(player_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_player(db, player_id=player_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/players/put/{player_id}", response_model=schemas.player)
async def update_players(player: schemas.playerCreate, db: Session = Depends(get_db),
    player_id: int = Path(ge=0, le=30, default=1)):
    return crud.update_players(db=db, player=player, playerId=player_id)


@app.get("/club/{club_value}", response_model=schemas.club)
def read_club(club_value: str,db: Session = Depends(get_db)):
    clubvalue = crud.get_club(db=db, club_value=club_value)
    return clubvalue


@app.delete("/delete/club/{club_id}", response_model=schemas.club)
async def delete_club(club_id: int = Path(ge=0, le=30, default=1),db: Session = Depends(get_db)):
    return crud.delete_club(db=db, clubId=club_id)
