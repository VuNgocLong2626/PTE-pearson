import boto3
import os
from pydantic import BaseSettings


my_session = boto3.session.Session()
my_region = my_session.region_name


class Settings(BaseSettings):
    app_name: str = "PTE Backend"
    title: str = "PTE example application"
    api_prefix: str = "/pte-backend"
    debug: bool = True

    class Config:
        env_file = ".venv/my-env/"


class DevSettings(Settings):
    region_name = my_region
    dynamo_link = 'devdynamo'
    table = 'PTE'


class StagingSettings(Settings):
    region_name = my_region
    dynamo_link = 'stagingdynamo'
    table = 'PTE-Stagting'


def get_settings():
    env = os.environ.get('env')
    if env == 'dev':
        return DevSettings()
    elif env == 'staging':
        return StagingSettings()
    return DevSettings()


config = get_settings()
