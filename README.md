# GeekHaven Brew

Projeto de cafeteria geek com React + FastAPI

## Stack
- Frontend: React + TypeScript + Vite + Tailwind + shadcn-ui
- Backend: FastAPI + Python + SQLAlchemy + PostgreSQL
- Deploy: Easypanel com Docker

## Estrutura
- `/src` - Frontend React
- `/backend` - API FastAPI
- `/public` - Assets estáticos

## Como rodar
```bash
# Frontend
npm install
npm run dev

# Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```