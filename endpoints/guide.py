from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from models import GuideIn, GuideOut, GuidesOut
from database import get_session, Guide

router = APIRouter(prefix="/guide", tags=["guide"])


@router.get("/{guide_id}", response_model=GuideOut)
async def get_guide(guide_id: int,
                   session: Session = Depends(get_session)):
    guide: Guide = session.query(Guide).get(guide_id)
    if guide:
        guide_dto = GuideOut(**guide.__dict__)
        return guide_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Guide with id {guide_id} not found!")


@router.post("/", response_model=GuideOut)
async def create_guide(guide: GuideIn):
    session = get_session()
    orm_guide = Guide(**guide.dict())
    session.add(orm_guide)
    session.commit()
    guide_dto = GuideOut(**orm_guide.__dict__)
    return guide_dto


@router.delete("/delete/{guide_id}")
async def delete_guide(guide_id: int,
                      session: Session = Depends(get_session)):
    guide: Guide = session.query(Guide).get(guide_id)
    if guide:
        session.delete(guide)
        session.commit()
        raise HTTPException(status_code=200,
                            detail=f"Guide with id {guide_id} deleted!")

    else:
        raise HTTPException(status_code=404,
                            detail=f"Guide with id {guide_id} not found!")


@router.put("/update/{guide_id}")
async def update_guide(guide_id: int, guide: GuideIn, session: Session = Depends(get_session)):
    server_guide: Guide = session.query(Guide).get(guide_id)
    if server_guide:
        server_guide.name = guide.name
        server_guide.rating = guide.rating
        server_guide.description = guide.description
        server_guide.owner_user_id = guide.owner_user_id
        server_guide.hero_id = guide.hero_id
        server_guide.main_text = guide.main_text
        session.commit()
        return GuideOut(id=server_guide.id, name=server_guide.name, rating=server_guide.rating, description=server_guide.description,
                        owner_user_id=server_guide.owner_user_id, hero_id=server_guide.hero_id, main_text=server_guide.main_text)
    else:
        raise HTTPException(status_code=404, detail=f"Guide with id {guide_id} not found!")
