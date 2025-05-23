from fastapi import APIRouter
from openai import OpenAI
from interfaces.chatinterfaces import InputMessage

router = APIRouter()

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message: " + data["message"])

    message = "Por favor responde de manera concreta, clara y siempre en castellano."

    try:
        completion = client.chat.completions.create(
            model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente que siempre responde en castellano de forma clara y breve"
                },
                {
                    "role": "user",
                    "content": message + " responde a esta pregunta: " + data["message"]
                }
            ]
        )
        respuesta = completion.choices[0].message.content
        print("response: " + respuesta)
        return {
            "status": "ok",
            "response": respuesta
        }
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "response": str(e)}
