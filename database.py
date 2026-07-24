from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL="sqlite:///./student.db"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread":False
    }
)
sessionLocal=sessionmaker(
    expire_on_commit=False,
    autoflush=False,
    bind=engine
)
base=declarative_base()
