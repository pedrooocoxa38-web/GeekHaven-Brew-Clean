"""
Script FINAL para atualizar produtos GeekHaven Brew com estrutura EXATA solicitada
"""
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import User, Product, UserRole
from utils.auth import get_password_hash


def update_products_final():
    """
    Atualiza o banco com a lista EXATA de produtos solicitada
    """
    print("🔄 Iniciando atualização FINAL dos produtos...")
    
    init_db()
    db: Session = SessionLocal()
    
    try:
        # Cria usuários se não existirem
        existing_users = db.query(User).count()
        if existing_users == 0:
            print("👤 Criando usuários...")
            admin = User(
                name="Admin GeekHaven",
                email="admin@geekhaven.com",
                password=get_password_hash("admin123"),
                role=UserRole.ADMIN
            )
            db.add(admin)
            
            test_user = User(
                name="Usuario Teste",
                email="user@test.com",
                password=get_password_hash("123456"),
                role=UserRole.USER
            )
            db.add(test_user)
            db.commit()
            print("✅ Usuários criados!")
        
        # REMOVE TODOS OS PRODUTOS ANTIGOS
        print("🗑️  Removendo TODOS os produtos antigos...")
        db.query(Product).delete()
        db.commit()
        print("✅ Produtos antigos removidos!")
        
        # LISTA EXATA DE PRODUTOS SOLICITADA
        products = [
            # ==========================================
            # CATEGORIA: Cafés e Bebidas (7 produtos)
            # ==========================================
            Product(
                name="Café Respawn",
                description="Espresso intenso com notas de cacau, perfeito para reviver o ânimo em segundos.",
                price=9.90,
                image="https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=100
            ),
            Product(
                name="Mocha Mana Potion",
                description="Café com chocolate e chantilly azul, restaura sua mana instantaneamente.",
                price=14.90,
                image="https://images.unsplash.com/photo-1578314675249-a6910f80cc4e?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=100
            ),
            Product(
                name="Cappuccino XP Boost",
                description="Cappuccino com canela e toque de baunilha, energia +50 garantida.",
                price=12.90,
                image="https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=100
            ),
            Product(
                name="Latte Cyber Brew",
                description="Café com leite e espuma de baunilha, sabor suave e futurista.",
                price=13.90,
                image="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=100
            ),
            Product(
                name="Milkshake Critical Hit",
                description="Sorvete de baunilha com calda de caramelo e chantilly.",
                price=16.90,
                image="https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=80
            ),
            Product(
                name="Energético Power Up",
                description="Mistura cítrica exclusiva, ideal para entrar em modo hardcore.",
                price=11.90,
                image="https://images.unsplash.com/photo-1622543925917-763c34d1a86e?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=120
            ),
            Product(
                name="Refrigerante 8-Bit Cola",
                description="Refrescante e nostálgico, com rótulo pixelado exclusivo.",
                price=8.90,
                image="https://images.unsplash.com/photo-1554866585-cd94860890b7?w=400&h=300&fit=crop&auto=format",
                category="Cafés e Bebidas",
                stock=150
            ),
            
            # ==========================================
            # CATEGORIA: Pizzas (5 produtos)
            # ==========================================
            Product(
                name="Pizza Fire Flower",
                description="Calabresa com pimenta e queijo derretido. Um verdadeiro power-up de sabor.",
                price=39.90,
                image="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=40
            ),
            Product(
                name="Pizza Wakanda",
                description="Frango com catupiry e toque de curry. Ousada e cheia de identidade.",
                price=49.90,
                image="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=35
            ),
            Product(
                name="Pizza Hyrule",
                description="Mussarela, tomate e manjericão. Equilíbrio perfeito entre tradição e aventura.",
                price=44.90,
                image="https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=35
            ),
            Product(
                name="Pizza Gotham",
                description="Pepperoni e molho especial escuro. Um sabor sombrio e viciante.",
                price=42.90,
                image="https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=35
            ),
            Product(
                name="Pizza Starfield",
                description="Quatro queijos espaciais, um sabor fora deste mundo.",
                price=48.90,
                image="https://images.unsplash.com/photo-1458642849426-cfb724f15ef7?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=30
            ),
            
            # ==========================================
            # CATEGORIA: Hambúrgueres (5 produtos)
            # ==========================================
            Product(
                name="Burger Ragnaros",
                description="Carne grelhada, cheddar e molho flamejante. O sabor do fogo e da glória.",
                price=26.90,
                image="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop&auto=format",
                category="Hambúrgueres",
                stock=50
            ),
            Product(
                name="Boss Final",
                description="200g de carne, bacon e molho secreto. Desafio lendário de sabor.",
                price=35.00,
                image="https://images.unsplash.com/photo-1550547660-d9450f859349?w=400&h=300&fit=crop&auto=format",
                category="Hambúrgueres",
                stock=45
            ),
            Product(
                name="Combo Pikachu",
                description="Hambúrguer de frango empanado com molho elétrico e batatas.",
                price=29.90,
                image="https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=400&h=300&fit=crop&auto=format",
                category="Hambúrgueres",
                stock=50
            ),
            Product(
                name="Burger Jedi",
                description="Pão australiano, carne suculenta e molho equilibrado no lado da Força.",
                price=32.00,
                image="https://images.unsplash.com/photo-1551782450-17144efb9c50?w=400&h=300&fit=crop&auto=format",
                category="Hambúrgueres",
                stock=45
            ),
            Product(
                name="Burger Kratos",
                description="Hambúrguer duplo com molho de pimenta. O sabor da guerra.",
                price=34.90,
                image="https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=400&h=300&fit=crop&auto=format",
                category="Hambúrgueres",
                stock=40
            ),
            
            # ==========================================
            # CATEGORIA: Sobremesas (5 produtos)
            # ==========================================
            Product(
                name="Cookie Multiverso",
                description="Cookie gigante com gotas de chocolate. Cada mordida abre uma nova dimensão.",
                price=11.90,
                image="https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=60
            ),
            Product(
                name="Brownie Infinity Gauntlet",
                description="Brownie com sorvete e calda quente. Poder doce absoluto.",
                price=18.90,
                image="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=55
            ),
            Product(
                name="Torta da Princesa Peach",
                description="Cheesecake de morango delicado e nostálgico.",
                price=15.00,
                image="https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=50
            ),
            Product(
                name="Pudim Pokéball",
                description="Pudim de baunilha com calda de frutas vermelhas. Doce e colecionável.",
                price=13.90,
                image="https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=55
            ),
            Product(
                name="Milkshake Groot",
                description="Milkshake de chocolate e amendoim. Eu sou doce.",
                price=16.90,
                image="https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=50
            ),
            
            # ==========================================
            # CATEGORIA: Sucos e Poções (5 produtos)
            # ==========================================
            Product(
                name="Potion Verde",
                description="Suco de abacaxi com hortelã, restaura energia instantaneamente.",
                price=10.90,
                image="https://images.unsplash.com/photo-1622597467836-f3285f2131b8?w=400&h=300&fit=crop&auto=format",
                category="Sucos e Poções",
                stock=70
            ),
            Product(
                name="Potion Rosa",
                description="Morango e limão, perfeito para recarregar o HP.",
                price=12.90,
                image="https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=400&h=300&fit=crop&auto=format",
                category="Sucos e Poções",
                stock=70
            ),
            Product(
                name="Elixir Tropical",
                description="Manga, maracujá e laranja. Sabor vibrante de verão geek.",
                price=13.90,
                image="https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400&h=300&fit=crop&auto=format",
                category="Sucos e Poções",
                stock=65
            ),
            Product(
                name="Suco Cibernético",
                description="Melancia com gengibre, refrescante com toque futurista.",
                price=14.90,
                image="https://images.unsplash.com/photo-1563227812-0ea4c22e6cc8?w=400&h=300&fit=crop&auto=format",
                category="Sucos e Poções",
                stock=65
            ),
            Product(
                name="Suco Kamehameha",
                description="Laranja com toque de gengibre, energia pura em um copo.",
                price=15.90,
                image="https://images.unsplash.com/photo-1600271889671-c685a53d2d4d?w=400&h=300&fit=crop&auto=format",
                category="Sucos e Poções",
                stock=65
            ),
            
            # ==========================================
            # CATEGORIA: Snacks e Aperitivos (5 produtos)
            # ==========================================
            Product(
                name="Batata Frita Player 1",
                description="Batatas crocantes com cheddar e bacon. O início perfeito da rodada.",
                price=9.90,
                image="https://images.unsplash.com/photo-1518013431117-eb1465fa5752?w=400&h=300&fit=crop&auto=format",
                category="Snacks e Aperitivos",
                stock=90
            ),
            Product(
                name="Nachos do Multiverso",
                description="Nachos com queijo e guacamole. Sabor interdimensional.",
                price=14.90,
                image="https://images.unsplash.com/photo-1582169296194-e4d644c48063?w=400&h=300&fit=crop&auto=format",
                category="Snacks e Aperitivos",
                stock=80
            ),
            Product(
                name="Pipoca Arcade",
                description="Pipoca amanteigada, clássica e nostálgica.",
                price=8.90,
                image="https://images.unsplash.com/photo-1578849278619-e73505e9610f?w=400&h=300&fit=crop&auto=format",
                category="Snacks e Aperitivos",
                stock=100
            ),
            Product(
                name="Anéis do Destino",
                description="Onion rings crocantes, um sabor para governar todos.",
                price=11.90,
                image="https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&h=300&fit=crop&auto=format",
                category="Snacks e Aperitivos",
                stock=85
            ),
            Product(
                name="Combo XP+",
                description="Mix de amendoim, batata e snacks. Aumenta seu nível de energia.",
                price=12.90,
                image="https://images.unsplash.com/photo-1621939514649-280e2ee25f60?w=400&h=300&fit=crop&auto=format",
                category="Snacks e Aperitivos",
                stock=75
            ),
            
            # ==========================================
            # CATEGORIA: Saladas (5 produtos)
            # ==========================================
            Product(
                name="Salada Jedi Mind Trick",
                description="Frango, alface e molho caesar. Equilíbrio e leveza.",
                price=18.90,
                image="https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=40
            ),
            Product(
                name="Salada Wakfu",
                description="Grão-de-bico, abacate e tahine. Nutritiva e mágica.",
                price=27.90,
                image="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=35
            ),
            Product(
                name="Salada Pixel Fresh",
                description="Mix de folhas e frutas. Refrescante como um novo save.",
                price=21.90,
                image="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=40
            ),
            Product(
                name="Salada Lara Croft",
                description="Frango grelhado, quinoa e molho de limão. Força e agilidade.",
                price=24.90,
                image="https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=35
            ),
            Product(
                name="Salada Guardian",
                description="Mix de proteínas e castanhas. Sabor de proteção divina.",
                price=22.90,
                image="https://images.unsplash.com/photo-1467453678174-768ec283a940?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=40
            ),
            
            # ==========================================
            # CATEGORIA: Colecionáveis e Action Figures (7 produtos)
            # ==========================================
            Product(
                name="Funko Pop! Kratos — God of War",
                description="Edição limitada com detalhes incríveis.",
                price=149.90,
                image="https://images.unsplash.com/photo-1608889825103-eb5ed706fc64?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=15
            ),
            Product(
                name="Funko Pop! Goku Super Saiyajin Blue",
                description="Dragon Ball Super — Item essencial para fãs.",
                price=179.90,
                image="https://images.unsplash.com/photo-1613836442253-f4c79d12e574?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=12
            ),
            Product(
                name="Action Figure Spider-Man (Miles Morales)",
                description="Figura articulada premium com acessórios.",
                price=299.90,
                image="https://images.unsplash.com/photo-1608889476561-6242cfdbf622?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=8
            ),
            Product(
                name="Estatueta The Witcher — Geralt em Batalha",
                description="Resina detalhada em pose épica.",
                price=249.90,
                image="https://images.unsplash.com/photo-1612033448550-9d6f9c17f07d?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=10
            ),
            Product(
                name="Funko Pop! Pikachu Feliz",
                description="Pokémon — O Pokémon mais amado em versão colecionável.",
                price=139.90,
                image="https://images.unsplash.com/photo-1613836442253-f4c79d12e574?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=20
            ),
            Product(
                name="Action Figure Master Chief — Halo Infinite",
                description="Armadura Mjolnir Mark VI com detalhes fiéis.",
                price=269.90,
                image="https://images.unsplash.com/photo-1611791483458-8715f3e4b0b8?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=7
            ),
            Product(
                name="Estatueta Eleven — Stranger Things",
                description="Réplica detalhada da personagem.",
                price=199.90,
                image="https://images.unsplash.com/photo-1608889825103-eb5ed706fc64?w=400&h=300&fit=crop&auto=format",
                category="Colecionáveis e Action Figures",
                stock=11
            ),
            
            # ==========================================
            # CATEGORIA: Jogos de Tabuleiro e Cartas (5 produtos)
            # ==========================================
            Product(
                name="Catan — O Jogo",
                description="Clássico de estratégia e negociação. Domine a ilha de Catan.",
                price=149.90,
                image="https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=12
            ),
            Product(
                name="Ticket to Ride — Europa",
                description="Viaje construindo ferrovias pelo velho continente.",
                price=219.90,
                image="https://images.unsplash.com/photo-1632501641765-e568d28b0015?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=10
            ),
            Product(
                name="Dungeons & Dragons Starter Set — Dragão da Montanha de Gelo",
                description="Kit completo para iniciar sua campanha.",
                price=179.90,
                image="https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=8
            ),
            Product(
                name="Zombicide — 2ª Edição",
                description="Sobreviva ao apocalipse zumbi em equipe.",
                price=359.90,
                image="https://images.unsplash.com/photo-1632501641765-e568d28b0015?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=5
            ),
            Product(
                name="Exploding Kittens — Edição Geek",
                description="Jogo de cartas explosivo e hilário.",
                price=129.90,
                image="https://images.unsplash.com/photo-1611891487976-1ab1a9e81d00?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=18
            ),
        ]
        
        # Adiciona todos os produtos
        print(f"📦 Adicionando {len(products)} produtos ao banco...")
        for product in products:
            db.add(product)
        
        db.commit()
        
        # Conta produtos por categoria
        categories = {}
        for product in products:
            if product.category not in categories:
                categories[product.category] = 0
            categories[product.category] += 1
        
        print("\n" + "="*60)
        print("🎉 ATUALIZAÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*60)
        print(f"\n📊 TOTAL: {len(products)} produtos")
        print(f"\n🗂️  PRODUTOS POR CATEGORIA:")
        for category, count in sorted(categories.items()):
            print(f"   ✓ {category}: {count} produtos")
        
        print(f"\n🔑 CREDENCIAIS:")
        print(f"   Admin: admin@geekhaven.com / admin123")
        print(f"   User: user@test.com / 123456")
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    update_products_final()
