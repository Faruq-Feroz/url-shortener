from fastapi import APIRouter

from app.schemas.url import URLCreate, URLResponse
from app.services import url as url_service

router = APIRouter(prefix="/urls", tags=["urls"])


@router.post("", response_model=URLResponse, status_code=201)
def create_url(payload: URLCreate) -> URLResponse:
    short_code, original_url = url_service.create_short_url(str(payload.original_url))
    return URLResponse(original_url=original_url, short_code=short_code)
