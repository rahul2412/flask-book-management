from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Genre, Book

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Initialising admin

User1 = User(name="Admin", email="admin@fakemail.com",
             picture='https://imgix.ranker.com/user_node_img/50081/'
             '1001613426/original/i-and-_39_ll-take-a-potato-chip-and'
             '-eat-it-photo-u1?w=650&q=50&fm=jpg&fit=crop&crop=faces')
session.add(User1)
session.commit()


# Adding genres

Fantasy = Genre(name="Fantasy",
                icon='https://is5-ssl.mzstatic.com/image/thumb/Purple'
                '122/v4/79/8c/df/798cdfed-8d1f-1cab-be14-89d761e9b4c8/source'
                '/256x256bb.jpg')
session.add(Fantasy)
session.commit()

ScienceFiction = Genre(name="Science Fiction",
                       icon='https://static.scientificamerican.com/blogs/cache'
                       '/file/DC6D37DB-CC3C-4128-B77A29A1F16F1AA4.jpg?w=590&'
                       'h=393&1A606BE2-035D-4821-843FCDDA0CD8D5EA')
session.add(ScienceFiction)
session.commit()

Classics = Genre(name="Classics",
                 icon='https://aardvarkian.files.wordpress.com/2011'
                 '/10/56_classics_431.jpg')
session.add(Classics)
session.commit()

Humor = Genre(name="Humor",
              icon='https://www.marketingfacts.nl/images/uploads/jeeves.jpg')
session.add(Humor)
session.commit()

Mystery = Genre(name="Mystery",
                icon='https://is3-ssl.mzstatic.com/image/thumb/Purple128'
                '/v4/d2/32/c9/d232c9b9-cc4d-5c87-fa0c-fb0e6833c64a'
                '/source/256x256bb.jpg')
session.add(Mystery)
session.commit()

Biography = Genre(name="Biography",
                  icon='https://tse.mm.bing.net/th?id=OIP.nbGs'
                  'UD3Rs1_kYypqsaZ3XQAAAA')
session.add(Biography)
session.commit()

SelfHelp = Genre(name="Self Help",
                 icon='https://cdn.24.co.za/files/Cms/General'
                 '/d/4482/dc628be03e8744118b959fcc2ad2ca43.jpg')
session.add(SelfHelp)
session.commit()


# Adding some Books

book1 = Book(name="Alice's Adventures in Wonderland",
             author="Lewis Caroll",
             description="Alice is sitting with her sister outdoors when she spies a White "
             "Rabbit with a pocket watch. Fascinated by the sight, she follows the rabbit "
             "down the hole. She falls for a long time, and finds herself in a long "
             "hallway full of doors.",
             cover='https://images-na.ssl-images-amazon.com/images/I/61RfhBNcKdL.jpg',
             link='https://www.gutenberg.org/files/11/11-h/11-h.htm',
             genre=Fantasy, user=User1)
session.add(book1)
session.commit()

book2 = Book(name="Peter Pan",
             author="James M. Barrie",
             description="n Peter Pan, Peter Pan takes Wendy and her siblings to Neverland. "
             "There, Peter is plagued by the pirate Hook, who is himself plagued by the "
             "crocodile who bit off his hand. In the end, Wendy, Peter, "
             "and the Lost Boys escape Hook's clutches.",
             cover='https://images.store.hmv.com/app_/responsive/HMVStore/media/product/876099/01-876099.jpg?w=500',
             link='https://www.gutenberg.org/files/16/16-h/16-h.htm',
             genre=Fantasy, user=User1)
session.add(book2)
session.commit()

book3 = Book(name="The Strange Case of Dr. Jekyll and Mr. Hyde", author="Robert Louis Stevenson",
             description="Strange Case of Dr Jekyll and Mr Hyde is a gothic novella by Scottish "
             "author Robert Louis Stevenson, first published in 1886. ... It is about a "
             "London lawyer named Gabriel John Utterson who investigates strange occurrences "
             "between his old friend, Dr Henry Jekyll, and the evil Edward Hyde.",
             cover='https://res.cloudinary.com/bubblin/image/upload/c_fill,f_auto,'
             'h_610,q_auto,w_450/v1/uploads/production/cover/486/front_image.jpg',
             link='https://www.gutenberg.org/files/43/43-h/43-h.htm',
             genre=ScienceFiction, user=User1)
session.add(book3)
session.commit()

book4 = Book(name="Frankenstein", author="Mary Wollstonecraft Shelley",
             description="helley describes the monster as 8-foot-tall ,(2.4 m), hideously "
             "ugly, but sensitive and emotional. The monster attempts to fit into human "
             "society but is shunned, which leads him to seek revenge against Frankenstein.",
             cover='https://images-na.ssl-images-amazon.com/images/I/51WEpw8t2LL._SX331_BO1,204,203,200_.jpg',
             link='https://www.gutenberg.org/files/84/84-h/84-h.htm',
             genre=ScienceFiction, user=User1)
session.add(book4)
session.commit()

book5 = Book(name="Pride and Prejudice", author="Jane Austen",
             description="The story charts the emotional development of the "
             "protagonist, Elizabeth Bennet, who learns the error of making "
             "hasty judgments and comes to appreciate the difference between "
             "the superficial and the essential.",
             cover='https://upload.wikimedia.org/wikipedia/commons'
             '/thumb/1/17/PrideAndPrejudiceTitlePage.jpg/330px'
             '-PrideAndPrejudiceTitlePage.jpg',
             link='https://www.gutenberg.org/files/42671/42671-h/42671-h.htm',
             genre=Classics, user=User1)
session.add(book5)
session.commit()

book6 = Book(name="Jane Eyre", author="Charlotte Bronte",
             description="Jane Eyre follows the experiences of its "
             "eponymous heroine, including her growth to adulthood and her "
             "love for Mr. Rochester, the brooding master of Thornfield Hall. "
             "The novel revolutionized prose fiction in that the focus on "
             "Jane's moral and spiritual development is told through an "
             "intimate, first-person narrative, where actions and events are "
             "coloured by a psychological intensity.",
             cover='https://upload.wikimedia.org/wikipedia/commons/thumb'
             '/9/9b/Jane_Eyre_title_page.jpg/330px-Jane_Eyre_title_page.jpg',
             link='https://www.gutenberg.org/files/1260/1260-h/1260-h.htm',
             genre=Classics, user=User1)
session.add(book6)
session.commit()

book7 = Book(name="Right Ho Jeeves", author="P G Wodehouse",
             description="Right Ho, Jeeves is a novel by P. G. Wodehouse, "
             "the second full-length novel featuring the popular characters "
             "Jeeves and Bertie Wooster, after Thank You, Jeeves.",
             cover='https://upload.wikimedia.org/wikipedia/en/8/83'
             '/RightHoJeeves.jpg',
             link='https://www.gutenberg.org/files/10554/10554-h/10554-h.htm',
             genre=Humor, user=User1)
session.add(book7)
session.commit()

book8 = Book(name="Three Men in a Boat", author="Jerome K Jerome",
             description="This is a humorous account by English writer "
             "Jerome K. Jerome of a two-week boating holiday on the Thames "
             "from Kingston upon Thames to Oxford and back to Kingston.",
             cover='https://images-na.ssl-images-amazon.com/images'
             '/I/71iCUnY11ML.jpg',
             link='https://www.gutenberg.org/files/308/308-h/308-h.htm',
             genre=Humor, user=User1)
session.add(book8)
session.commit()

book9 = Book(name="The Adventures of Sherlock Holmes", author="Arthur Conan Doyle",
             description="The Adventures of Sherlock Holmes is a collection of twelve "
             "short stories by Arthur Conan Doyle, featuring his fictional detective "
             "Sherlock Holmes. It was first published on 14 October 1892; the "
             "individual stories had been serialised in The Strand Magazine "
             "between July 1891 and June 1892.",
             cover="https://is5-ssl.mzstatic.com/image/thumb/Video/v4"
             "/a3/93/28/a393285a-4184-dfe2-8565-910873e794f0/source/1200x630bb.jpg",
             link='https://www.gutenberg.org/files/1661/1661-h/1661-h.htm',
             genre=Mystery, user=User1)
session.add(book9)
session.commit()

book10 = Book(name="The Hound of the Baskervilles", author="Arthur Conan Doyle",
              description="Based on a local legend of a spectral hound that haunted "
              "Dartmoor in Devonshire, England, the story is set in the moors at "
              "Baskerville Hall and the nearby Grimpen Mire, and the action takes "
              "place mostly at night, when the terrifying hound howls for blood.",
              cover='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNmgWh_AKWunTgr8pOoUGbdoq3uJQpbISvV2QqmTuCMgKHAoq2AQ',
              link='https://www.gutenberg.org/files/2852/2852-h/2852-h.htm',
              genre=Mystery, user=User1)
session.add(book10)
session.commit()

book11 = Book(name="Autobiography of Benjamin Franklin", author="Benjamin Franklin",
              description="he Autobiography of Benjamin Franklin is the traditional "
              "name for the unfinished record of his own life written by Benjamin "
              "Franklin from 1771 to 1790; however, Franklin himself appears to "
              "have called the work his Memoirs.",
              cover='https://images-na.ssl-images-amazon.com/images/I/61X7DcomJGL._SX339_BO1,204,203,200_.jpg',
              link='https://www.gutenberg.org/files/20203/20203-h/20203-h.htm',
              genre=Biography, user=User1)
session.add(book11)
session.commit()

book12 = Book(name="The Story of My Life", author="Helen Keller",
              description="A main theme of The Story of My Life is the power of perseverance. "
              "Helen is at a significant disadvantage in her life due to her disabilities, "
              "yet she is persistent enough to overcome these great obstacles. Another theme "
              "is the importance of role models, as Anne Sullivan's guidance changes Helen's life",
              cover='https://images-na.ssl-images-amazon.com/images/I/41IGG13YO4L.jpg',
              link='https://www.gutenberg.org/files/2397/2397-h/2397-h.htm',
              genre=Biography, user=User1)
session.add(book12)
session.commit()

book13 = Book(name="Self-Help", author="Samuel Smiles",
              description="This brilliant interpretation of samuel Smiles Self-Help is "
              "an entertaining accompaniment to one of the most famous books on self-improvement ever written.",
              cover='https://images-na.ssl-images-amazon.com/images/I/51-DU1JKYQL.jpg',
              link='https://www.gutenberg.org/files/935/935-h/935-h.htm',
              genre=SelfHelp, user=User1)
session.add(book13)
session.commit()

book14 = Book(name="Increasing Personal Efficiency",
              author="Russell H. Conwell",
              description="Some women may be superficial in education and accomplishments, extravagant "
              "in tastes, conspicuous in apparel, something more than self-assured in bearing, "
              "devoted to trivialities, inclined to frequent public places.",
              cover='https://images-na.ssl-images-amazon.com/images/I/41hMGeLZ3rL._SX335_BO1,204,203,200_.jpg',
              link='https://www.gutenberg.org/files/36898/36898-h/36898-h.htm',
              genre=SelfHelp, user=User1)
session.add(book14)
session.commit()


print "Initialised the database"
