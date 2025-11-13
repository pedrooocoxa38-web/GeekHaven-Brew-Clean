"""
Script para criar usuário de teste manualmente
"""
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import User, UserRole
from utils.auth import get_password_hash

def create_test_user():
    """
    Cria um usuário de teste com senha hasheada corretamente
    """
    print("🔧 Criando usuário de teste...")
    
    init_db()
    db: Session = SessionLocal()
    
    try:
        # Remove usuário teste se existir
        existing_user = db.query(User).filter(User.email == "teste@mail.com").first()
        if existing_user:
            db.delete(existing_user)
            db.commit()
            print("✅ Usuário anterior removido!")
        
        # Cria novo usuário teste
        test_password = "senha123"
        hashed_password = get_password_hash(test_password)
        
        print(f"\n📝 Criando usuário:")
        print(f"   Email: teste@mail.com")
        print(f"   Senha: {test_password}")
        print(f"   Hash: {hashed_password[:60]}...")
        
        user = User(
            name="Usuario Teste Debug",
            email="teste@mail.com",
            password=hashed_password,
            role=UserRole.USER
        )
        db.add(user)
        db.commit()
        
        print("\n✅ Usuário criado com sucesso!")
        print("\n🔑 CREDENCIAIS PARA LOGIN:")
        print("   Email: teste@mail.com")
        print("   Senha: senha123")
        print("\n" + "="*60)
        
        # Verifica se a senha bate
        from utils.auth import verify_password
        is_valid = verify_password(test_password, hashed_password)
        print(f"🔐 Verificação de senha: {'✅ OK' if is_valid else '❌ FALHOU'}")
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    create_test_user()
