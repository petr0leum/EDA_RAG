from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
from io import StringIO
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Pydantic model for request body
class VisualizationRequest(BaseModel):
    data: str  # JSON format data from the CSV file
    prompt: str

@app.post("/generate")
async def generate_visualization(request: VisualizationRequest):
    # Convert JSON data back to DataFrame
    df = pd.read_json(request.data)
    
    # Use GPT-4 or open-source model to generate visualization script
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Generate a Python script using matplotlib or seaborn to {request.prompt} using this dataset: {df.head()}",
        max_tokens=200
    )
    
    # Extract the generated Python script
    script = response.choices[0].text

    # Execute the script and save the plot as an image
    # (We'll add error handling and execution safety later)

    # Return the image as response
    return {"image_url": "image_path.png"}  # Replace with actual image handling logic
