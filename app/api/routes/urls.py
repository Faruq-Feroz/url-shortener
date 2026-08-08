from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.schemas.url import URLCreate, URLResponse
from app.services import url as url_service

router = APIRouter(prefix="/urls", tags=["urls"])


@router.post("", response_model=URLResponse, status_code=201)
def create_url(payload: URLCreate) -> URLResponse:
    short_code, original_url = url_service.create_short_url(str(payload.original_url))
    return URLResponse(original_url=original_url, short_code=short_code)


@router.get("/{short_code}")
def redirect_to_url(short_code: str):
    original_url = url_service.get_original_url(short_code)
    if original_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=original_url, status_code=307)

