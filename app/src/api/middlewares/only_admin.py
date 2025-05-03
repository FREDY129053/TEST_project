from app.src.helpers.jwt import decode_jwt_token

from fastapi import Request, HTTPException, status

async def admin_required(request: Request):
  token = request.cookies.get("test")

  if not token:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")

  payload = decode_jwt_token(token)
  print(payload)
  if not payload.get("is_admin"):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")

  return payload