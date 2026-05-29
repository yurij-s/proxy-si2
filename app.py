#Importando as bibliotecas.
from flask import Flask, render_template, Response
import requests
import json
import re

app = Flask(__name__)

#Lendo o arquivo words.json
with open("words.json", "r") as fileWords:
    palavroes: dict = json.load(fileWords)

with open('blocked.json', 'r') as blockeds:
    bloqueados: list = json.load(blockeds)['bloqueados']


#Função que substitui os palavrões.
def substitui(palavra): 
    for palavrao, substituto in palavroes.items():
        '''
        palavrao -> o que procurar,
        substituto -> o que colocar no lugar,
        palavra -> o texto onde procurar,
        IGNORECASE -> ignora maiusculas e minusculas.
        '''
        palavra = re.sub(palavrao, substituto, palavra, flags=re.IGNORECASE)
    return palavra

#Rota Home para estética.
@app.route('/')
def home():
    return render_template('home.html')

#Rota que vai aparecer o site
@app.route('/<path:url>')
def proxy(url):
    
    if url not in bloqueados: #Lógica pra verificar se o site está na lista de bloqueados:
        
        headers = {'User-Agent': 'Mozilla/5.0'}  #Esse headers foi necessario IA (Pra conseguir abrir o HTML da página).

        r = requests.get(url, headers=headers) #Aqui ele está buscando o site.
        
        content_type = r.headers.get("Content-Type", "") # Pega o Header, que diz o tipo de conteúdo do site.

        if "text" in content_type or "javascript" in content_type:
            conteudo = substitui(r.text) # Filtra os palavrões.
            return Response(conteudo, status=r.status_code, content_type=content_type) # Empacota e envia ao Browser.
        
        return Response(r.content, status=r.status_code, content_type=content_type)
    
    else: # Caso ele esteja na lista de sites bloqueados ele retorna a página HTML de bloqueio.
        return render_template('pagina_bloqueado.html', url=url)


if __name__ == "__main__":
    app.run(debug=True)