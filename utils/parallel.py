from concurrent.futures import ThreadPoolExecutor
from models.chatgpt_model import chatgpt_response
from models.gemini_model import gemini_response
from models.llama_model import llama_response

def run_parallel(prompt:str)-> dict:
    results = {}

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            "Chatgpt":executor.submit(chatgpt_response,prompt),
            "Gemini":executor.submit(gemini_response,prompt),
            "Llama":executor.submit(llama_response,prompt)
        }
        for model,future in futures.items():
            try:
                results[model]=future.result()
            except Exception as e:
                results[model]=f"Error: {str(e)}"
    return results