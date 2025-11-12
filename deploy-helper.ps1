# GeekHaven Brew - Scripts de Deploy e Teste
# PowerShell version

param(
    [string]$Command = "help"
)

function Show-Status {
    Write-Host "Status da Aplicacao:" -ForegroundColor Cyan
    Write-Host "Frontend: https://geekhaven-brew-1-cafeteria-front.a9negi.easypanel.host/" -ForegroundColor Green
    Write-Host "Backend: https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/" -ForegroundColor Green
    Write-Host "API Docs: https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/docs" -ForegroundColor Green
    Write-Host "Health: https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/health" -ForegroundColor Green
}

function Test-API {
    Write-Host "Testando conectividade da API..." -ForegroundColor Yellow
    
    Write-Host "1. Testando raiz do backend..." -ForegroundColor Cyan
    try {
        $response = Invoke-RestMethod -Uri "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/" -Method Get
        Write-Host ($response | ConvertTo-Json -Depth 3) -ForegroundColor Green
    } catch {
        Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host "2. Testando health check..." -ForegroundColor Cyan
    try {
        $response = Invoke-RestMethod -Uri "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/health" -Method Get
        Write-Host ($response | ConvertTo-Json -Depth 3) -ForegroundColor Green
    } catch {
        Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host "3. Testando produtos..." -ForegroundColor Cyan
    try {
        $response = Invoke-RestMethod -Uri "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api/products" -Method Get
        if ($response -and $response.Count) {
            Write-Host "Quantidade de produtos: $($response.Count)" -ForegroundColor Green
            Write-Host "Primeiro produto: $($response[0].name)" -ForegroundColor Green
        } else {
            Write-Host "Nenhum produto encontrado ou resposta vazia" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host "4. Testando auth endpoint..." -ForegroundColor Cyan
    try {
        $headers = @{ 'Content-Type' = 'application/json' }
        $body = @{ email = "test"; password = "test" } | ConvertTo-Json
        $response = Invoke-RestMethod -Uri "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api/auth/login" -Method Post -Headers $headers -Body $body
    } catch {
        if ($_.Exception.Response.StatusCode -eq 401) {
            Write-Host "Auth endpoint esta funcionando (retornou 401 como esperado)" -ForegroundColor Green
        } else {
            Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

function Test-CORS {
    Write-Host "Testando CORS..." -ForegroundColor Yellow
    try {
        $headers = @{
            'Origin' = 'https://geekhaven-brew-1-cafeteria-front.a9negi.easypanel.host'
            'Access-Control-Request-Method' = 'GET'
            'Access-Control-Request-Headers' = 'Content-Type'
        }
        $response = Invoke-WebRequest -Uri "https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api/products" -Method Options -Headers $headers
        Write-Host "CORS headers:" -ForegroundColor Green
        $response.Headers | ForEach-Object { Write-Host "$($_.Key): $($_.Value)" }
    } catch {
        Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
    }
}

function Build-Local {
    Write-Host "Fazendo build local..." -ForegroundColor Yellow
    npm install
    npm run build
    Write-Host "Build concluido!" -ForegroundColor Green
}

function Test-Local {
    Write-Host "Testando ambiente local..." -ForegroundColor Yellow
    
    # Verificar backend local
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/" -Method Get
        Write-Host "Backend local esta rodando" -ForegroundColor Green
        Write-Host ($response | ConvertTo-Json -Depth 2) -ForegroundColor Green
    } catch {
        Write-Host "Backend local nao esta rodando" -ForegroundColor Red
        Write-Host "Para iniciar: cd backend && python -m uvicorn app:app --reload" -ForegroundColor Yellow
    }
    
    # Verificar frontend local
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:5173/" -Method Head
        Write-Host "Frontend local esta rodando" -ForegroundColor Green
    } catch {
        Write-Host "Frontend local nao esta rodando" -ForegroundColor Red
        Write-Host "Para iniciar: npm run dev" -ForegroundColor Yellow
    }
}

function Test-FullTest {
    Write-Host "Teste completo..." -ForegroundColor Magenta
    Show-Status
    Test-API
    Test-CORS
}

function Show-Help {
    Write-Host "GeekHaven Brew - Scripts de Deploy e Teste" -ForegroundColor Cyan
    Write-Host "===========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Uso: .\deploy-helper.ps1 -Command <comando>" -ForegroundColor White
    Write-Host ""
    Write-Host "Comandos disponiveis:" -ForegroundColor Yellow
    Write-Host "  status      - Mostra URLs da aplicacao" -ForegroundColor White
    Write-Host "  test-api    - Testa endpoints da API" -ForegroundColor White
    Write-Host "  test-cors   - Testa configuracao CORS" -ForegroundColor White
    Write-Host "  build       - Faz build local" -ForegroundColor White
    Write-Host "  test-local  - Testa ambiente local" -ForegroundColor White
    Write-Host "  full-test   - Executa todos os testes" -ForegroundColor White
}

# Executar comando
switch ($Command.ToLower()) {
    "status" { Show-Status }
    "test-api" { Test-API }
    "test-cors" { Test-CORS }
    "build" { Build-Local }
    "test-local" { Test-Local }
    "full-test" { Test-FullTest }
    default { Show-Help }
}