from openai import OpenAI


class ChatGPTResponder:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    def get_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )
        chatbot_response = response.choices[0].message.content
        return chatbot_response
