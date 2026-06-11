import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sqlalchemy import text
from config.db_config import get_engine

engine = get_engine()

query = """
SELECT
    tablename,
    indexname
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename;
"""

with engine.connect() as conn:

    result = conn.execute(text(query))

    print("\nIndexes:\n")

    for row in result:
        print(f"{row.tablename} --> {row.indexname}")