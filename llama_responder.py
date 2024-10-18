import ollama


class LlamaResponder:
    def __init__(self, model="llama3.2"):
        self.model = model

    def get_response(self, user_input):
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        chatbot_response = response['message']['content']
        return chatbot_response
