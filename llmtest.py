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