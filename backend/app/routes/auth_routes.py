from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    return {}

@router.get("/login")
def login():
    return {}

@router.get("/logout")
def logout():
    return {}