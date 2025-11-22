from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI()

# Mount static directory for JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Data model for posted fingerprint
class FingerprintPayload(BaseModel):
    visitorId: str
    components: Dict[str, Any]

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FingerprintJS + FastAPI Demo</title>
        <script src="https://openfpcdn.io/fingerprintjs/v3"></script>
    </head>
    <body>
        <h1>Using FingerprintJS to fingerprint your browser...</h1>
        <pre id="output">Collecting...</pre>
        <script type="module" src="/static/fingerprint.js"></script>
    </body>
    </html>
    """

@app.post("/submit")
async def submit_fingerprint(data: FingerprintPayload):
    print("🎯 Fingerprint received:")
    print(f"Visitor ID: {data.visitorId}")
    print("Components:")
    for key, value in data.components.items():
        print(f"  {key}: {value.get('value')}")
    return JSONResponse(content={"status": "received"})
