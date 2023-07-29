# Импортируем необходимые библиотеки Flask, transformers и другие
from flask import Flask, render_template,request,jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Загружаем модель и токенизатор DialoGPT
tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/rugpt3medium_based_on_gpt2")
model = AutoModelForCausalLM.from_pretrained("sberbank-ai/rugpt3medium_based_on_gpt2")

# Создаем приложение Flask
app = Flask(__name__)

# Маршрут для отображения чатбота
@app.route("/")
def index():
    return render_template('chatbot.html')

# Маршрут для получения ответа от чатбота
@app.route('/get', methods=['GET','POST'])
def chat():
    msg = request.form['msg']
    input = msg
    return get_Chat_response(input)

# Функция для генерации ответа чатбота
def get_Chat_response(text):

    # Код для генерации ответа моделью DialoGPT
    for step in range(5):

        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
# Запуск приложения Flask
if __name__ == "__main__":
    app.run