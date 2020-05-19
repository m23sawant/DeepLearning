## https://www.googleapis.com/drive/v3/files/1--bCN_4Y95_GXwH0ezPdAXHw9Ba3d2JU?alt=media&key=AIzaSyDUh05b8uHWU1WHZK_rYwqgTsz-oGaJf_Q


import aiohttp
import asyncio
import uvicorn
from fastai import *
from fastai.vision import *
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles


export_file_url = 'https://www.googleapis.com/drive/v3/files/1--bCN_4Y95_GXwH0ezPdAXHw9Ba3d2JU?alt=media&key=AIzaSyDUh05b8uHWU1WHZK_rYwqgTsz-oGaJf_Q' #This will be the download url for your export.pkl file that you have already saved.
export_file_name = 'export3.pkl'

classes = ["Apple pie","Baby back ribs","Baklava","Beef carpaccio","Beef tartare","Beet salad","Beignets","Bibimbap","Bread pudding","Breakfast burrito","Bruschetta",
           "Caesar salad","Cannoli","Caprese salad","Carrot cake","Ceviche","Cheesecake","Cheese plate","Chicken curry","Chicken quesadilla","Chicken wings",
           "Chocolate cake","Chocolate mousse","Churros","Clam chowder","Club sandwich","Crab cakes","Creme brulee","Croque madame","Cup cakes",
           "Deviled eggs","Donuts","Dumplings","Edamame","Eggs benedict","Escargots","Falafel","Filet mignon","Fish and chips","Foie gras","French fries",
           "French onion soup","French toast","Fried calamari","Fried rice","Frozen yogurt","Garlic bread","Gnocchi","Greek salad","Grilled cheese sandwich",
           "Grilled salmon","Guacamole","Gyoza","Hamburger","Hot and sour soup","Hot dog","Huevos rancheros","Hummus","Ice cream","Lasagna","Lobster bisque",
           "Lobster roll sandwich","Macaroni and cheese","Macarons","Miso soup","Mussels","Nachos","Omelette","Onion rings","Oysters","Pad thai","Paella",
           "Pancakes","Panna cotta","Peking duck","Pho","Pizza","Pork chop","Poutine","Prime rib","Pulled pork sandwich","Ramen","Ravioli","Red velvet cake",
           "Risotto","Samosa","Sashimi","Scallops","Seaweed salad","Shrimp and grits","Spaghetti bolognese","Spaghetti carbonara","Spring rolls","Steak",
           "Strawberry shortcake","Sushi","Tacos","Takoyaki","Tiramisu","Tuna tartare","Waffles"] #Replace these classes with the labels that your model identifies.

path = Path(__file__).parent

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))


async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f:
                f.write(data)


async def setup_learner():
    await download_file(export_file_url, path / export_file_name)
    try:
        learn = load_learner(path, export_file_name)
        return learn
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
            raise RuntimeError(message)
        else:
            raise


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()


@app.route('/')
async def homepage(request):
    html_file = path / 'view' / 'index.html'
    return HTMLResponse(html_file.open().read())


@app.route('/analyze', methods=['POST'])
async def analyze(request):
    img_data = await request.form()
    img_bytes = await (img_data['file'].read())
    img = open_image(BytesIO(img_bytes))
    prediction = learn.predict(img)[0]
    return JSONResponse({'result': str(prediction)})



if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app, host='0.0.0.0', port=5000, log_level="info")
