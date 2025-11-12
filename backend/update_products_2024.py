"""
Script para atualizar o banco de dados com a nova lista completa de produtos GeekHaven Brew 2024
"""
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import User, Product, UserRole
from utils.auth import get_password_hash


def update_products():
    """
    Atualiza o banco de dados com todos os produtos atualizados da GeekHaven Brew
    """
    print("🔄 Iniciando atualização dos produtos GeekHaven Brew 2024...")
    
    # Inicializa o banco
    init_db()
    
    db: Session = SessionLocal()
    
    try:
        # Verifica se ja existem usuarios, senao cria
        existing_users = db.query(User).count()
        if existing_users == 0:
            print("👤 Criando usuários...")
            # Cria usuario admin
            admin = User(
                name="Admin GeekHaven",
                email="admin@geekhaven.com",
                password=get_password_hash("admin123"),
                role=UserRole.ADMIN
            )
            db.add(admin)
            
            # Cria usuario teste
            test_user = User(
                name="Usuario Teste",
                email="user@test.com",
                password=get_password_hash("123456"),
                role=UserRole.USER
            )
            db.add(test_user)
            db.commit()
            print("✅ Usuários criados com sucesso!")
        
        # Remove produtos existentes para evitar duplicatas
        print("🗑️  Removendo produtos antigos...")
        db.query(Product).delete()
        db.commit()
        
        # Lista COMPLETA de produtos atualizados
        products = [
            # ===============================
            # CATEGORIA: CAFÉS 
            # ===============================
            Product(
                name="Expresso Geralt",
                description="Café forte e encorpado, perfeito para quem enfrenta monstros antes do nascer do sol.",
                price=8.00,
                image="https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=400&h=300&fit=crop&auto=format",
                category="Cafés Especiais",
                stock=50
            ),
            Product(
                name="Latte Tardis",
                description="Café com leite e espuma de baunilha, doce e imprevisível como uma viagem no tempo.",
                price=14.00,
                image="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&h=300&fit=crop&auto=format",
                category="Cafés Especiais",
                stock=50
            ),
            Product(
                name="Cappuccino Pantera Negra",
                description="Cappuccino com chocolate meio amargo e canela, nobre e intenso.",
                price=14.00,
                image="https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400&h=300&fit=crop&auto=format",
                category="Cafés Especiais",
                stock=50
            ),
            Product(
                name="Mocha do Multiverso",
                description="Mistura de café, chocolate e chantilly - cada gole abre uma nova dimensão.",
                price=16.00,
                image="https://images.unsplash.com/photo-1578314675249-a6910f80cc4e?w=400&h=300&fit=crop&auto=format",
                category="Cafés Especiais",
                stock=50
            ),
            Product(
                name="Café Master Chief",
                description="Café médio com toque de canela, energia para qualquer missão.",
                price=10.00,
                image="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400&h=300&fit=crop&auto=format",
                category="Cafés Especiais",
                stock=50
            ),
            
            # ===============================
            # CATEGORIA: PIZZAS
            # ===============================
            Product(
                name="Pizza Fire Flower",
                description="Calabresa com pimenta e queijo, dá um verdadeiro power-up de sabor.",
                price=35.00,
                image="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=30
            ),
            Product(
                name="Pizza Wakanda",
                description="Frango com catupiry e toque de curry - ousada e cheia de identidade.",
                price=50.00,
                image="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=25
            ),
            Product(
                name="Pizza Hyrule",
                description="Mussarela, tomate e manjericão - equilíbrio perfeito entre tradição e aventura.",
                price=40.00,
                image="https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=25
            ),
            Product(
                name="Pizza Starfield",
                description="Quatro queijos espaciais - um sabor fora deste mundo.",
                price=48.00,
                image="https://images.unsplash.com/photo-1458642849426-cfb724f15ef7?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=20
            ),
            Product(
                name="Pizza Gotham",
                description="Pepperoni e molho especial escuro - sabor sombrio e viciante.",
                price=38.00,
                image="https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400&h=300&fit=crop&auto=format",
                category="Pizzas",
                stock=25
            ),
            
            # ===============================
            # CATEGORIA: SUCOS
            # ===============================
            Product(
                name="Potion Verde",
                description="Suco de abacaxi com hortelã - restaura energia instantaneamente.",
                price=10.00,
                image="https://images.unsplash.com/photo-1622597467836-f3285f2131b8?w=400&h=300&fit=crop&auto=format",
                category="Sucos",
                stock=60
            ),
            Product(
                name="Suco Cibernético",
                description="Mistura de melancia e gengibre - refrescante com toque futurista.",
                price=16.00,
                image="https://images.unsplash.com/photo-1563227812-0ea4c22e6cc8?w=400&h=300&fit=crop&auto=format",
                category="Sucos",
                stock=60
            ),
            Product(
                name="Potion Rosa",
                description="Morango e limão - perfeito para recarregar o HP.",
                price=12.00,
                image="https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=400&h=300&fit=crop&auto=format",
                category="Sucos",
                stock=60
            ),
            Product(
                name="Elixir Tropical",
                description="Manga, maracujá e laranja - sabor vibrante de verão geek.",
                price=14.00,
                image="https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400&h=300&fit=crop&auto=format",
                category="Sucos",
                stock=60
            ),
            Product(
                name="Suco Kamehameha",
                description="Laranja com toque de gengibre - energia pura em um copo.",
                price=15.00,
                image="https://images.unsplash.com/photo-1600271889671-c685a53d2d4d?w=400&h=300&fit=crop&auto=format",
                category="Sucos",
                stock=60
            ),
            
            # ===============================
            # CATEGORIA: HAMBÚRGUERES
            # ===============================
            Product(
                name="Burger Ragnaros",
                description="Carne grelhada, cheddar e molho flamejante.",
                price=22.00,
                image="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop&auto=format",
                category="Hamburgueres",
                stock=40
            ),
            Product(
                name="Boss Final",
                description="200g de carne, bacon e molho secreto - desafio lendário.",
                price=35.00,
                image="https://images.unsplash.com/photo-1550547660-d9450f859349?w=400&h=300&fit=crop&auto=format",
                category="Hamburgueres",
                stock=35
            ),
            Product(
                name="Combo Pikachu",
                description="Hambúrguer de frango empanado com molho elétrico.",
                price=28.00,
                image="https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=400&h=300&fit=crop&auto=format",
                category="Hamburgueres",
                stock=40
            ),
            Product(
                name="Burger Jedi",
                description="Pão australiano, carne suculenta e molho equilibrado no lado da força.",
                price=30.00,
                image="https://images.unsplash.com/photo-1551782450-17144efb9c50?w=400&h=300&fit=crop&auto=format",
                category="Hamburgueres",
                stock=35
            ),
            Product(
                name="Burger Kratos",
                description="Hambúrguer duplo com molho de pimenta - o sabor da guerra.",
                price=33.00,
                image="https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=400&h=300&fit=crop&auto=format",
                category="Hamburgueres",
                stock=30
            ),
            
            # ===============================
            # CATEGORIA: SOBREMESAS
            # ===============================
            Product(
                name="Cookie Multiverso",
                description="Cookie gigante com gotas de chocolate - cada mordida abre uma nova dimensão.",
                price=12.00,
                image="https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=50
            ),
            Product(
                name="Brownie Infinity Gauntlet",
                description="Brownie com sorvete e calda quente - poder doce absoluto.",
                price=18.00,
                image="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=40
            ),
            Product(
                name="Torta da Princesa Peach",
                description="Cheesecake de morango delicado e nostálgico.",
                price=15.00,
                image="https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=45
            ),
            Product(
                name="Pudim Pokéball",
                description="Pudim de baunilha com calda de frutas vermelhas - doce e colecionável.",
                price=13.00,
                image="https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=50
            ),
            Product(
                name="Milkshake Groot",
                description="Milkshake de chocolate e amendoim - Eu sou doce.",
                price=16.00,
                image="https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=400&h=300&fit=crop&auto=format",
                category="Sobremesas",
                stock=45
            ),
            
            # ===============================
            # CATEGORIA: SNACKS
            # ===============================
            Product(
                name="Batata Frita Player 1",
                description="Batatas crocantes com cheddar e bacon - o início perfeito da rodada.",
                price=9.00,
                image="https://images.unsplash.com/photo-1518013431117-eb1465fa5752?w=400&h=300&fit=crop&auto=format",
                category="Snacks",
                stock=80
            ),
            Product(
                name="Nachos do Multiverso",
                description="Nachos com queijo e guacamole - sabor interdimensional.",
                price=15.00,
                image="https://images.unsplash.com/photo-1582169296194-e4d644c48063?w=400&h=300&fit=crop&auto=format",
                category="Snacks",
                stock=70
            ),
            Product(
                name="Pipoca Arcade",
                description="Pipoca amanteigada - clássica e nostálgica.",
                price=10.00,
                image="https://images.unsplash.com/photo-1578849278619-e73505e9610f?w=400&h=300&fit=crop&auto=format",
                category="Snacks",
                stock=90
            ),
            Product(
                name="Anéis do Destino",
                description="Onion rings crocantes - um sabor para governar todos.",
                price=12.00,
                image="https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&h=300&fit=crop&auto=format",
                category="Snacks",
                stock=75
            ),
            Product(
                name="Combo XP+",
                description="Mix de amendoim, batata e snacks - aumenta seu nível de energia.",
                price=14.00,
                image="https://images.unsplash.com/photo-1621939514649-280e2ee25f60?w=400&h=300&fit=crop&auto=format",
                category="Snacks",
                stock=65
            ),
            
            # ===============================
            # CATEGORIA: SALADAS
            # ===============================
            Product(
                name="Salada Jedi Mind Trick",
                description="Frango, alface e molho caesar - equilíbrio e leveza.",
                price=18.00,
                image="https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=30
            ),
            Product(
                name="Salada Wakfu",
                description="Grão-de-bico, abacate e tahine - nutritiva e mágica.",
                price=28.00,
                image="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=25
            ),
            Product(
                name="Salada Pixel Fresh",
                description="Mix de folhas e frutas - refrescante como um novo save.",
                price=20.00,
                image="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=30
            ),
            Product(
                name="Salada Lara Croft",
                description="Frango grelhado, quinoa e molho de limão - força e agilidade.",
                price=24.00,
                image="https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=25
            ),
            Product(
                name="Salada Guardian",
                description="Mix de proteínas e castanhas - sabor de proteção divina.",
                price=22.00,
                image="https://images.unsplash.com/photo-1467453678174-768ec283a940?w=400&h=300&fit=crop&auto=format",
                category="Saladas",
                stock=30
            ),
            
            # ===============================
            # CATEGORIA: BEBIDAS
            # ===============================
            Product(
                name="Coca-Cola Player Classic",
                description="O tradicional refrigerante do gamer raiz.",
                price=7.00,
                image="https://images.unsplash.com/photo-1554866585-cd94860890b7?w=400&h=300&fit=crop&auto=format",
                category="Bebidas",
                stock=100
            ),
            Product(
                name="Soda Stark Industries",
                description="Refrigerante cítrico com gás intenso - inovação líquida.",
                price=7.00,
                image="https://images.unsplash.com/photo-1581006852262-e4307cf6283a?w=400&h=300&fit=crop&auto=format",
                category="Bebidas",
                stock=100
            ),
            Product(
                name="Mana Potion",
                description="Energético azul - restaura mana instantaneamente.",
                price=12.00,
                image="https://images.unsplash.com/photo-1622543925917-763c34d1a86e?w=400&h=300&fit=crop&auto=format",
                category="Bebidas",
                stock=80
            ),
            Product(
                name="Cyber Brew 2077",
                description="Energético com sabor cítrico neon - estilo cyberpunk.",
                price=12.00,
                image="https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop&auto=format",
                category="Bebidas",
                stock=80
            ),
            
            # ===============================
            # CATEGORIA: BONECOS E COLECIONÁVEIS
            # ===============================
            Product(
                name="Funko Pop! Kratos - God of War",
                description="Boneco colecionável do lendário Deus da Guerra. Edição limitada com detalhes em alta qualidade.",
                price=149.90,
                image="https://images.unsplash.com/photo-1608889825103-eb5ed706fc64?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=15
            ),
            Product(
                name="Funko Pop! Goku Super Saiyajin Blue - Dragon Ball Super",
                description="Goku em sua forma mais poderosa. Item essencial para fãs de Dragon Ball.",
                price=179.90,
                image="https://images.unsplash.com/photo-1613836442253-f4c79d12e574?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=12
            ),
            Product(
                name="Action Figure Spider-Man Miles Morales - Marvel",
                description="Figure articulado de alta qualidade do Homem-Aranha do multiverso, com acessórios.",
                price=299.90,
                image="https://images.unsplash.com/photo-1608889476561-6242cfdbf622?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=8
            ),
            Product(
                name="Estatueta The Witcher - Geralt em Batalha",
                description="Estatueta premium de resina do bruxo Geralt de Rivia em pose de combate épica.",
                price=249.90,
                image="https://images.unsplash.com/photo-1612033448550-9d6f9c17f07d?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=10
            ),
            Product(
                name="Funko Pop! Pikachu Feliz - Pokemon",
                description="O Pokémon mais amado do mundo em versão Funko Pop adorável. Novo na caixa.",
                price=139.90,
                image="https://images.unsplash.com/photo-1613836442253-f4c79d12e574?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=20
            ),
            Product(
                name="Action Figure Master Chief - Halo Infinite",
                description="O lendário Spartan-117 em action figure detalhado com armadura Mjolnir Mark VI.",
                price=269.90,
                image="https://images.unsplash.com/photo-1611791483458-8715f3e4b0b8?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=7
            ),
            Product(
                name="Estatueta Eleven - Stranger Things",
                description="Estatueta colecionável da Eleven com detalhes incríveis da série Stranger Things.",
                price=199.90,
                image="https://images.unsplash.com/photo-1608889825103-eb5ed706fc64?w=400&h=300&fit=crop&auto=format",
                category="Bonecos e Colecionaveis",
                stock=11
            ),
            
            # ===============================
            # CATEGORIA: JOGOS DE TABULEIRO E CARTAS
            # ===============================
            Product(
                name="Catan - O Jogo",
                description="O clássico jogo de estratégia e negociação. Construa colônias e domine a ilha de Catan.",
                price=149.90,
                image="https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=12
            ),
            Product(
                name="Ticket to Ride - Europa",
                description="Viaje pela Europa construindo ferrovias neste jogo premiado e viciante.",
                price=219.90,
                image="https://images.unsplash.com/photo-1632501641765-e568d28b0015?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=10
            ),
            Product(
                name="Dungeons & Dragons Starter Set - Dragão da Montanha de Gelo",
                description="Kit inicial completo para começar sua aventura no mundo de D&D. Inclui dados e fichas.",
                price=179.90,
                image="https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=8
            ),
            Product(
                name="Zombicide - 2ª Edição",
                description="Sobreviva ao apocalipse zumbi neste jogo cooperativo cheio de ação e estratégia.",
                price=359.90,
                image="https://images.unsplash.com/photo-1632501641765-e568d28b0015?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=5
            ),
            Product(
                name="Exploding Kittens - Edição Geek",
                description="Jogo de cartas explosivo e hilário criado pelos autores de The Oatmeal.",
                price=149.90,
                image="https://images.unsplash.com/photo-1611891487976-1ab1a9e81d00?w=400&h=300&fit=crop&auto=format",
                category="Jogos de Tabuleiro e Cartas",
                stock=18
            ),
        ]
        
        # Adiciona todos os produtos
        print("📦 Adicionando produtos ao banco de dados...")
        for product in products:
            db.add(product)
        
        db.commit()
        
        print("\n🎉 ATUALIZAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f"\n📊 ESTATÍSTICAS:")
        print(f"   Total de produtos: {len(products)}")
        
        # Conta produtos por categoria
        categories = {}
        for product in products:
            if product.category not in categories:
                categories[product.category] = 0
            categories[product.category] += 1
        
        print(f"\n🗂️  PRODUTOS POR CATEGORIA:")
        for category, count in categories.items():
            print(f"   - {category}: {count} produtos")
        
        print(f"\n🔑 CREDENCIAIS DE ACESSO:")
        print(f"   Admin: admin@geekhaven.com / admin123")
        print(f"   Usuario: user@test.com / 123456")
        
        print(f"\n✅ Banco de dados atualizado e pronto para uso!")
        
    except Exception as e:
        print(f"❌ Erro ao atualizar banco de dados: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    update_products()