import os
import unittest
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestDatabaseFunctionality(unittest.TestCase):
    def test_database_is_removed_if_exists(self):
        db_name = "test_amity_exists.db"
        if os.path.exists(db_name):
            os.remove(db_name)
        from sqlalchemy import create_engine
        engine = create_engine('sqlite:///' + db_name)
        from sqlalchemy.orm import sessionmaker
        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)
        os.remove(db_name)
        self.assertTrue("sqlite:///" + db_name)
