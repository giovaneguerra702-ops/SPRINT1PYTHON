# Challenge JOVI Python - EXPTECH

Aplicativo de terminal para organizar pastas de estudos, cadastrar PDFs e ler texto de imagens usando OCR.

## Requisitos

- Python instalado
- Imagens para leitura dentro da pasta `images`

## Instalação e execução

No terminal, na pasta do projeto, instale as dependências e inicie o aplicativo:

```bash
python -m pip install -r requirements.txt
python app.py
```

## Como usar

Escolha uma opção digitando o número correspondente no menu:

- **1:** exibe a explicação do projeto.
- **2:** cadastra uma pasta, com nome, matéria e quantidade de fotos.
- **3 e 4:** lista ou remove pastas cadastradas.
- **5:** cadastra um PDF informando seu nome e número de páginas.
- **6 e 7:** lista ou remove PDFs cadastrados.
- **8:** lê uma imagem com OCR. Coloque o arquivo em `images`, escolha a opção e informe o nome completo, incluindo a extensão, como `lousa.jpg`. O texto reconhecido é exibido na tela e o registro de uma página é adicionado à lista de PDFs.
- **9:** encerra o aplicativo.

Os cadastros são salvos nos arquivos `pastas.json` e `pdfs.json`. As opções de PDF registram informações no arquivo JSON.