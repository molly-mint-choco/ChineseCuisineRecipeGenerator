import os
from dotenv import load_dotenv
from openai import OpenAI
import time
from image_gen.openai_recipe_image_gen import recipe_image_gen

def ingredient_assistant(photo_path, additional_instructions = None):
    load_dotenv()
    openai_api_key_file_path = os.getenv('OPENAI_API_KEY')
    with open(openai_api_key_file_path, 'r') as file:
        openai_api_key = file.readline().strip()
    assistant_id = os.getenv('OPENAI_ASSISTANT_ID')
    client = OpenAI(api_key=openai_api_key)
    photo_file = client.files.create(file=open(photo_path, "rb"),purpose="vision")
    thread = client.beta.threads.create()
    print(thread)
    content = [
        {
            "type":"image_file",
            "image_file": {
                "file_id": photo_file.id
            }
        }
    ]
    if additional_instructions:
        content.append(
            {
                "type": "text",
                "text": additional_instructions
            }
        )
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content
    )
    print(message)
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id)

    if run.required_action and run.required_action.submit_tool_outputs:
        for tool_call in run.required_action.submit_tool_outputs.tool_calls:
            tool_call_id = tool_call.id
            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=
                [
                    {
                        "tool_call_id": tool_call_id,
                        "output": "Success"
                    }
                ]
            )
        

    print(run)
    while (run.status != 'completed'):
        time.sleep(3)
        run = client.beta.threads.runs.poll(thread_id=thread.id, run_id=run.id)
        print(run)

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        print(messages)
        for message in messages.data:
            if message.role == 'assistant':
                recipe_text = message.content[0].text.value
                recipe_image_url = recipe_image_gen(openai_api_key, recipe_text)
                return {"recipe": recipe_text, "image_url": recipe_image_url}

    else:
        print(run.status)
        return "Error in messages."


