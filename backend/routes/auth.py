"""
Rotas de autenticação (Login, Registro, Profile)
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from database import get_db
from models import User, UserRole
from schemas import UserCreate, UserLogin, UserResponse, Token, UserUpdate, MessageResponse
from utils.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(prefix="/api/auth", tags=["Autenticação"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Registra um novo usuário
    """
    # Verifica se o email já existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    # Cria novo usuário
    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password,
        role=UserRole.USER
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Autentica usuário e retorna token JWT
    """
    # DEBUG: Log da tentativa de login
    print(f"🔐 Tentativa de login: {user_credentials.email}")
    print(f"   Tamanho da senha recebida: {len(user_credentials.password)} caracteres")
    
    # Busca usuário pelo email
    user = db.query(User).filter(User.email == user_credentials.email).first()
    
    if not user:
        print(f"❌ Usuário não encontrado: {user_credentials.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    print(f"✅ Usuário encontrado: {user.name} ({user.email})")
    print(f"   Hash no banco: {user.password[:60]}...")
    
    # Verifica senha
    password_valid = verify_password(user_credentials.password, user.password)
    print(f"   Verificação de senha: {'✅ OK' if password_valid else '❌ FALHOU'}")
    
    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Cria token JWT
    print(f"✅ Login bem-sucedido para: {user.email}")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    """
    Retorna informações do usuário autenticado
    """
    return current_user


@router.put("/profile", response_model=UserResponse)
async def update_profile(
    user_data: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Atualiza informações do usuário autenticado
    """
    if user_data.name:
        current_user.name = user_data.name
    
    if user_data.email:
        # Verifica se o novo email já está em uso
        existing_user = db.query(User).filter(
            User.email == user_data.email,
            User.id != current_user.id
        ).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email já está em uso"
            )
        current_user.email = user_data.email
    
    db.commit()
    db.refresh(current_user)
    
    return current_user


@router.post("/logout", response_model=MessageResponse)
async def logout(current_user: User = Depends(get_current_user)):
    """
    Logout (no JWT, o token é removido no frontend)
    """
    return {
        "message": "Logout realizado com sucesso",
        "detail": f"Até logo, {current_user.name}!"
    }
