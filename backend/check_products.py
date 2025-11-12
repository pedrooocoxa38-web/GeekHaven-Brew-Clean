"""
Script para VERIFICAR os produtos atuais no banco de dados
Use este script para descobrir quais produtos estão realmente salvos
"""
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Product


def check_products():
    """
    Verifica e exibe todos os produtos no banco de dados
    """
    print("\n" + "="*70)
    print("🔍 VERIFICANDO PRODUTOS NO BANCO DE DADOS")
    print("="*70)
    
    init_db()
    db: Session = SessionLocal()
    
    try:
        # Busca todos os produtos
        products = db.query(Product).all()
        
        print(f"\n📊 TOTAL DE PRODUTOS: {len(products)}")
        
        # Agrupa por categoria
        categories = {}
        for product in products:
            if product.category not in categories:
                categories[product.category] = []
            categories[product.category].append(product)
        
        print(f"\n📁 TOTAL DE CATEGORIAS: {len(categories)}")
        print("\n" + "-"*70)
        
        # Exibe produtos por categoria
        for category_name in sorted(categories.keys()):
            products_in_category = categories[category_name]
            print(f"\n🗂️  {category_name} ({len(products_in_category)} produtos)")
            print("-"*70)
            for product in products_in_category:
                print(f"   • {product.name} - R$ {product.price:.2f}")
                print(f"     Estoque: {product.stock} | ID: {product.id}")
        
        print("\n" + "="*70)
        print("✅ VERIFICAÇÃO CONCLUÍDA!")
        print("="*70)
        
        # Verifica se são os produtos antigos ou novos
        print("\n🔎 ANÁLISE:")
        if "Cafés Especiais" in categories:
            print("   ⚠️  PRODUTOS ANTIGOS DETECTADOS!")
            print("   ⚠️  Para atualizar, execute: python update_products_final.py")
        elif "Cafés e Bebidas" in categories:
            print("   ✅ PRODUTOS NOVOS DETECTADOS!")
            print("   ✅ Banco de dados está atualizado!")
        else:
            print("   ❓ Estrutura de produtos desconhecida")
        
        print("\n")
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    check_products()
