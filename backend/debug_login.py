"""
Script para verificar e forçar a criação do usuário admin
"""
import requests
import json

API_BASE = "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host"

def test_login():
    """Testa se consegue fazer login com as credenciais admin"""
    print("🔐 Testando login admin...")
    
    try:
        response = requests.post(
            f"{API_BASE}/api/auth/login",
            headers={"Content-Type": "application/json"},
            json={
                "email": "admin@geekhaven.com",
                "password": "admin123"
            }
        )
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Login funcionando!")
            data = response.json()
            print(f"Token: {data.get('access_token', 'N/A')}")
            return True
        else:
            print("❌ Login falhou!")
            return False
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return False

def create_admin_user():
    """Tenta criar o usuário admin"""
    print("👤 Criando usuário admin...")
    
    try:
        response = requests.post(
            f"{API_BASE}/api/auth/register",
            headers={"Content-Type": "application/json"},
            json={
                "name": "Administrator",
                "email": "admin@geekhaven.com", 
                "password": "admin123"
            }
        )
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 201:
            print("✅ Usuário admin criado!")
            return True
        else:
            print("⚠️ Usuário já existe ou houve erro")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao criar usuário: {e}")
        return False

def check_backend():
    """Verifica se o backend está funcionando"""
    print("🔍 Verificando backend...")
    
    try:
        response = requests.get(f"{API_BASE}/")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Backend online!")
            data = response.json()
            print(f"API: {data.get('message', 'N/A')}")
            return True
        else:
            print("❌ Backend com problemas!")
            return False
            
    except Exception as e:
        print(f"❌ Backend fora do ar: {e}")
        return False

def check_products():
    """Verifica se existem produtos"""
    print("📦 Verificando produtos...")
    
    try:
        response = requests.get(f"{API_BASE}/api/products")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ {len(data)} produtos encontrados!")
            
            # Lista categorias únicas
            categories = list(set(p.get('category', 'N/A') for p in data))
            print(f"📂 Categorias: {', '.join(categories)}")
            return True
        else:
            print("❌ Erro ao buscar produtos!")
            return False
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return False

if __name__ == "__main__":
    print("🚀 GeekHaven Brew - Diagnóstico e Correção")
    print("=" * 50)
    
    # 1. Verifica backend
    if not check_backend():
        print("❌ Backend não está funcionando. Pare por aqui.")
        exit(1)
    
    # 2. Verifica produtos  
    check_products()
    
    # 3. Testa login
    if not test_login():
        print("\n🔧 Login falhou. Tentando criar usuário admin...")
        create_admin_user()
        
        print("\n🔄 Testando login novamente...")
        if test_login():
            print("✅ Problema resolvido!")
        else:
            print("❌ Ainda há problemas. Verifique logs do backend.")
    else:
        print("✅ Login já está funcionando!")
    
    print("\n" + "=" * 50)
    print("🎯 Teste concluído!")