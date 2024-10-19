from openai import OpenAI

def recipe_image_gen(openai_api_key, prompt):
    client = OpenAI(api_key=openai_api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt="Generate a finished realistic vivid cuisine image in warm atmosphere and family table based on the recipe: " + prompt,
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    return image_url



