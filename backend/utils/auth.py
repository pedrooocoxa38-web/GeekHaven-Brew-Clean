"""
Utilidades para autenticação JWT e criptografia de senha
"""
import os
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import hashlib
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import TokenData

# Configurações de segurança
SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-secreta-super-segura-mude-em-producao-2024")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 horas

# Contexto de criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")



def _sha256_digest(password: str) -> str:
    """Gera um hash SHA256 hexadecimal da senha (garante tamanho fixo para bcrypt)"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha corresponde ao hash usando SHA256 + bcrypt"""
    try:
        password_digest = _sha256_digest(plain_password)
        return pwd_context.verify(password_digest, hashed_password)
    except Exception as e:
        print(f"Erro ao verificar senha: {e}")
        return False


def get_password_hash(password: str) -> str:
    """Cria hash da senha usando SHA256 + bcrypt"""
    password_digest = _sha256_digest(password)
    return pwd_context.hash(password_digest)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Cria token JWT"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """Obtém o usuário atual a partir do token JWT"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    
    return user


async def get_current_admin_user(current_user: User = Depends(get_current_user)) -> User:
    """Verifica se o usuário atual é admin"""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas administradores podem acessar este recurso"
        )
    return current_user
