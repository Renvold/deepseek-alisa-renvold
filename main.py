from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.post("/")
async def handle_alice_request():
    logging.info("--- ПОЛУЧЕН ЗАПРОС ОТ АЛИСЫ ---")
    return {
        "version": "1.0",
        "session": {},
        "response": {
            "end_session": False,
            "text": "Тестовый ответ! Сервер работает."
        }
    }
