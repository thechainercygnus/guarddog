import os
import logging

from fastapi import FastAPI
import yaml

from . import schemas

app = FastAPI(title="GuardDog")

if not os.path.exists("logs"):
    os.mkdir("logs")

logger = logging.getLogger("guarddog")
logger.setLevel("DEBUG")

LOG_FILE = os.path.join("logs", "guarddog.log")

file_handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_config(config_path) -> dict:
    with open(config_path, "r") as reader:
        target_file_contents = reader.read()
    dict_from_yaml = yaml.safe_load(target_file_contents)
    return dict_from_yaml


def get_available_targets(config: dict) -> list:
    return [target["name"] for target in config["targets"]]


@app.post("/status/")
def post_webhook(incoming_webook: schemas.IncomingWebhook):
    try:
        logger.debug(incoming_webook)
        return 200
    except:
        return 500
