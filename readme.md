# crewAI no Docker

Esse projeto visa fazer a utilização do crewAI usando Docker, sem ter que instalar e promovendo uma utilização segura sem impactar as bibiliotecas e facilitando o usos.

Esse projeto usa o crewAI, Docker e a biblioteca gradIO.


# Como usar

Segue passo a passo de como usar:

## Instale o Docker Desktop (Windows) ou alguma versão Linux.

Existem vários tutoriais explicando como instalar o docker.

## Crie uma pasta para seu projeto

Crie uma pasta para seu projeto e dentro dela crie uma pasta chamada **app**

## Baixe os arquivos desse repositório

Faça download dos arquivos e salve na pasta de seu projeto, atente para os arquivos dentro da pasta **app**.

## Ajuste sua chave da openAI

Dentro da pasta **app**, ajuste sua **API KEY** da openAI no arquivo `settings.py`

## Execute o comando para executar o container

Para baixar e ativar o container execute o comando:

    docker compose up

## Entre pelo navegador na página do gradio

Acesse o endereço do gradio:

[http://localhost:7860/](http://localhost:7860/)

ou para tema dark:

[http://localhost:7860/?__theme=dark](http://localhost:7860/?__theme=dark)