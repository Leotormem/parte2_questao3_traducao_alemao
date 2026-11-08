# TP2 — Parte 2, Questão 3: Tradução Inglês–Alemão

## Descrição

Neste projeto desenvolvi uma API de tradução de inglês para alemão utilizando FastAPI, LangChain e o modelo Helsinki-NLP/opus-mt-en-de da Hugging Face.

A aplicação recebe um texto em inglês por meio de uma requisição HTTP e retorna sua tradução para o alemão em formato JSON.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- LangChain Core
- Hugging Face Transformers
- PyTorch
- Pydantic
- SentencePiece
- Sacremoses

## Estrutura do projeto

```text
parte2_questao3_traducao_alemao/
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Funcionamento

A aplicação utiliza a rota `POST /translate` para receber um texto em inglês.

O FastAPI recebe a requisição e o Pydantic valida os dados enviados.

O LangChain utiliza o componente RunnableLambda para executar a função Python responsável pela tradução.

Essa função utiliza o tokenizer e o modelo Helsinki-NLP/opus-mt-en-de da Hugging Face para gerar o texto em alemão.

A tradução é retornada ao usuário em formato JSON.

## Arquitetura da aplicação

```text
Usuário / Swagger UI
        |
        v
FastAPI - POST /translate
        |
        v
Pydantic - Validação da entrada
        |
        v
LangChain - RunnableLambda
        |
        v
Função Python de tradução
        |
        v
Hugging Face - Helsinki-NLP/opus-mt-en-de
        |
        v
Resposta JSON
```

## Instalação

Crie um ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Execução

Inicie o servidor:

```powershell
python -m uvicorn main:app --reload
```

Acesse o Swagger UI:

http://127.0.0.1:8000/docs

Na primeira execução, o modelo será baixado automaticamente da Hugging Face.

## Exemplo de utilização

Requisição POST /translate:

```json
{
  "text": "Hello, how are you today?"
}
```

Exemplo de resposta obtida:

```json
{
  "original_text": "Hello, how are you today?",
  "translated_text": "Hallo, wie geht's dir heute?",
  "source_language": "English",
  "target_language": "German"
}
```

## Testes realizados

Realizei três testes utilizando o Swagger UI:

1. Tradução de uma frase curta.
2. Tradução de um texto médio sobre Python.
3. Tradução de um texto longo sobre inteligência artificial.

Nos três testes, a aplicação retornou HTTP 200 e apresentou as traduções em alemão.

## Limitações

O modelo pode apresentar dificuldades com expressões idiomáticas, gírias e frases que dependem do contexto.

O processamento local também utiliza recursos do computador, como memória RAM e CPU.

Textos muito longos podem ultrapassar o limite de entrada configurado na aplicação e sofrer truncamento.

A integração com LangChain facilita a organização do fluxo, mas adiciona uma camada ao processamento.

Essas limitações serão discutidas com mais detalhes na Questão 5.

## Autor

Leonardo Luiz Tormem