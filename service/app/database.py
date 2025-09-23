from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL="postgresql://postgres:postgres@localhost:5432/home_library"

engine = create_engine(DATABASE_URL)

def create_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
