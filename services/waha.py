#Client WAHA

# BIBLIOTECAS
import requests
 
class Waha:   # classe Waha
    def __init__(self):
        self.__api_url = 'http://waha:3000' # metodo de inicialização

    def send_message(Self, chat_id, message):   # metodo de envio de mensagem 
        url = f'{Self.__api_url}/api/sendText'
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': message,
        }
        requests.post (
            url=url,
            json=payload,
            headers=headers,
        )

# metodo mostra 'digitando...' no whatsapp

    def start_typing(self, chat_id):   # inicia a execução do status 'digitando...'
        url = f'{self.__api_url}/api/startTyping'
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers,
        )

    def stop_typing(self,chat_id):   # finaliza a execução do status 'digitando...'
        url=f'{self.__api_url}/api/stopTyping'
        headers={
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers,
        )