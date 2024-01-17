from flask import Flask,request

from treino_routes.main import insertuser


app= Flask("nome_app")

@app.route("/olamundo", methods=['GET'])
def olamundo():
    return {'ola': 'mundo'}


@app.route('/cadastrar/usuario',methods=['POST'])
def method_name():
    """ return {'id':0} """
    body=request.get_json()
    
    if("name" not in body):
        return {"status": 400, "message":"o parametro nome nao foi inserido"}
    
    usuario = insertuser(body["nome"],body["email"],body["senha"])
    
    return usuario

def geraResponse(status,mensagem, nome_conteudo=False,conteudo=False):
    response={}
    response["status"]=status
    response["message"]=mensagem
    
    if(nome_conteudo and conteudo):
        responde[nome_conteudo]=conteudo
        



app.run()