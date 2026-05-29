## Yuri Jardim Silveira

## Trabalho de Proxy com FILTRO DE PALAVRÕES


## Instalando dependências

'pip install flask requests'


## Configurando as listas

# words.json - Arquivo .json que contém as palavras que serão bloqueadas e substituídas

'
{
    "palavrao": "substituto"
}
'

# blocked.json - Arquivo .json que contém a lista de sites que são bloqueados pelo Proxy

'
{
    "bloqueados": [
        "https://sitebloqueado.com.br"
    ]
}
'

## Executando o Proxy no terminal

'flask run'