# Projeto de Geração de Screenshots

Este projeto é um aplicativo web simples que permite aos usuários gerar screenshots de páginas web fornecendo uma URL. O projeto usa FastAPI para o backend, Selenium WebDriver para capturar screenshots, e Docker para empacotamento e implantação.

## Estrutura do Projeto

O projeto consiste em três arquivos principais:

- `app.py`: Este arquivo contém o código do servidor FastAPI que serve uma página da web com um formulário onde os usuários podem inserir uma URL.
- `script.py`: Este arquivo contém a função `take_screenshot`, que usa o Selenium WebDriver para capturar um screenshot de uma página web.
- `Dockerfile`: Este arquivo contém as instruções para construir uma imagem Docker para o projeto.

## Como Executar o Projeto

1. **Construir a Imagem Docker**:
    ```bash
    docker build -t screenshot-app .
    ```

2. **Executar o Container Docker**:
    ```bash
    docker run -d -p 7000:7000 screenshot-app
    ```

Agora, o aplicativo estará disponível em `http://localhost:7000`. Você pode acessar essa URL em um navegador web para usar o aplicativo.

![image](https://github.com/volneifilho/queroprint/assets/79425059/152c3214-fe77-4165-9998-a9b98b0173fe)


## Dependências

As principais dependências do projeto incluem:

- FastAPI
- Selenium
- GeckoDriver
- Firefox

As dependências do Python são listadas no arquivo `requirements.txt`. As dependências do sistema e o GeckoDriver são instalados através do `Dockerfile`.

## Contribuições

Contribuições para o projeto são bem-vindas. Sinta-se à vontade para abrir uma Issue ou criar um Pull Request no GitHub.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para mais detalhes.
