README

<p> 1 - Clonar o Repositorio </p>
<p> 2 - Acessar a pasta do projeto no VS </p>
<h1>AppBiblioteca-01</h1>
<ul>
<li> 3 - Acessar atraves do terminal a pasta AppBiblioteca-01 -> cd AppBiblioteca-01</li>
<li> 4 - Criar o seu virtual Enviroment (Linux python3) (Window python) -> python3 -m venv env</li>
<li> 5 - Ativalo -> . env/bin/activate</li>
<li> 6 - Instalar as dependecias do projeto -> pip install -r requirements.txt</li>
<li> 7 - criar um arquivo na raiz da pasta AppBiblioteca com o nome do virtual envirament, tendo um ponto (.) no inicio, ex: .env </li>
<li> 8 - Abrir o arquivo .env e realizar a seguinte alteração</li>
	<li> Definir as variaveis baseando-se nos parametros cedidos pelo site do auth0:</li>
		<li> APP_DOMAIN= siteAuth0->Domain(sem aspas) Ex. APP_DOMAIN=dev-f7rius332k4fgv61.us.auth0.com</li>
		<li>APP_CLIENT_ID= siteAuth0->Client ID(sem aspas)</li>
		<li>APP_CLIENT_SECRET= siteAuth0->Client Secret(sem aspas)</li>
</ul>
<ul>
<h1>AppGaragem-02</h1>
<li> 9 - Acessar atraves do terminal a pasta AppGaragem-02 -> cd AppGaragem-02</li>
<li> 10 - Criar o seu virtual Enviroment (Linux python3) (Window python) -> python3 -m venv env</li>
<li> 11 - Ativalo -> . env/bin/activate</li>
<li> 12 - Instalar as dependecias do projeto -> pip install -r requirements.txt</li>
<li> 13 - criar um arquivo na raiz da pasta AppGaragem-02 com o nome do virtual envirament, tendo um ponto (.) no inicio, ex: .env </li>
<li> 14 - Abrir o arquivo .env e realizar a seguinte alteração</li>
	<li> Definir as variaveis baseando-se nos parametros cedidos pelo site do auth0:</li>
		<li> APP_DOMAIN= siteAuth0->Domain(sem aspas) Ex. APP_DOMAIN=dev-f7rius332k4fgv61.us.auth0.com</li>
		<li> APP_CLIENT_ID= siteAuth0->Client ID(sem aspas)</li>
		<li> APP_CLIENT_SECRET= siteAuth0->Client Secret(sem aspas)</li>
</ul>

<h1>Em ambos os apps</h1>
<ul>
<li> 15 - Precisamos realizar as migrations -> python manage.py migrate</li>
<li> 16 - Rodar os servidores</li>
	<li> python manage.py runserver localhost:8000</li>
	<li> python manage.py runserver localhost:5000</li>
</ul>
