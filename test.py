from helper_classes.heading import HeadingCA
from app.factory import create_app, db
import pprint




if __name__=='__main__':
    app = create_app()
    pp = pprint.PrettyPrinter()
    with app.app_context():
        t = HeadingCA('0403')


        # d = t.gen_tariff_dict()
        # pp.pprint(d)
        t.book_view()