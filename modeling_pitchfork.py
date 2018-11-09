# modeling pitchfork.db

# things to remember:
# 1. reviewid is the same for each review across tables. ie the review with reviewid '16' will be the same review in every table. 


# uses for this database: 
# 1. correlating score with linguistic analysis of content
# 2. correllation between number of artists reviewed, score, year, number of contributions
# 3. relating score and background of author with review of genre
# 4. correlation between average score, year and genre
# 5. 




from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pitchfork.sqlite', echo = True)

# the echo flag sets up Sqlalchemy logging, it allows us to see all the SQL produced

Base = declarative_base()


# table names ['artists', 'content', 'genres', 'labels', 'reviews', 'years']

# Table('artists', MetaData(bind=None), Column('reviewid', 
# INTEGER(), table=<artists>), Column('artist', TEXT(), 
# table=<artists>), schema=None)






class Artists(Base):
    __tablename__ = 'artists'

    reviewid = Column('reviewid', Integer, primary_key = True)
    artist = Column('artist', String)


    def __repr__(self):
        return "<Artists(artist = '%s')>" % (self.artist)

print(engine.table_names())

class Content(Base):
    __tablename__ = 'content'

    reviewid = Column('reviewid', Integer, primary_key = True)
    content = Column('content', String)

    def __repr__(self):
        return "<Content(content = '%s')>" % (self.content)

class Genres(Base):
    __tablename__ = 'genres'

    reviewid = Column('reviewid', Integer, primary_key = True)
    genre = Column('genre', String)

    def __repr__(self):
        return "<Genres(genre = '%s')>" % (self.genre)

class Labels(Base):
    __tablename__ = 'labels'

    reviewid = Column('reviewid', Integer, primary_key = True)
    label = Column('label', String)

    def __repr__(self):
        return "<Labels(label = '%s'>" % (self.label)


class Years(Base):
    __tablename__ = 'years'

    reviewid = Column('reviewid', Integer, primary_key = True)
    year = Column('year', Integer)

    def __repr__(self):
        return "<Years(year = '%s')>" % (self.label)

class Reviews(Base):
    __tablename__ = 'reviews'

    reviewid = Column('reviewid', Integer, primary_key = True) 
    title = Column('title',String)
    artist = Column('artist',String)
    url = Column('url',String)
    score = Column('score', Float)
    best_new_music = Column('best_new_music',Integer)
    author = Column('author',String)
    author_type = Column('author_type',String)
    pub_date = Column('pub_date',String)
    pub_weekday = Column('pub_weekday',Integer)
    pub_day = Column('pub_day',Integer)
    pub_month = Column('pub_month',Integer)
    pub_year = Column('pub_year',Integer)

    def __repr__(self):
        return """<Reviews(
        title = '%s', 
        artist = '%s',
        url = '%s',
        score = '%s',
        best_new_music  = '%s',
        author = '%s',
        author_type = '%s',
        pub_date = '%s', 
        pub_weekday = '%s',      
        pub_day = '%s',    
        pub_month = '%s',      
        pub_year = '%s',
        )>""" % (self.title, self.artist, self.url, self.score,  self.best_new_music, self.author, self.pub_date, self.pub_weekday, self.pub_day, self.pub_month, self.pub_year)



# print(repr(Artists.__table__))


Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)




session = Session()





# new_artist = Artists(reviewid = None, artist = 'test_artist411' )

# session.add(new_artist)


# print(check)


# for instance in session.query(Artists).order_by(Artists.reviewid):
#     print(instance.artist)

# for instance in session.query(Content).order_by(Content.reviewid):
#     print(instance.content)

# for instance in session.query(Genres).order_by(Genres.reviewid):
#     print(instance.genre)
#     print(instance.reviewid)


# for instance in session.query(Labels).order_by(Labels.reviewid):
#     print(instance.label)
#     print(instance.reviewid)


# for instance in session.query(Years).order_by(Years.reviewid):
#     print(instance.year)
#     print(instance.reviewid)


search1 = session.query(Reviews).order_by(Reviews.pub_date)

total = [r.pub_date for r in search1]


print(len(total))
for t in total:
    print(t)


    



# search2 = session.query(Content).filter_by(reviewid = 16).first()
# search3 = session.query(Labels).filter_by(reviewid = 16).first()


# print(r[0] for r in search1.title)
# print(search1.pub_year)
# print(search1.pub_month)
# print(search1.url)
# print(search2.content)
# print(search3.label)



session.commit()


