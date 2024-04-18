@app.route("/enviar_mensagem", methods=['POST'])
def enviar_mensagem():
    if request.method == 'POST':
        telefone_destinatario = request.json["telefone_destinatario"]
        mensagem = request.json["mensagem"]

        nome_usuario = session["usuario_logado"]["nome"]
        telefone_usuario = session["usuario_logado"]["telefone"]
        chat = Chat(nome_usuario, telefone_usuario)

        destinatario = Contato("", telefone_destinatario)
        enviado = chat.enviar_mensagem(mensagem, destinatario)

        if enviado:
            return jsonify({"mensagem": "Mensagem enviada com sucesso!"}), 200
        else:
            return jsonify({"mensagem": "Erro ao enviar mensagem."})

