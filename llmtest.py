from openai import OpenAI

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")


messages = input("Cual es tu pregunta: ")

prompt = (
    "Por favor responde de manera clara y sin simbolos innecesarios"
    "Evita usar otros idiomas que no sean el castellano y escribe una respuesta concisa"
    f"Pregunta del usaurio: {messages}"
)

completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
        {
            "role": "user",
            "content":prompt   
        }
    ]
)

print(completion.choices[0].message.content)
