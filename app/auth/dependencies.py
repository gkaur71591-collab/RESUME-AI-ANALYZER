from jose import JWTError, jwt 
from fastapi import Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.config import settings
from app.database.database import get_db
from app.models.user import User

### This file will:
## Read the JWT token from the Authorization header.
##Decode and validate the token.
##Load the current user from the database.
##Make the authenticated user available to any protected endpoint.
##This keeps the logic reusable instead of repeating it in every route.

## Read the Bearer token from the Authorization header.
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

def current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)) -> User:
        # add exception code
        credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="credentials are not valid",
                headers={"WWW-Authenticate": "Bearer"},
        )

        try:
                payload = jwt.decode(
                        token,
                        settings.JWT_SECRET_KEY,
                        algorithms=[settings.JWT_ALGORITHM],
                )
                # We read the "sub" claim because it contains the user ID.
                user_id = payload.get("sub")
                if user_id is None:
                        raise credentials_exception
        except JWTError:
                raise credentials_exception

        # It is simpler and efficient for primary key lookups.
        user = db.get(User, int(user_id))
        if user is None:
                raise credentials_exception
        return user
