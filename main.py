from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fetch_data import fetch_and_merge_all_datasets

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/analytics/datadump")
async def get_analytics_data():
    """Returns the combined analytics data as JSON."""
    df = fetch_and_merge_all_datasets()
    # return df.to_json(orient='records', date_format='iso')
    # Convert Timestamps to strings before converting to JSON
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return JSONResponse(content=df.to_dict(orient='records'))
