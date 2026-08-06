from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Website API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PAGE_CONTENT = {
    "title": "To get started, edit the page.tsx file.",
    "description": (
        "Looking for a starting point or more instructions? "
        "Head over to Templates or the Learning center."
    ),
    "links": {
        "templates": "https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app",
        "learning": "https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app",
        "deploy_now": "https://vercel.com/new?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app",
        "documentation": "https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app",
    },
}


@app.get("/")
async def root() -> dict[str, str]:
    return {"status": "ok", "message": "Website API is running"}


@app.get("/api/page")
async def page() -> dict:
    return PAGE_CONTENT


@app.get("/api/hello")
async def hello() -> dict[str, str]:
    return {"message": PAGE_CONTENT["title"]}