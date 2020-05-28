from whoosh.qparser import QueryParser
import searching.result as r
from whoosh.qparser import MultifieldParser
from query.expander import expand
import logging
from whoosh import scoring

logger = logging.getLogger()


class Searcher:
    def __init__(self, wikimedia):
        self.wikimedia = wikimedia

    def search(self, text):
        results = []
        # TODO expand query
        query = MultifieldParser(['title', 'text'], schema=self.wikimedia.index.schema).parse(text)
        # QueryParser("text", schema=self.wikimedia.index.schema).parse(text)

        try:
            searcher = self.wikimedia.index.searcher(weighting=scoring.PL2())
            results = searcher.search(query, limit=100)
            return [r.Result(i, query) for i in results]
        except Exception as e:
            logger.error(e)
