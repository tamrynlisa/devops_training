import json
import os

from fastapi import FastAPI

app = FastAPI()


def add_message(response: dict, msg: str) -> dict:
    return {
        **response,
        "message": msg
    }


@app.get("/")
def root():
    return add_message({}, "Hi Me!")


@app.get("/test1")
def test():
    return add_message({}, "test take two")


@app.get("/custom")
def custom():
    return add_message({}, os.environ['MESSAGE'])


@app.get("/version")
def version():
    with open("src/version.json", "r") as version_file:
        version_data = json.load(version_file)
        return {
            "version": version_data.get("version", "0.0.0")
        }