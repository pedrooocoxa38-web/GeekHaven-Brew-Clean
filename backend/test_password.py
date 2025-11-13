"""
Script para testar hash e verificação de senha
"""
from utils.auth import get_password_hash, verify_password

# Teste com as senhas do sistema
test_passwords = [
    ("admin123", "senha do admin"),
    ("123456", "senha do user"),
]

print("🔐 TESTANDO HASH E VERIFICAÇÃO DE SENHA\n")
print("="*60)

for password, desc in test_passwords:
    print(f"\n📝 Testando: {desc}")
    print(f"   Senha original: {password}")
    
    # Gera hash
    hashed = get_password_hash(password)
    print(f"   Hash gerado: {hashed[:60]}...")
    
    # Verifica se o hash bate
    is_valid = verify_password(password, hashed)
    print(f"   ✅ Verificação: {'OK' if is_valid else '❌ FALHOU'}")
    
    # Testa senha errada
    is_invalid = verify_password("senha_errada_123", hashed)
    print(f"   ❌ Senha errada: {'BLOQUEADO' if not is_invalid else '⚠️ ACEITOU (ERRO!)'}")

print("\n" + "="*60)
print("✅ Teste concluído!")
