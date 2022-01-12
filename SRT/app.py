# SRT core module
import sys
sys.path.append("../")
import settings

 
def app():
    # init conf
    settings.read_config()
    

    
    

if __name__ == "__main__":
    app()