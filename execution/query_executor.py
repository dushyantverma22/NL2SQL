import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sqlalchemy import text

from config.db_config import get_engine

engine = get_engine()


def execute_query(sql: str):

    with engine.connect() as conn:

        result = conn.execute(text(sql))

        columns = list(result.keys())

        rows = result.fetchall()

    return columns, rows