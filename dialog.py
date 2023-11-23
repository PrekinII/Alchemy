from connection import session
from models import Publisher, Book, Shop, Stock, Sale


def show_publisher():
    query = session.query(Publisher).all()
    for x in query:
        print(f'ID Издателя {x.id} | Издатель {x.name}')
    return


def selected_publisher(id_p):
    query = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .join(Publisher).join(Stock).join(Shop).join(Sale)
        .filter(Publisher.id == id_p)
    )
    for x in query:
        print(f'{x.title} | {x.name} | {x.price} | {x.date_sale}')
    return
