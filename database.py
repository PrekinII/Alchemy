import json
from models import Publisher, Book, Shop, Stock, Sale
from connection import Session


def insert_publisher(id_p, author1):
    publisher1 = Publisher(id=id_p, name=author1)
    with Session() as session:
        session.add(publisher1)
        session.commit()


def insert_book(id_b, title_b, id_pub):
    book = Book(id=id_b, title=title_b, id_publisher=id_pub)
    with Session() as session:
        session.add(book)
        session.commit()


def insert_shop(id_s, name_s):
    shop = Shop(id=id_s, name=name_s)
    with Session() as session:
        session.add(shop)
        session.commit()


def insert_stock(id_st, id_sh, id_b, count_st):
    stock = Stock(id=id_st, id_shop=id_sh, id_book=id_b, count=count_st)
    with Session() as session:
        session.add(stock)
        session.commit()


def insert_sale(id_sale1, price1, date_sale1, count1, id_stock1):
    sale = Sale(id=id_sale1, price=price1, date_sale=date_sale1, count=count1, id_stock=id_stock1)
    with Session() as session:
        session.add(sale)
        session.commit()


def open_json():
    with open("tests_data.json") as file:
        data = json.load(file)
    for row in data:
        if row.get('model') == 'publisher':
            id_publ = row.get('pk')
            author = row.get('fields').get('name')
            insert_publisher(id_publ, author)
        elif row.get('model') == 'book':
            book_id = row.get('pk')
            title = row.get('fields').get('title')
            id_publisher = row.get('fields').get('id_publisher')
            insert_book(book_id, title, id_publisher)
        elif row.get('model') == 'shop':
            shop_id = row.get('pk')
            name = row.get('fields').get('name')
            insert_shop(shop_id, name)
        elif row.get('model') == 'stock':
            stock_id = row.get('pk')
            id_shop = row.get('fields').get('id_shop')
            id_book = row.get('fields').get('id_book')
            count = row.get('fields').get('count')
            insert_stock(stock_id, id_shop, id_book, count)
        elif row.get('model') == 'sale':
            id_sale = row.get('pk')
            price = row.get('fields').get('price')
            date_sale = row.get('fields').get('date_sale')
            count = row.get('fields').get('count')
            id_stock = row.get('fields').get('id_stock')
            insert_sale(id_sale, price, date_sale, count, id_stock)