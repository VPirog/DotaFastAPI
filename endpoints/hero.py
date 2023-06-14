from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import HeroIn, HeroOut, HeroesOut
from database import get_session, Hero

router2 = APIRouter(prefix="/hero", tags=["hero"])


@router2.get("/{hero_id}", response_model=HeroOut)
async def get_hero(hero_id: int,
                   session: Session = Depends(get_session)):
    hero: Hero = session.query(Hero).get(hero_id)
    if hero:
        hero_dto = HeroOut(**hero.__dict__)
        return hero_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Hero with id {hero_id} not found!")


@router2.post("/", response_model=HeroOut)
async def create_hero(hero: HeroIn):
    session = get_session()
    orm_hero = Hero(**hero.dict())
    session.add(orm_hero)
    session.commit()
    hero_dto = HeroOut(**orm_hero.__dict__)
    return hero_dto


@router2.delete("/delete/{hero_id}")
async def delete_hero(hero_id: int,
                      session: Session = Depends(get_session)):
    hero: Hero = session.query(Hero).get(hero_id)
    if hero:
        session.delete(hero)
        session.commit()
        raise HTTPException(status_code=200,
                            detail=f"Hero with id {hero_id} deleted!")

    else:
        raise HTTPException(status_code=404,
                            detail=f"Hero with id {hero_id} not found!")


@router2.put("/update/{hero_id}")
async def update_hero(hero: HeroIn,
                      hero_id: int,
                      session: Session = Depends(get_session)):
    server_hero: Hero = session.query(Hero).get(hero_id)
    if hero:
        server_hero.name = hero.name
        server_hero.base_strength = hero.base_strength
        server_hero.base_agility = hero.base_agility
        server_hero.base_intelligence = hero.base_intelligence
        server_hero.str_gain = hero.str_gain
        server_hero.agi_gain = hero.agi_gain
        server_hero.int_gain = hero.int_gain
        server_hero.base_armor = hero.base_armor
        server_hero.base_magic_res = hero.base_magic_res
        server_hero.base_move_speed = hero.base_move_speed
        server_hero.attack_type = hero.attack_type
        session.commit()
        return HeroOut(**server_hero.__dict__)
    else:
        raise HTTPException(status_code=404,
                            detail=f"Hero with id {hero_id} not found!")