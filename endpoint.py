from fastapi import FastAPI
from pydantic import BaseModel
from diia import diia

app = FastAPI()


@app.post("/diia-receiver")
async def diia_reciver(data):
    print(data)
    return { "success": True }

class link_generator(BaseModel):
    user_id: str
    return_link: str

@app.post("/link-generator")
async def link_generator(data:link_generator):
    deeplink = diia.create_deeplink(
        branch_id=diia.branch_id,
        return_deeplink=data.return_link,
        user_id=data.user_id)
    return { "deeplink": deeplink }