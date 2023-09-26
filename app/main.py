from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Create a FastAPI instance
app = FastAPI()

# Create a Jinja2Templates object
templates = Jinja2Templates(directory="template")

@app.get("/", response_class=HTMLResponse)
async def showing_item(request: Request):
    # Render the 'index.html' template and pass any required data
    return templates.TemplateResponse("index.html", {"request": request})
