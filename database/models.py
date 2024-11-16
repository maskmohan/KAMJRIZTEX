from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(String)
    description = Column(String)

Base.metadata.create_all(bind=engine)

def save_to_db(data):
    db = SessionLocal()
    for item in data:
        product = Product(**item)
        db.add(product)
    db.commit()

def fetch_latest_data():
    db = SessionLocal()
    return db.query(Product).all()
