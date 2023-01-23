from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi import Form, Request


TITLE = 'Portfolio'
CONTACTS = 'baptiste.u@gmail.com'
URL_DOC = "/redoc"
URL_SWAGGER = "/docs"

templates = Jinja2Templates("./app/templates")

app = FastAPI(
    title = TITLE,
    contacts = CONTACTS,
    redoc_url = URL_DOC,
    docs_url = URL_SWAGGER
)

app.mount("/assets", StaticFiles(directory="./app/assets"), name="assets")

@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index_test.html", context={'request': request})

@app.get("/curriculum-vitae", response_class=FileResponse)
def download_cv(request: Request):
    return "assets/file/cv_philippine_urgell.pdf"

@app.get('/info')
async def about() -> dict[str, str]:
    """Give information about the API.

    Returns:
        Dict[str, str]: With shape :
    `
    {"app_title": <TITLE>, "app_contacts": <CONTACTS>, "api_url_doc": <URL_DOC>, "api_url_swagger": <URL_SWAGGER>}
    `
    """
    return {
        "app_title": TITLE,
        "app_contacts": CONTACTS,
        "api_url_doc": URL_DOC,
        "api_url_swagger": URL_SWAGGER
    }
