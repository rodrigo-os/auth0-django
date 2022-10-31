README

1 - Clonar o Repositorio
2 - Acessar a pasta do projeto no VS
<h1>AppBiblioteca-01</h1>
3 - Acessar atraves do terminal a pasta AppBiblioteca-01 -> cd AppBiblioteca-01
4 - Criar o seu virtual Enviroment (Linux python3) (Window python) -> python3 -m venv env
5 - Ativalo -> . env/bin/activate
6 - Instalar as dependecias do projeto -> pip install -r requirements.txt
7 - criar um arquivo na raiz da pasta AppBiblioteca com o nome do virtual envirament, tendo um ponto (.) no inicio, ex: .env 
8 - Abrir o arquivo .env e realizar a seguinte alteração
	Definir as variaveis baseando-se nos parametros cedidos pelo site do auth0:
		APP_DOMAIN= siteAuth0->Domain(sem aspas) Ex. APP_DOMAIN=dev-f7rius332k4fgv61.us.auth0.com
		APP_CLIENT_ID= siteAuth0->Client ID(sem aspas)
		APP_CLIENT_SECRET= siteAuth0->Client Secret(sem aspas)
<h1>AppGaragem-02</h1>
9 - Acessar atraves do terminal a pasta AppGaragem-02 -> cd AppGaragem-02
10 - Criar o seu virtual Enviroment (Linux python3) (Window python) -> python3 -m venv env
11 - Ativalo -> . env/bin/activate
12 - Instalar as dependecias do projeto -> pip install -r requirements.txt
13 - criar um arquivo na raiz da pasta AppGaragem-02 com o nome do virtual envirament, tendo um ponto (.) no inicio, ex: .env 
14 - Abrir o arquivo .env e realizar a seguinte alteração
	Definir as variaveis baseando-se nos parametros cedidos pelo site do auth0:
		APP_DOMAIN= siteAuth0->Domain(sem aspas) Ex. APP_DOMAIN=dev-f7rius332k4fgv61.us.auth0.com
		APP_CLIENT_ID= siteAuth0->Client ID(sem aspas)
		APP_CLIENT_SECRET= siteAuth0->Client Secret(sem aspas)

<h1>Em ambos os apps</h1>
15 - Precisamos realizar as migrations -> python manage.py migrate
16 - Rodar os servidores
	python manage.py runserver localhost:8000
	python manage.py runserver localhost:5000
