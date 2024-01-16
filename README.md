# Portal de Notícias

Esse projeto em Django foi feito para três disciplinas: Programação para Internet, Projeto de Desenvolvimento de Software e Fundamentos de sistemas operacionais e Sistemas operacionais de redes.

## Instalação

### Ambiente de produção

Para instalar o ambiente de produção, é necessário ter o Docker e o Docker Compose instalados. Após isso, basta executar o comando:

```bash
cp .env.prod.example .env.prod
```

```bash
cp .env.prod.db.example .env.prod.db
```

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

Após isso, o projeto estará rodando em `http://localhost:1337`