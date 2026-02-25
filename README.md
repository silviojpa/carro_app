# 🚗 Carro App - Deploy Profissional na AWS EC2
Este repositório documenta o processo de deploy da aplicação Django "Carro App" em uma infraestrutura AWS, utilizando servidores de alto desempenho (Nginx e uWSGI) e banco de dados PostgreSQL.
---
## Projeto:
<img width="448" height="611" alt="image" src="https://github.com/user-attachments/assets/f6fbc616-9529-4787-b364-389a84deca32" />
## Ferramentas necessárias:
- SO -> De preferencia Linux
- Banco de Dados -> Tabela estruturada SQL
- Repositório Git
- Ambiente Python e uWSGI
- Servidor Web (Nginx)
- Provide AWS
---
Fluxiograma 
<img width="915" height="368" alt="image" src="https://github.com/user-attachments/assets/686975fb-4bd3-45cf-b39a-fc349b3c0535" />
<img width="800" height="465" alt="image" src="https://github.com/user-attachments/assets/32df8c9c-6142-43f3-bc30-16b82f9ecefb" />

## 🛠️ 1. Banco de Dados (PostgreSQL)

Configuração do ambiente de banco de dados relacional diretamente na instância EC2.

### Instalação e Criação
```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Acessar Shell do Postgres
sudo -u postgres psql

# Comandos de criação
CREATE DATABASE carros;
ALTER USER postgres WITH PASSWORD '1989';
````


# Dica - habilitar a port 8000 no security group na regra inbound com TCP

# Permitir acesso na rede em nuvem
ALLOWED_HOSTS = ['*']
python3 manage.py migrate
python3 manage.py runserver 0:8000
