"""
Script para corrigir usuários com senhas inválidas
Remove todos os usuários e cria novamente com senhas hasheadas corretamente
"""
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import User, UserRole
from utils.auth import get_password_hash


def fix_users():
    """
    Remove usuários antigos e cria novos com senhas hasheadas corretamente
    """
    print("🔧 Iniciando correção de usuários...")
    
    init_db()
    db: Session = SessionLocal()
    
    try:
        # Remove TODOS os usuários antigos (com senhas corrompidas)
        print("🗑️  Removendo usuários antigos...")
        deleted_count = db.query(User).delete()
        db.commit()
        print(f"✅ {deleted_count} usuários removidos!")
        
        # Cria novos usuários com senhas hasheadas CORRETAMENTE
        print("\n👤 Criando novos usuários...")
        
        # Admin
        admin = User(
            name="Admin GeekHaven",
            email="admin@geekhaven.com",
            password=get_password_hash("admin123"),  # Hash correto
            role=UserRole.ADMIN
        )
        db.add(admin)
        print("✅ Admin criado: admin@geekhaven.com / admin123")
        
        # Usuário teste
        test_user = User(
            name="Usuario Teste",
            email="user@test.com",
            password=get_password_hash("123456"),  # Hash correto
            role=UserRole.USER
        )
        db.add(test_user)
        print("✅ Usuário teste criado: user@test.com / 123456")
        
        db.commit()
        
        print("\n" + "="*60)
        print("🎉 USUÁRIOS CORRIGIDOS COM SUCESSO!")
        print("="*60)
        print("\n🔑 CREDENCIAIS:")
        print("   Admin: admin@geekhaven.com / admin123")
        print("   User: user@test.com / 123456")
        print("\n✅ Agora você pode fazer login normalmente!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    fix_users()
