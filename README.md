# 🚗 Carro App - Deploy Profissional na AWS EC2
Este repositório documenta o processo de deploy da aplicação Django "Carro App" em uma infraestrutura AWS, utilizando servidores de alto desempenho (Nginx e uWSGI) e banco de dados PostgreSQL.
------------
## Projeto:
<img width="448" height="611" alt="image" src="https://github.com/user-attachments/assets/f6fbc616-9529-4787-b364-389a84deca32" />

## Ferramentas necessárias:
-SO -> De preferencia Linux
-Banco de Dados -> Tabela estruturada SQL
-Repositório Git
-Ambiente Python e uWSGI
-Servidor Web (Nginx)
-Provide AWS
--------------
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
```

## Configuração Django (settings.py)
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carros',
        'USER': 'postgres',
        'PASSWORD': '1989',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

🔑 2. Autenticação e Git (SSH)
Geração de chaves para deploy seguro e integração com GitHub para os usuários `ubuntu` e `root`.

```Bash
# Gerar chave
ssh-keygen -t ed25519 -C "seu-email@exemplo.com"

# Adicionar ao agente SSH
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Exibir chave pública
cat ~/.ssh/id_ed25519.pub

# Testar autenticação
ssh -T git@github.com
```

🐍 3. Ambiente Python e uWSGI
Isolamento do projeto e instalação do servidor de aplicação.

```Bash
# Dependências do sistema
sudo apt install build-essential python3-dev python3-venv python3-pip

# Configuração da venv e pacotes
cd /var/www/carro_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install uwsgi
```
# -------------- Intalação das independências do python --------------------
## Comandos para instalar dependências e ferramentas do Python:

````Python
sudo apt install build-essential python3
sudo apt install python3-dev
sudo apt install python3-venv
sudo apt install python3-pip
````

## Instalação da venv
1- python3 -m venv venv
2- source venv/bin/activate
3- pip install -r requirements.txt

# ----------- Instalação de modulo -----------
## Aplication server -> Faz o papel de tradutor entre o python com appweb
- Comando para instalar uWsgi:
1- pip install uwsgi

- Comando para rodar uWsgi:
1 -uwsgi --http :8000 --module app.wsgi --chmod-socket=666
# coração da apalicação (app.wsgi) wsgi é arquivo wsgi.py
2- --chmod-socket=666 -> permissões para executar socket sem restrição

## Comando para subir uWsgi com socket:
1- source venv/bin/activate
2- uwsgi --socket /var/www/carro_app/carros.sock --module app.wsgi --chmod-socket=666

## Comando para subir o uWsgi como ini:
- uwsgi --ini carros_uwsgi.ini


🌐 4. Servidor Web (Nginx)
Configuração do proxy reverso para gerenciar tráfego e arquivos estáticos.

Arquivo: `nano /etc/nginx/sites-available/carros.conf`

````Nginx
upstream django {
    server unix:///var/www/carro_app/carros.sock;
}

server {
    listen      8000; 
    server_name 3.217.200.23; # Elastic IP fixo associado
    charset     utf-8;

    client_max_body_size 75M;

    location /media  {
        alias /var/www/carro_app/media;
    }

    location /static {
        alias /var/www/carro_app/static;
    }

    location / {
        uwsgi_pass  django;
        include     /var/www/carro_app/uwsgi_params;
    }
}
````

⚙️ 5. Automação de Inicialização (Systemd)
Criação do serviço para garantir que a aplicação suba automaticamente com o servidor Linux.

Arquivo: nano/etc/systemd/system/carros.service
````Ini, TOML
[Unit]
Description=uWSGI instance to serve carros
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/var/www/carro_app
ExecStart=/var/www/carro_app/venv/bin/uwsgi --ini /var/www/carro_app/carros_uwsgi.ini

[Install]
WantedBy=multi-user.target
````

-Gerenciamento do serviço:
````
sudo systemctl daemon-reload
sudo systemctl start carros
sudo systemctl enable carros
sudo systemctl status carros
````
## Dica - habilitar a port 8000 no security group na regra inbound com TCP
## Permitir acesso na rede em nuvem
- ALLOWED_HOSTS = ['*']
- python3 manage.py migrate
- python3 manage.py runserver 0:8000
