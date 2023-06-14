from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from models import CommentIn, CommentOut, CommentsOut
from database import get_session, GuideCommentary

router = APIRouter(prefix="/comment", tags=["comment"])


@router.get("/{guide_id}-{user_id}", response_model=CommentOut)
async def get_comment(user_id: int,
                      guide_id: int,
                      session: Session = Depends(get_session)
                      ):
    comment: GuideCommentary = session.query(GuideCommentary).get({"user_id": user_id, "guide_id": guide_id})
    if comment:
        comment_dto = CommentOut(**comment.__dict__)
        return comment_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"GuideCommentary with id not found!")


@router.post("/", response_model=CommentOut)
async def create_comment(comment: CommentIn):
    session = get_session()
    orm_comment = GuideCommentary(**comment.dict())
    session.add(orm_comment)
    session.commit()
    comment_dto = CommentOut(**orm_comment.__dict__)
    return comment_dto


@router.delete("/update/{guide_id}-{user_id}")
async def update_comment(guide_id: int, user_id: int, comment: CommentIn, session: Session = Depends(get_session)):
    query = session.query(GuideCommentary).filter(GuideCommentary.user_id == user_id,
                                                  GuideCommentary.guide_id == guide_id)
    affected_rows = query.delete()
    session.commit()

    if affected_rows > 0:
        raise HTTPException(status_code=200,
                            detail=f"GuideCommentary with guide_id={guide_id} and user_id={user_id} deleted!")
    else:
        raise HTTPException(status_code=404,
                            detail=f"GuideCommentary with guide_id={guide_id} and user_id={user_id} not found!")



@router.put("/update/{guide_id}-{user_id}", response_model=CommentOut)
async def update_comment(guide_id: int, user_id: int, comment: CommentIn, session: Session = Depends(get_session)):
    query = session.query(GuideCommentary).filter(GuideCommentary.user_id == user_id,
                                                  GuideCommentary.guide_id == guide_id)
    affected_rows = query.update({GuideCommentary.commentary: comment.commentary})
    session.commit()

    if affected_rows > 0:
        return CommentOut(guide_id=guide_id, user_id=user_id, commentary=comment.commentary)
    else:
        raise HTTPException(status_code=404,
                            detail=f"GuideCommentary with guide_id={guide_id} and user_id={user_id} not found!")
