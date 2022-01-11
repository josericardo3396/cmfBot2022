from settings.server import server_manager
from dotenv import load_dotenv

if server_manager.get_app().debug:
    load_dotenv()
