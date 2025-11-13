"""
Script para adicionar novos valores ao enum orderstatus no PostgreSQL
"""
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("❌ DATABASE_URL não encontrada no .env")
    exit(1)

engine = create_engine(DATABASE_URL)

print("🔄 Adicionando novos valores ao enum orderstatus...")

try:
    with engine.connect() as conn:
        # Adicionar 'preparing' se não existir
        try:
            conn.execute(text("ALTER TYPE orderstatus ADD VALUE IF NOT EXISTS 'preparing'"))
            conn.commit()
            print("✅ Valor 'preparing' adicionado")
        except Exception as e:
            print(f"⚠️  'preparing' pode já existir: {e}")
        
        # Adicionar 'ready' se não existir
        try:
            conn.execute(text("ALTER TYPE orderstatus ADD VALUE IF NOT EXISTS 'ready'"))
            conn.commit()
            print("✅ Valor 'ready' adicionado")
        except Exception as e:
            print(f"⚠️  'ready' pode já existir: {e}")
        
        # Adicionar 'delivered' se não existir
        try:
            conn.execute(text("ALTER TYPE orderstatus ADD VALUE IF NOT EXISTS 'delivered'"))
            conn.commit()
            print("✅ Valor 'delivered' adicionado")
        except Exception as e:
            print(f"⚠️  'delivered' pode já existir: {e}")
        
        # Verificar valores do enum
        result = conn.execute(text("""
            SELECT e.enumlabel 
            FROM pg_enum e
            JOIN pg_type t ON e.enumtypid = t.oid
            WHERE t.typname = 'orderstatus'
            ORDER BY e.enumsortorder
        """))
        
        print("\n📋 Valores atuais do enum orderstatus:")
        for row in result:
            print(f"  - {row[0]}")
        
        print("\n✅ Migração concluída com sucesso!")

except Exception as e:
    print(f"❌ Erro durante migração: {e}")
    exit(1)
