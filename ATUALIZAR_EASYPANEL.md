# 🚀 INSTRUÇÕES PARA ATUALIZAR NO EASYPANEL

## 📋 Resumo das Mudanças

✅ **Backend**: 51 produtos atualizados em 10 categorias  
✅ **Frontend**: Categorias sincronizadas com o banco de dados  
✅ **GitHub**: Código enviado para o repositório

---

## 🛠️ Como Atualizar no EasyPanel

### 1. **Acesse o Painel do EasyPanel**
- Entre no seu projeto GeekHaven Brew no EasyPanel

### 2. **Faça Pull do GitHub** 
- No terminal do container ou na interface do EasyPanel, execute:
```bash
git pull origin main
```

### 3. **Atualize o Backend (Python/FastAPI)**
- Acesse o terminal do container do backend
- Execute o script para atualizar produtos:
```bash
cd backend
python update_products_2024.py
```

### 4. **Reinicie os Serviços**
- Reinicie o serviço do **backend** (FastAPI)
- Reinicie o serviço do **frontend** (React/Vite)

### 5. **Teste a Aplicação**
- Acesse a URL do seu projeto
- Navegue até a página "Produtos"
- Verifique se as categorias aparecem corretamente

---

## 📦 Produtos Atualizados (51 itens)

### ☕ **Cafés Especiais** (5 produtos)
- Expresso Geralt - R$ 8,00
- Latte Tardis - R$ 14,00  
- Cappuccino Pantera Negra - R$ 14,00
- Mocha do Multiverso - R$ 16,00
- Café Master Chief - R$ 10,00

### 🍕 **Pizzas** (5 produtos)  
- Pizza Fire Flower - R$ 35,00
- Pizza Wakanda - R$ 50,00
- Pizza Hyrule - R$ 40,00
- Pizza Starfield - R$ 48,00
- Pizza Gotham - R$ 38,00

### 🥤 **Sucos** (5 produtos)
- Potion Verde - R$ 10,00
- Suco Cibernético - R$ 16,00
- Potion Rosa - R$ 12,00
- Elixir Tropical - R$ 14,00
- Suco Kamehameha - R$ 15,00

### 🍔 **Hambúrgueres** (5 produtos)
- Burger Ragnaros - R$ 22,00
- Boss Final - R$ 35,00
- Combo Pikachu - R$ 28,00
- Burger Jedi - R$ 30,00
- Burger Kratos - R$ 33,00

### 🍪 **Sobremesas** (5 produtos)
- Cookie Multiverso - R$ 12,00
- Brownie Infinity Gauntlet - R$ 18,00
- Torta da Princesa Peach - R$ 15,00
- Pudim Pokéball - R$ 13,00
- Milkshake Groot - R$ 16,00

### 🍟 **Snacks** (5 produtos)
- Batata Frita Player 1 - R$ 9,00
- Nachos do Multiverso - R$ 15,00
- Pipoca Arcade - R$ 10,00
- Anéis do Destino - R$ 12,00
- Combo XP+ - R$ 14,00

### 🥗 **Saladas** (5 produtos)
- Salada Jedi Mind Trick - R$ 18,00
- Salada Wakfu - R$ 28,00
- Salada Pixel Fresh - R$ 20,00
- Salada Lara Croft - R$ 24,00
- Salada Guardian - R$ 22,00

### 🥤 **Bebidas** (4 produtos)
- Coca-Cola Player Classic - R$ 7,00
- Soda Stark Industries - R$ 7,00
- Mana Potion - R$ 12,00
- Cyber Brew 2077 - R$ 12,00

### 🧸 **Bonecos e Colecionáveis** (7 produtos)
- Funko Pop! Kratos - R$ 149,90
- Funko Pop! Goku Super Saiyajin Blue - R$ 179,90
- Action Figure Spider-Man Miles Morales - R$ 299,90
- Estatueta The Witcher - Geralt em Batalha - R$ 249,90
- Funko Pop! Pikachu Feliz - R$ 139,90
- Action Figure Master Chief - R$ 269,90
- Estatueta Eleven - Stranger Things - R$ 199,90

### 🎲 **Jogos de Tabuleiro e Cartas** (5 produtos)
- Catan - O Jogo - R$ 149,90
- Ticket to Ride - Europa - R$ 219,90
- Dungeons & Dragons Starter Set - R$ 179,90
- Zombicide - 2ª Edição - R$ 359,90
- Exploding Kittens - Edição Geek - R$ 149,90

---

## 🔑 Credenciais de Acesso

**Admin:** admin@geekhaven.com / admin123  
**Usuario:** user@test.com / 123456

---

## ⚠️ Problemas Conhecidos

- **Login com erro 500**: Use o modo debug (VITE_DEBUG_MODE=true) enquanto corrigimos o backend
- **Imagens do Unsplash**: Todas otimizadas com auto=format para carregamento rápido

---

## 📞 Suporte

Se algo não funcionar:
1. Verifique os logs do EasyPanel  
2. Confirme se o git pull foi executado
3. Reinicie os serviços novamente
4. Teste a API diretamente: `[sua-url]/api/products`

**Atualização realizada em:** ${new Date().toLocaleString('pt-BR')}