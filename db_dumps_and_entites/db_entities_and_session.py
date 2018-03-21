from pony.orm import *

db = Database()

db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='root', db='soc_net_analysis')


class Venue(db.Entity):
    venue_id = PrimaryKey(int, auto=True)
    name = Required(unicode, unique=True)
    url = Optional(unicode, max_len=256)
    venue__article_venue_id = Set('Article')


class Article(db.Entity):
    article_id = PrimaryKey(int)
    title = Required(unicode)
    abstract = Required(LongUnicode)
    year = Required(int)
    venue_id = Optional(Venue)
    article__citation_article_id = Set('Citation', reverse='article_id')
    article__author_article = Set('AuthorArticle', reverse='article_id')
    # article__citation_cited_by = Set('Citation', reverse='cited_by')


class Citation(db.Entity):
    citation_id = PrimaryKey(int, auto=True)
    article_id = Required(Article)
    cited_by = Required(int)
    # cited_by = Required(Author)


class Author(db.Entity):
    author_id = PrimaryKey(int, auto=True)
    name = Required(LongUnicode)
    url = Optional(unicode, max_len=256)
    author__author_article = Set('AuthorArticle', reverse='author_id')


class AuthorArticle(db.Entity):
    _table_ = 'author_article'
    author_id = Required(Author)
    article_id = Required(Article)


db.generate_mapping(create_tables=True)