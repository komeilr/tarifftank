# from helper_classes.heading import HeadingCA
# from helper_classes.tariffrate import TariffRateCA

class Notes:
    def __init__(self):
        self.chapter_notes = self._query_chapter_notes()
        self.section_notes = self.chapter_notes.section

    
    def _query_chapter_notes(self):

        query = app.ca.models.Chapter.query.filter_by(chapter=chapter).first()
        return query