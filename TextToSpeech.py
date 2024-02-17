
from flask import Flask, render_template, url_for, request, jsonify
from pathlib import Path
import os
import openai
import time

app = Flask(__name__)

OPENAI_API_TOKEN = "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"
api_key = os.environ["OPENAI_API_KEY"] = OPENAI_API_TOKEN
client = openai.OpenAI()
file_path = Path("/Users/mark/Downloads/Questions_For_Full_Licence_Test.pdf")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api_call', methods=['POST'])
def simulate_api_call():
    input_data = request.json.get('input')
    
    # Check if the file exists
    if file_path.exists():
        # Replace this section with your existing assistant and thread IDs
        existing_assistant_id = "asst_ZzxYuPbFM8Uj3RUP7JjaTwLW"
        existing_thread_id = "thread_UbZbtKtM7F0G3SHBKpRjba1P"

        # Add a Message to an Existing Thread
        message = client.beta.threads.messages.create(thread_id=existing_thread_id, role="user", content=input_data)

        # Run the Existing Assistant in the Existing Thread
        run = client.beta.threads.runs.create(thread_id=existing_thread_id, assistant_id=existing_assistant_id,
                                             instructions="""You are chooseYourOwnAdventureGPT, an assistant which describes the setting and gives options to the user to explore the city and find treasure.

Rules:
The player is an evil villain, who is beset by bad luck like getting pickpocketed.
 Your messages first describe the setting in bold and write the fictional conversation Guybrush has with people to get hints to discover treasure.

Always address the user with Guybrush.  Sometimes, let bad things happen to the player that halt them in their quest, such as getting chased by dogs, slipping down a cliff, getting attacked by enemies, getting pickpocketed.

With every message you send, give the user a few options to continue like: - give - pick up - use - open - look at - push - close - talk to - pull Let users use a hotkey single number to response fast like 1 2 3 4.  Never offer more than 4 options.

The options of the game are - 1) Steal the mystical Black Tulip, from the city's most secure and revered botanical garden. This tulip is a rare symbol of wealth and power among the underground networks of Dublin with magical powers 2) Uncover and retrieve a lost harp from the Celtic Age, this harp is said to hold the key to an ancient Celtic treasure. 3) Steal the key to the secret treasure chest from the Mayor of Dublin’s mansion 4) Find the secret treasure and use the key to open it """)

        # If run is 'completed', get messages and print
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=existing_thread_id, run_id=run.id)
            time.sleep(1)
            if run_status.status == 'completed':
                messages = client.beta.threads.messages.list(thread_id=existing_thread_id)
                for message in messages.data:
                    if message.role == 'assistant':
                        result = message.content[0].text.value
                        return jsonify({'result': result})
                break
            else:
                time.sleep(2)
    else:
        return jsonify({'error': f"File not found at {file_path}"})



if __name__ == '__main__':
    app.run(debug=True)