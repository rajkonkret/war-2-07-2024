import openai

# API-KEY - klucz pobrany z openai (płatny)
client = openai.OpenAI(api_key='{API_KEY}')
print(client)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role': "assistant", "content": "Kto wygrał F1 w 2020"}]
)
print(response)
print(response.choices[0].message.content)
# W sezonie Formuły 1 2020 mistrzem świata został Lewis Hamilton
# reprezentujący zespół Mercedes-AMG Petronas Formula One Team.
# Był to już siódmy tytuł mistrzowski dla Hamiltona.
