from models import create_tables
from database import open_json
from connection import engine
from dialog import show_publisher, selected_publisher


create_tables(engine)
open_json()
show_publisher()
ques = int(input("Введите ID издателя: "))
selected_publisher(ques)
