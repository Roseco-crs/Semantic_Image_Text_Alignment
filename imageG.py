import openai
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Example prompt
prompt = """
A vibrant, detailed image of a LEGO CITY set, showcasing key features like buildings, vehicles, and mini-figures.
Interactive Element: 'Choose Your Adventure' prompt, a large, colorful button placed strategically to draw attention.
Logo: LEGO logo placed subtly in the corner to reinforce brand recognition.
"""

# Generate image from text
response = openai.Completion.create(
    engine="image-alpha-001",  # Use the image generation engine
    prompt=prompt,
    temperature=0.7,
    max_tokens=512,
)

# Extract image URL from the API response
image_url = response['choices'][0]['content']

# Display the generated image URL
print("Generated Image URL:", image_url)
