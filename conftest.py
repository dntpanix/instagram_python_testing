import sys
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).parent.absolute()
sys.path.insert(0, str(ROOT_DIR))

load_dotenv()
