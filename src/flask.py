from flask import Flask, request, jsonify
import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_visualization():
    req_data = request.get_json()
    df = pd.read_json(req_data['data'])
    user_prompt = req_data['prompt']
    
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Generate a Python script using matplotlib or seaborn to {user_prompt} using this dataset: {df.head()}",
        max_tokens=200
    )
    
    script = response.choices[0].text

    # Execute the script and generate image
    # Return image URL
    return jsonify({"image_url": "image_path.png"})  # Replace with actual image handling logic

if __name__ == "__main__":
    app.run(debug=True)
