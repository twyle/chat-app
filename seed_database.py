from dotenv import load_dotenv
load_dotenv()
from chat.tools.utils.database.video_crud import seed_database


seed_database()
