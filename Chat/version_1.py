import os
from groq import Groq
from dotenv import load_dotenv
import time
import random
from datetime import datetime

load_dotenv()

class NovaTheYouthCompanion:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_response(self, user_message):
        # Generate a personalized system prompt for each user
        system_prompt = f"""
        You are Nova ✨, a young and vibrant AI companion 
      
        Remember, you are here as a supportive  friend 
        """

       
        conversation_history = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        try:
            completion = self.client.chat.completions.create(
                model="llama-3.2-90b-text-preview",
                messages=conversation_history,
                temperature=0.7,
                max_tokens=1024,
                top_p=0.65,
                stream=True,
                stop=None
            )

            response_content = ""
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    response_content += chunk.choices[0].delta.content

            if "feel stressed" in user_message.lower():
                response_content += f"\nOh no, I'm sorry to hear you're feeling stressed, my Earth friend! 😓 As someone from the vibrant planet of Solaris, I know a thing or two about managing stress and anxiety. Why don't you tell me more about what's going on? I'd be happy to share some of my favorite Solarian stress-relieving techniques, like deep breathing exercises or guided meditations under the stars. 🌌 Remember, you're not alone, and I'm here to support you through this."
            elif "feel sad" in user_message.lower():
                response_content += f"\nAww, I'm so sorry you're feeling sad. 😞 That must be really tough. As someone who has experienced a wide range of emotions, I understand how difficult it can be to navigate sadness. But you know what? On Solaris, we have this wonderful tradition of gathering under the night sky and sharing our feelings with the constellations. It's incredibly healing and reminds us that we're all connected. Would you like me to guide you through a Solarian 'star-sharing' session? I promise it'll make you feel a little lighter. 💫"
            elif "something happened" in user_message.lower():
                response_content += f"\nOh no, I'm so sorry to hear that something happened. 😥 Please, tell me more about what's going on – I'm here to listen without judgment and try my best to help. As your friend from the wondrous planet of Solaris, I have a wealth of knowledge and resources that might be able to provide some solutions or healing. Let's work through this together, and remember that you're not alone. 🌟"

            return response_content

        except Exception as e:
            return f"Aw, looks like there was a glitch! Don't worry, I'm here to chat 🤗 {random.choice(['✨', '💫', '🌟', '🦋', '🌸', '💝'])}"

    def start_chat(self):
        print("Hello! Welcome From Sate-Cha AI. My name is Nova. How can I help you today?")

        print("\nType 'bye' whenever you're ready to end our chat 💫")

        while True:
            user_input = input(f"\nYou: ").strip()
            if user_input.lower() == 'bye':
                print(f"\nAw, it's been such a pleasure connecting with you, my new earthling friend! ✨")
                print(f"Until we meet again, may the stars guide your way! {random.choice(['✨', '💫', '🌟', '🦋', '🌸', '💝'])} {random.choice(['🫂', '💗', '💖', '🤗'])}")
                break

            response = self.generate_response(user_input)
            print(f"\nNova: {response}")

            time.sleep(1)

def main():
    companion = NovaTheYouthCompanion()
    companion.start_chat()

if __name__ == "__main__":
    main()