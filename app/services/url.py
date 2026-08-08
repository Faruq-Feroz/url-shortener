import secrets
import string

# In-memory store: short_code -> original URL string.
# Temporary until we add a database in a later step.
_urls: dict[str, str] = {}


def _generate_short_code(length: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        code = "".join(secrets.choice(alphabet) for _ in range(length))
        if code not in _urls:
            return code


def create_short_url(original_url: str) -> tuple[str, str]:
    short_code = _generate_short_code()
    _urls[short_code] = original_url
    return short_code, original_url
