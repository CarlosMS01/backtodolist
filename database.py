from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv() # Carga variables de entorno

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("SUPABASE_URL o SUPABASE_SERVICE_ROLE_KEY no están definidos en el entorno. Verifica tu archivo .env.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)  # Crear cliente Supabase
