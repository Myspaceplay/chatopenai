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
