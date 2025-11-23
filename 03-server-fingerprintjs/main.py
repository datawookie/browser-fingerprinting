import logging
from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)8s] %(message)s"
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class FingerprintData(BaseModel):
    visitorId: str
    components: dict[str, dict[str, Any]]


@app.get("/", response_class=FileResponse)
async def index() -> FileResponse:
    return FileResponse("static/fingerprint.html", media_type="text/html")


@app.post("/submit")
async def submit_fingerprint(data: FingerprintData) -> JSONResponse:
    logging.info("Visitor ID: %s", data.visitorId)
    for name, component in data.components.items():
        logging.info("Component %s: %s", name, component.get("value"))
    return JSONResponse(content={"status": "ok"})
