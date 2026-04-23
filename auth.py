from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Partner

def verify_api_key(
    x_api_key: str = Header(...),
    db: Session = Depends(get_db)
):
    partner = db.query(Partner).filter(Partner.api_key == x_api_key).first()

    if not partner:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return partner