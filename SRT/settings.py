import yaml

CONFIG='conf.yml'


def read_config():

    with open(CONFIG, "r") as config:
        try:
            print(yaml.safe_load(CONFIG))
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":
    read_config()