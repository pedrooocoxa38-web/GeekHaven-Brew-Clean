"""
Debug mais detalhado do problema de login
"""
import requests
import json
from passlib.context import CryptContext

API_BASE = "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host"

def detailed_login_test():
    """Teste mais detalhado do login"""
    print("🔐 Teste detalhado de login")
    print("-" * 40)
    
    # Dados de login
    login_data = {
        "email": "admin@geekhaven.com",
        "password": "admin123"
    }
    
    print(f"📝 Dados: {json.dumps(login_data, indent=2)}")
    
    try:
        # Faz a requisição
        response = requests.post(
            f"{API_BASE}/api/auth/login",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            json=login_data,
            timeout=10
        )
        
        print(f"📡 Status Code: {response.status_code}")
        print(f"📄 Headers: {dict(response.headers)}")
        
        # Tenta obter o conteúdo
        try:
            if response.headers.get('content-type', '').startswith('application/json'):
                data = response.json()
                print(f"📊 Response JSON: {json.dumps(data, indent=2)}")
            else:
                text = response.text
                print(f"📄 Response Text: {text}")
        except Exception as e:
            print(f"❌ Erro ao processar resposta: {e}")
            print(f"📄 Raw content: {response.content}")
        
        # Se deu erro 500, tenta entender o motivo
        if response.status_code == 500:
            print("\n🔍 ANÁLISE DO ERRO 500:")
            print("Possíveis causas:")
            print("1. Erro no hash da senha")
            print("2. Problema com dependências (jose, passlib)")
            print("3. Erro na query do banco de dados")
            print("4. Problema com o enum UserRole")
            print("5. Erro na geração do JWT")
            
        return response.status_code == 200
        
    except requests.exceptions.Timeout:
        print("❌ Timeout na requisição")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def test_password_hash():
    """Testa se conseguimos fazer hash da senha como o backend faria"""
    print("\n🔒 Teste de Hash de Senha")
    print("-" * 40)
    
    try:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
        password = "admin123"
        print(f"🔑 Senha original: {password}")
        
        # Trunca senha (como no backend)
        password_bytes = password.encode('utf-8')
        if len(password_bytes) > 72:
            password_bytes = password_bytes[:72]
        truncated_password = password_bytes.decode('utf-8', errors='ignore')
        
        print(f"✂️ Senha truncada: {truncated_password}")
        
        # Faz hash
        hashed = pwd_context.hash(truncated_password)
        print(f"🔐 Hash gerado: {hashed[:50]}...")
        
        # Verifica
        is_valid = pwd_context.verify(truncated_password, hashed)
        print(f"✅ Verificação: {is_valid}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste de hash: {e}")
        return False

def test_alternative_login():
    """Testa login com usuário alternativo"""
    print("\n👤 Teste com Usuário Alternativo")
    print("-" * 40)
    
    # Cria usuário teste
    register_data = {
        "name": "Debug User",
        "email": f"debug{int(requests.get(f'{API_BASE}/').elapsed.total_seconds() * 1000)}@test.com",
        "password": "123456"
    }
    
    print(f"📝 Criando usuário: {register_data['email']}")
    
    try:
        # Registra
        reg_response = requests.post(
            f"{API_BASE}/api/auth/register",
            headers={"Content-Type": "application/json"},
            json=register_data
        )
        
        print(f"📡 Registro Status: {reg_response.status_code}")
        
        if reg_response.status_code == 201:
            print("✅ Usuário criado!")
            
            # Tenta fazer login
            login_response = requests.post(
                f"{API_BASE}/api/auth/login",
                headers={"Content-Type": "application/json"},
                json={
                    "email": register_data["email"],
                    "password": register_data["password"]
                }
            )
            
            print(f"📡 Login Status: {login_response.status_code}")
            
            if login_response.status_code == 200:
                print("✅ Login com novo usuário funcionou!")
                data = login_response.json()
                print(f"🎫 Token: {data.get('access_token', 'N/A')[:20]}...")
                return True
            else:
                print("❌ Login com novo usuário falhou!")
                print(f"📄 Resposta: {login_response.text}")
        else:
            print(f"❌ Falha ao criar usuário: {reg_response.text}")
            
    except Exception as e:
        print(f"❌ Erro no teste alternativo: {e}")
    
    return False

if __name__ == "__main__":
    print("🚀 GeekHaven - Debug Detalhado de Login")
    print("=" * 50)
    
    # 1. Teste básico de hash
    test_password_hash()
    
    # 2. Teste detalhado de login
    detailed_login_test()
    
    # 3. Teste com usuário alternativo
    test_alternative_login()
    
    print("\n" + "=" * 50)
    print("🏁 Debug concluído!")