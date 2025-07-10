from fastapi import APIRouter

router = APIRouter()

@router.get("/media")
def get_all_media():
    return {}

@router.post("/media")
def add_media():
    return {}

@router.put("/media/{id}")
def update_media():
    return {}

@router.delete("/media{id}")
def delete_media():
    return {}

@router.get("/media/{id}")
def get_media():
    return {}