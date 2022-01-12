import yaml

CONFIG='conf.yml'


def read_config(CONFIG):
    
    if CONFIG == None:
        print('No config file exists. Set config file in config.py')
    
    else:
        with open(CONFIG) as config:
            print('Config file read.')
            return yaml.safe_load(config)


if __name__ == "__main__":
    read_config()