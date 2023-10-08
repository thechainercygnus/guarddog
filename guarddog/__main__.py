import argparse

import discord
from discord.ext import commands
from fabric import Connection
import yaml

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def parse_flags():
    parser = argparse.ArgumentParser(prog="GuardDog")
    parser.add_argument(
        "--config-file",
        "-c",
        action="store",
    )
    return parser.parse_args()


def read_config(config_path) -> dict:
    with open(config_path, "r") as reader:
        target_file_contents = reader.read()
    dict_from_yaml = yaml.safe_load(target_file_contents)
    return dict_from_yaml


def get_available_targets(config: dict) -> list:
    return [target["name"] for target in config["targets"]]


c = Connection(
    host=target["properties"]["address"],
    user=target["services"]["ssh"]["sshUser"],
    connect_kwargs={"password": target["services"]["ssh"]["sshPass"]},
)
try:
    c.run("reboot")
except Exception as e:
    print(e)


if __name__ == "__main__":
    arguments = parse_flags()
    gd_config = read_config(arguments.config_file)
