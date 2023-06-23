import openai
from flask import Flask, request, jsonify

openai.api_key = 'your-api-key'

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    response = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(port=5000)
