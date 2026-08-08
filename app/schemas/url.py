from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    """What the client sends when creating a shortened URL."""

    original_url: HttpUrl


class URLResponse(BaseModel):
    """What the API returns after a URL is shortened."""

    original_url: HttpUrl
    short_code: str
