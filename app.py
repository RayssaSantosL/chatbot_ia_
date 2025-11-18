# API 

# BIBLIOTECAS
from flask import Flask, request, jsonify
# importar as configurações que fizemos no 'ai_bot.py'
from bot.ai_bot import AIBot

from services.waha import Waha  #importar serviçoes do Waha (API própria)


app = Flask(__name__)


# ROTA / WEBHOOK

# Quando o Waha receber uma mensagem, ela virá para cá 👇
@app.route ('/chatbot/webhook', methods=[ 'POST' ])
def webhook():
    # Aqui estão os dados da mensagem recebida
    data = request.json  

    # ignora grupos e status
    chat_id = data['payload']['from']
    received_message = data['payload']['body']
    is_group = '@g.us' in chat_id
    is_status = 'status@broadcast' in chat_id

    if is_group or is_status:
        return jsonify({'status': 'secess', 'message': 'Mensagem de grupo/status ignorada.'}), 200
    

# INICIALIZAR O CLIENT CRIADO (WAHA)
    waha = Waha()  
    ai_bot = AIBot()

    # [NOVA FUNÇÃO ADICIONADA : 'digitando...']
    waha.start_typing(chat_id=chat_id)
    response = ai_bot.invoke(question=received_message)

    # CHAMA O METÓDO 'SEND MESSAGE'
    waha.send_message(
        chat_id = chat_id,
        message = response,
    )
    waha.stop_typing(chat_id=chat_id) # tira o status de 'digitando...'

    return jsonify({'status': 'sucess'}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
