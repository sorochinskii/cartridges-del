from fastapi import FastAPI

from source.api.v1.app import app as app_v1
from source.config import settings

app = FastAPI(title='cartridges')

app.mount('/v1', app_v1)
print(settings.HOST)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('__main__:app',
                host=f'{settings.HOST}',
                port=settings.HTTP_PORT,
                reload=True,
                reload_dirs=['source'],
                log_level='debug')
