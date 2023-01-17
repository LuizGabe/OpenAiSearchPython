from modules.retornaConfig import apiKeyOpenai
import openai

async def pesquisar(pesquisa):
  openai.api_key = apiKeyOpenai

  try:
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=pesquisa,
      max_tokens=2048,
      n = 1,
      stop=None,
      temperature=0.5
    )
    return response

  except:
    return f"Erro ocorrido"