from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Partner
from auth import verify_api_key
import secrets

router = APIRouter(prefix="/api/partners", tags=["Partners"])

# GET all
@router.get("/")
def get_all_partners(
    db: Session = Depends(get_db),
    #current_partner = Depends(verify_api_key)
):
    return db.query(Partner).all()

# GET by ID
@router.get("/{partner_id}")
def get_partner(
    partner_id: int,
    db: Session = Depends(get_db),
    #current_partner = Depends(verify_api_key)
):
    return db.query(Partner).filter(Partner.id == partner_id).first()

# CREATE
@router.post("/")
def create_partner(
    name: str,
    email: str,
    country: str,
    db: Session = Depends(get_db),
    #current_partner = Depends(verify_api_key)
):
    api_key = secrets.token_hex(16)

    new_partner = Partner(
        name=name,
        email=email,
        country=country,
        api_key=api_key
    )

    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)

    return new_partner