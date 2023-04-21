from fastapi import FastAPI, Response, Request
from fastapi.responses import StreamingResponse, HTMLResponse
import io
import os
from script import take_screenshot

app = FastAPI()

def generate_form() -> str:
    return """
    <html>
        <body>
            <h1>Gerar Screenshot</h1>
            <form action="/screenshot" method="get">
                <label for="url">URL:</label>
                <input type="text" id="url" name="url" value="https://web.whatsapp.com/" required>
                <button type="submit">Gerar Screenshot</button>
            </form>
        </body>
    </html>
    """

@app.get("/screenshot", response_class=HTMLResponse)
async def get_screenshot(request: Request):
    url = request.query_params.get("url")
    if not url:
        return generate_form()

    filename = take_screenshot(url)
    img_data = None

    with open(filename, "rb") as img_file:
        img_data = img_file.read()
        os.remove(filename)

    return StreamingResponse(io.BytesIO(img_data), media_type="image/png")
