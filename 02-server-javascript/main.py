import json
import logging
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict

logging.getLogger().setLevel(logging.INFO)

app = FastAPI()

class FingerprintData(BaseModel):
    data: Dict[str, Any]

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Browser Fingerprint</title></head>
    <body>
        <h1>Browser Fingerprint</h1>
        <pre id="fingerprint"></pre>
        <script>
        async function fingerprint() {
            const data = {
                userAgent: navigator.userAgent,
                language: navigator.language,
                platform: navigator.platform,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                screen: {
                    width: screen.width,
                    height: screen.height,
                    colorDepth: screen.colorDepth
                },
                plugins: Array.from(navigator.plugins).map(p => p.name),
            };

            document.getElementById("fingerprint").textContent = JSON.stringify(data, null, 2);

            await fetch("/submit", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ data })
            });
        }
        fingerprint();
        </script>
    </body>
    </html>
    """

@app.post("/submit")
async def submit_fingerprint(fingerprint: FingerprintData):
    logging.info(f"Fingerprint:\n{json.dumps(fingerprint.data, indent=2)}")
    return JSONResponse(content={"status": "ok"})
