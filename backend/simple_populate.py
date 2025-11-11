"""
Script simples para popular o banco com dados básicos
"""
import os
import sys

# Configurar DATABASE_URL antes de importar
os.environ['DATABASE_URL'] = 'postgresql://cafeteria_user:485b030a39acd60d5d65@geekhaven-brew_1_cafeteria-db:5432/cafeteria'

try:
    from database import SessionLocal, init_db, Base, engine
    from sqlalchemy import text
    
    print("🚀 Iniciando população simples do banco...")
    
    # Inicializa banco e CRIA TODAS AS TABELAS
    print("📋 Criando tabelas...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Limpar dados existentes (se existirem)
    print("🗑️ Limpando dados existentes...")
    try:
        db.execute(text("DELETE FROM users"))
        db.execute(text("DELETE FROM products"))
        db.commit()
        print("✅ Dados antigos removidos")
    except:
        print("ℹ️ Tabelas estavam vazias")
        db.rollback()
    
    # Inserir admin diretamente via SQL (sem hash complexo)
    print("👤 Criando usuário admin...")
    db.execute(text("""
        INSERT INTO users (name, email, password, role) 
        VALUES ('Admin', 'admin@geekhaven.com', 'admin123', 'admin')
    """))
    
    # Inserir produtos básicos
    print("📦 Criando produtos...")
    products_sql = """
        INSERT INTO products (name, description, price, image, category, stock) VALUES 
        ('Cappuccino Especial', 'Café premium com leite', 12.90, 'https://picsum.photos/400/300', 'Bebidas', 50),
        ('Brownie Gamer', 'Brownie de chocolate', 15.00, 'https://picsum.photos/400/301', 'Doces', 25),
        ('Energy Drink', 'Bebida energética', 8.50, 'https://picsum.photos/400/302', 'Bebidas', 30),
        ('Pizza Personal', 'Pizza individual', 28.90, 'https://picsum.photos/400/303', 'Comidas', 20)
    """
    db.execute(text(products_sql))
    
    # Confirmar mudanças
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