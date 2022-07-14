import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PTE Backend"
    title: str = "PTE example application"
    api_prefix: str = "/pte-backend"
    debug: bool = True

    class Config:
        env_file = ".venv/my-env/"


class DevSettings(Settings):
    region_name = 'ap-southeast-1'
    dynamo_link = 'devdynamo'
    buckets = 'pte-question'
    table = 'PTE'


class StagingSettings(Settings):
    region_name = 'ap-southeast-1'
    dynamo_link = 'stagingdynamo'
    buckets = 'pte-question'
    table = 'PTE-Stagting'


def get_settings():
    env = os.environ.get('env')
    if env == 'dev':
        return DevSettings()
    elif env == 'staging':
        return StagingSettings()
    return DevSettings()


config = get_settings()
