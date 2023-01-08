from sqlalchemy.orm import Session

import models
import schemas
import auth


def get_player(db: Session, player_id: int):
    return db.query(models.players).filter(models.players.playerId == player_id).first()


def get_player_by_email(db: Session, email: str):
    return db.query(models.players).filter(models.players.email == email).first()


def get_country(db: Session, country_name: str):
    return db.query(models.country).filter(models.country.country_name == country_name).first()


def get_club(db: Session, club_value: str):
    return db.query(models.club).filter(models.club.club_value == club_value).first()


def create_player(db: Session, player: schemas.playerCreate):
    hashed_password = auth.get_password_hash(player.password)
    db_player = models.players(name=player.name, height=player.height, email=player.email,
                               password=hashed_password, date_of_birth=player.date_of_birth)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def update_players(db: Session, playerId: int, player: schemas.playerCreate):
    db_user = db.query(models.players).filter(models.players.playerId == playerId).first()
    db_user.name = player.name
    db_user.email = player.email
    db_user.height = player.height
    db_user.date_of_birth = player.date_of_birth
    db_user.password = player.password
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_club(db: Session, clubId: int):
    print(clubId)
    db_delete = db.query(models.club).filter(models.club.clubId == clubId).first()
    db.delete(db_delete)
    db.commit()
    return None


def create_country(db: Session, country: schemas.countryCreate):
    db_country = models.country(country_name=country.country_name, countryId=country.countryId,
                                continent=country.continent)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


def create_club(db: Session, club: schemas.clubCreate):
    db_club = models.club(clubId=club.clubId, club_value=club.club_value,
                                club_name=club.club_name)
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club