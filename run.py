# responsavel pela execução do servidor
#camada controller recebe a requisição e retorna a resposta.
#model é responsavel por criar um modelo que vai para o banco de dados

from test_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)