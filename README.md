# pytest_tdd

# Índice
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Testes](#testes)
* [Ferramentas utilizadas](#ferramentas-utilizadas)
* [Linguagem de programação e Biblioteca utilizada](#linguagem-de-programação-e-biblioteca-utilizada)
* [Desenvolvedores do Projeto](#desenvolvedores)

# Descrição do projeto
pytest_tdd é um projeto de teste de unidade que realiza testes em uma classe que representa um funcionário de uma empresa. O teste contém vários métodos que testam diferentes cenários e comportamento da clase Funcionário, como:

# Testes
 - ✔️ `Teste 1`: Testa se a idade calculada está correta
 - ✔️ `Teste 2`: Testa se o sobrenome está sendo extraído corretamente
 - ✔️ `Teste 3`: Testa se o decréscimo do salário está sendo aplicado corretamente
 - ✔️ `Teste 4`: Testa se o cálculo do bonus está sendo realizado

# Ferramentas utilizadas
- `PyCharm`

# Linguagem de programação e Biblioteca utilizada
- `Python`
- `pytest`


# Abrir o projeto e realizar os testes
Após baixar o projeto, você pode abrir com o PyCharm. Para isso, na tela de launcher clique em:

- Open
- Procure o local onde o projeto está e o selecione (Caso o projeto seja baixado via zip, é necessário extraí-lo antes de procurá-lo)
- Por fim clique em OK

Se necessário, configure o Python interpreter e faça a instalação das bibliotecas incluídas no arquivo ```requirements.txt``` através do comando ```pip install -r requirements.txt```.  Feito isso, no terminal de comando, ative o ambiente virtual e execute os testes utilizando o comando ```pytest --cov```. Após a execução do comando, o relatório de testes será mostrado no terminal e irá incluir as informações sobre as linhas que não foram cobertas pelos testes. Se você deseja obter um relatório em HTML, execute o comando ```pytest --cov=codigo tests/ --cov-report html```, vá para diretório ```coverage_relatorio_html``` que foi criado na pastar raiz do projeto e abra o arquivo ```index.html``` usando um navegador da web.   



### É isso 🏆!
Fique a vontade para testar, modificar, adicionar e editar os testes! 

# Desenvolvedores

| [<img src="https://avatars.githubusercontent.com/u/48070981?s=400&v=4" width=115><br><sub>Thulio Carvalho</sub>](https://github.com/Thulio-FM-Carvalho) |  
| :---: |