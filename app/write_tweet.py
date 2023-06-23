import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def write_tweet(news_header: str, news_content: str, news_link: str):
    prompt = f"""

    Escríbeme un Twit polémico para que gane mucha visibilidad en base a la siguiente noticia (riéndote de la noticia con mal carácter) (DEBE DE TENER UN MÁXIMO DE 240 CARACTERES):

    Título: "{news_header}"
    
    Contenido:

    {news_content}

    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    
    return [f'{choice["message"]["content"]} {news_link}' for choice in response["choices"]]
