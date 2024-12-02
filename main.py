
from fastapi import FastAPI
from routes.route import router
app = FastAPI(
    title="Student Course API",
    description="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection.",
)

app.include_router(router)

