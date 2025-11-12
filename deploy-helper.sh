#!/bin/bash

echo "🚀 GeekHaven Brew - Scripts de Deploy e Teste"
echo "=============================================="

# Função para mostrar status
show_status() {
    echo "📊 Status da Aplicação:"
    echo "Frontend: https://geekhaven-brew-1-cafeteria-front.a9negi.easypanel.host/"
    echo "Backend: https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/"
    echo "API Docs: https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/docs"
    echo "Health: https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/health"
}

# Função para testar APIs
test_api() {
    echo "🧪 Testando conectividade da API..."
    
    echo "1. Testando raiz do backend..."
    curl -s https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/ | jq '.'
    
    echo "2. Testando health check..."
    curl -s https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/health | jq '.'
    
    echo "3. Testando produtos..."
    curl -s https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api/products | jq '. | length'
    
    echo "4. Testando auth endpoint..."
    curl -s -X POST https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api/auth/login \
         -H "Content-Type: application/json" \
         -d '{"email":"test","password":"test"}' | jq '.'
}

# Função para verificar CORS
test_cors() {
    echo "🔒 Testando CORS..."
    curl -s -I -X OPTIONS \
         -H "Origin: https://geekhaven-brew-1-cafeteria-front.a9negi.easypanel.host" \
         -H "Access-Control-Request-Method: GET" \
         -H "Access-Control-Request-Headers: Content-Type" \
         https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api/products
}

# Função para build local
build_local() {
    echo "🏗️ Fazendo build local..."
    npm install
    npm run build
    echo "✅ Build concluído!"
}

# Função para testar local
test_local() {
    echo "🏠 Testando ambiente local..."
    
    # Verificar se o backend local está rodando
    if curl -s http://localhost:8000/ > /dev/null; then
        echo "✅ Backend local está rodando"
        curl -s http://localhost:8000/ | jq '.'
    else
        echo "❌ Backend local não está rodando"
        echo "Para iniciar: cd backend && python -m uvicorn app:app --reload"
    fi
    
    # Verificar se o frontend local está rodando
    if curl -s http://localhost:5173/ > /dev/null; then
        echo "✅ Frontend local está rodando"
    else
        echo "❌ Frontend local não está rodando"
        echo "Para iniciar: npm run dev"
    fi
}

# Verificar argumentos
case "$1" in
    "status")
        show_status
        ;;
    "test-api")
        test_api
        ;;
    "test-cors")
        test_cors
        ;;
    "build")
        build_local
        ;;
    "test-local")
        test_local
        ;;
    "full-test")
        echo "🎯 Teste completo..."
        show_status
        test_api
        test_cors
        ;;
    *)
        echo "Uso: $0 {status|test-api|test-cors|build|test-local|full-test}"
        echo ""
        echo "Comandos disponíveis:"
        echo "  status      - Mostra URLs da aplicação"
        echo "  test-api    - Testa endpoints da API"
        echo "  test-cors   - Testa configuração CORS"
        echo "  build       - Faz build local"
        echo "  test-local  - Testa ambiente local"
        echo "  full-test   - Executa todos os testes"
        ;;
esac