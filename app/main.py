from fastapi import FastAPI
from starlette.responses import HTMLResponse
import sys

app = FastAPI()

@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>Simple HTML Page</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTML page generated by FastAPI.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/error")
def exit():
    sys.exit("Program crashed due to /exit endpoint being accessed.")