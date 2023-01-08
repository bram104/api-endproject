from pydantic import BaseModel


class playerBase(BaseModel):
    name: str
    height: float
    email: str
    date_of_birth: str


class player(playerBase):
    playerId: int

    class Config:
        orm_mode = True


class playerCreate(playerBase):
    password: str | None = "Invalid"


class countryBase(BaseModel):
    country_name: str
    continent: str
    countryId: int


class country(countryBase):

    class Config:
        orm_mode = True


class clubBase(BaseModel):
    clubId: int
    club_name: str
    club_value: str


class club(clubBase):

    class Config:
        orm_mode = True


class countryCreate(countryBase):
    pass


class clubCreate(clubBase):
    pass
