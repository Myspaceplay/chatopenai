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
