"""
Script simples para popular o banco com dados básicos
"""
import os
import sys

# Configurar DATABASE_URL antes de importar
os.environ['DATABASE_URL'] = 'postgresql://cafeteria_user:485b030a39acd60d5d65@geekhaven-brew_1_cafeteria-db:5432/cafeteria'

try:
    from database import SessionLocal, Base, engine
    from models import User, Product, UserRole
    from sqlalchemy import text
    
    print("🚀 Iniciando população simples do banco...")
    
    # FORÇA criação de todas as tabelas
    print("📋 Criando tabelas...")
    Base.metadata.drop_all(bind=engine)  # Remove todas primeiro
    Base.metadata.create_all(bind=engine)  # Cria todas novamente
    print("✅ Tabelas criadas!")
    
    db = SessionLocal()
    
    # Criar usuário admin usando modelo ORM
    print("👤 Criando usuário admin...")
    admin = User(
        name="Admin",
        email="admin@geekhaven.com",
        password="admin123",  # Senha simples sem hash por enquanto
        role=UserRole.ADMIN
    )
    db.add(admin)
    
    # Criar produtos usando modelo ORM
    print("📦 Criando produtos...")
    products = [
        Product(
            name="Cappuccino Especial",
            description="Café premium com leite vaporizado",
            price=12.90,
            image="https://picsum.photos/400/300",
            category="Bebidas",
            stock=50
        ),
        Product(
            name="Brownie Gamer",
            description="Brownie artesanal com chocolate",
            price=15.00,
            image="https://picsum.photos/400/301",
            category="Doces",
            stock=25
        ),
        Product(
            name="Energy Drink Mix",
            description="Bebida energética importada",
            price=8.50,
            image="https://picsum.photos/400/302",
            category="Bebidas",
            stock=30
        ),
        Product(
            name="Pizza Personal",
            description="Pizza individual margherita",
            price=28.90,
            image="https://picsum.photos/400/303",
            category="Comidas",
            stock=20
        )
    ]
    
    for product in products:
        db.add(product)
    
    # Salvar tudo
    db.commit()
    
    print("✅ População concluída com sucesso!")
    print("🔑 Login: admin@geekhaven.com / admin123")
    print("📊 4 produtos criados")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    sys.exit(1)
finally:
    if 'db' in locals():
        db.close()