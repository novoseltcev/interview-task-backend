from app import create_app
from app.db import db


def main(dump_file='dumps/inserts.sql'):
    """Пересоздаёт таблицы БД и загружает тестовый набор"""

    create_app()
    db.drop_all()
    db.create_all()
    try:
        with open(dump_file) as f:
            db.engine.execute(f.read())
    except Exception:
        pass


if __name__ == '__main__':
    main()
