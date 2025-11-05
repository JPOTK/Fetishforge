from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# YOUR GROK KEY
GROK_KEY = "xai-XWUHDHWErv3u25bGwfOgkoFaCGBJ52juAA4x5TPbpJaUnAPqV7Mhw1GVACTSsHJfiPS39QR2YeCZOI6C"

@app.post("/chat")
async def chat(data: dict):
    profile = data.get("profile", [])
    msg = data.get("message", "")

    prompt = f"BDSM AI companion. Profile: {profile}. Respond in character: {msg}"

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://api.x.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROK_KEY}"},
            json={"model": "grok-beta", "messages": [{"role": "user", "content": prompt}], "temperature": 0.9}
        )
        reply = res.json()["choices"][0]["message"]["content"]

    return {"reply": reply}