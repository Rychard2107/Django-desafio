
Django-desafio
1. Criando um ambiente virtual:

Comece criando um ambiente virtual isolado para o projeto. Isso garante que as dependências do projeto não interfiram com outras instalações em seu sistema.

Para criar o ambiente virtual, abra o terminal e navegue até a pasta do projeto. Em seguida, execute o seguinte comando:

python -m venv venv
Este comando cria um diretório chamado venv que contém o ambiente virtual.

2. Ativando o ambiente virtual:

Ative o ambiente virtual para que as ferramentas e bibliotecas instaladas nele sejam usadas.

Em sistemas Unix/Linux, execute:

source venv/bin/activate
Em Windows, execute:

venv\Scripts\activate.bat
3. Instalando as dependências:

Com o ambiente virtual ativado, você pode instalar as bibliotecas necessárias para o projeto.

Execute o seguinte comando no terminal:

pip install -r requirements.txt
Este comando lerá o arquivo requirements.txt e instalará todas as bibliotecas listadas nele.

4. Criando super usuário!

Execute o seguinte comando no terminal com tudo instalado:

python manage.py createsuperuser
Esse passo é para você ver algum usuário no seu campo de autor, quando você for criar novos animes,
já que ainda não está implementado a criação de usuários.
5. Pronto para começar!

Com o ambiente virtual configurado e as dependências instaladas, você está pronto para iniciar o projeto!
Execute o seguinte comando no terminal:

python manage.py runserver
Esse comando irá iniciar seu servidor do django e clicando no link você irá ser direcionado para home.

Na home você pode clicar em algumas coisas para direcionar a outros links, tais como criar anime, 
que fica na parte superior esquerda da pagina, direciona para um formulário para você criar seu anime.
A foto usada será armazenada em uma pasta 'media' com um name spacing, e a data da criação.

Ao clicar no nome do site que fica no centro da header irá retornar para a home.

Também há a opção de clicar no gênero que irá retonar todos os animes do gênero clicado.
Essa página contem um bug que não encontra a foto cadastrada por reutilização da home.html para economizar tempo.

Ao clicar no nome do anime ele deve renonar para uma página com os detalhes incluindo o resumo criado.
Essa página contem um bug não esperado que por falta de conhecimento não consegui resolver.

O plano inicial era implementar uma api chamada jikanpy, que iria retornar os animes no search localizado a direita da header,
não consegui implementar.
Coisas a melhorar:
  * Enfrentei muitos bugs relacionados as urls e views, e conflitos de nomes. Isso me custou tempo precioso, preciso estudar os conseitos básicos de cada arquivo e nomeação.
  * Aprender mais rápido lendo documentação.
  * Criação de testes.
  * Criar códigos com autenticações e melhorias de segurança.
 



