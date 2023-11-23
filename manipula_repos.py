import requests
import base64

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token='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'
        self.headers = {'Authorization':"Bearer " + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}

    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Analise e exporte as linguagens de programação mais utilizadas nos repositórios da Amazon, Spotify e Netflix usando a API do GitHub. Explore as principais tecnologias dessas empresas líderes.",
            "private": False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", 
                                 json=data, headers=self.headers)

        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):

        # Codificando o arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": "Adicionando arquivos",
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')

# instanciando um objeto
novo_repo = ManipulaRepositorios('igorleonel')

# Criando o repositório
nome_repo = 'GitHubExplorer_Linguagens_de_Programacao_em_Empresas_Tech'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'dados_repos.py', '/home/igor/projeto_Requests/dados_repos.py')
novo_repo.add_arquivo(nome_repo, 'manipula_repos.py', '/home/igor/projeto_Requests/manipula_repos.py')
novo_repo.add_arquivo(nome_repo, 'linguagens_nubank.csv', '/home/igor/projeto_Requests/dados/linguagens_nubank.csv')


