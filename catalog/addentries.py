from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

from database_setup import Authors, Base, Books

engine = create_engine('sqlite:///library.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
author1 = Authors(name="Steven King")

session.add(author1)
session.commit()


books1 = Books(title="Carrie", cover_url = "https://upload.wikimedia.org/wikipedia/en/3/31/Carrienovel.jpg",
		isbn=978085086950, description="Carrie is an American epistolary novel and author Stephen King's first published novel, released on April 5, 1974, with an approximate first print-run of 30,000 copies. Set in the then-future year of 1979, it revolves around the eponymous Carrietta N. \"Carrie\" White, a misfit and bullied high school girl who uses her newly discovered telekinetic powers to exact revenge on those who torment her, while in the process causing one of the worst local disasters in American history. King has commented that he finds the work to be \"raw\" and \"with a surprising power to hurt and horrify.\" It is one of the most frequently banned books in United States schools.[2] Much of the book is written in an epistolary structure, using newspaper clippings, magazine articles, letters, and excerpts from books to tell how Carrie destroyed the fictional town of Chamberlain, Maine while exacting revenge on her sadistic classmates.",
		published_date=datetime.date(1974,4,5), authors=author1)

session.add(books1)
session.commit()

books2 = Books(title="The Shining", cover_url = "https://upload.wikimedia.org/wikipedia/en/4/4c/Shiningnovel.jpg",
		isbn=9780385121675, description="The Shining centers on the life of Jack Torrance, an aspiring writer and recovering alcoholic who accepts a position as the off-season caretaker of the historic Overlook Hotel in the Colorado Rockies. His family accompanies him on this job, including his young son Danny, who possesses \"the shining,\" an array of psychic abilities that allow Danny to see the hotel's horrific past. Soon, after a winter storm leaves them snowbound, the supernatural forces inhabiting the hotel influence Jack's sanity, leaving his wife and son in incredible danger.",
		published_date=datetime.date(1977,1,28),authors=author1)

session.add(books2)
session.commit()

books3 = Books(title="The Stand", cover_url = "https://upload.wikimedia.org/wikipedia/en/9/96/The_Stand_cover.jpg",
		isbn=9780385121682, description="The Stand is a post-apocalyptic horror/fantasy novel by American author Stephen King. It expands upon the scenario of his earlier short story, \"Night Surf\". The novel was originally published in 1978 and was later re-released in 1990 as The Stand: The Complete & Uncut Edition; King restored some text originally cut for brevity, added and revised sections, changed the setting of the story from 1980 (which in turn was changed to 1984 for the original paperback release in 1980) to 1990, and updated a few pop culture references accordingly. The Stand was nominated for the World Fantasy Award for Best Novel in 1979, and was adapted into both a television miniseries for ABC and a graphic novel published by Marvel Comics. It marks the first appearance of Randall Flagg, King's recurring antagonist, whom King would bring back many times in his later writings.",
		published_date=datetime.date(1978, 9, 1), authors=author1)

session.add(books3)
session.commit()

books4 = Books(title="Misery", cover_url = "https://upload.wikimedia.org/wikipedia/en/6/6f/Stephen_King_Misery_cover.jpg",
		isbn=9780670813643, description="Misery is a 1987 psychological horror novel by Stephen King. The novel was nominated for the World Fantasy Award for Best Novel in 1988, and was later made into a Hollywood film and an off-Broadway play of the same name. When King was writing Misery in 1985 he planned the book to be released under the pseudonym Richard Bachman but the identity of the pseudonym was discovered before the release of the book. The novel focuses on Paul Sheldon, a writer famous for Victorian-era romance novels involving the character of Misery Chastain. One day he is rescued from a car crash by crazed fan Annie Wilkes, who transports him to her home and, once finding out what he has done to Misery in his latest book, forces him to write a new book modifying the story - no matter what it takes.",
		published_date=datetime.date(1987, 6, 8), authors=author1)

session.add(books4)
session.commit()

books5 = Books(title="It", cover_url = "https://upload.wikimedia.org/wikipedia/en/5/5a/It_cover.jpg",
		isbn=670813028, description=" The story follows the exploits of seven children as they are terrorized by the eponymous being which exploits the fears and phobias of its victims in order to disguise itself while hunting its prey. It primarily appears in the form of a clown in order to attract its preferred prey of young children. The novel is told through narratives alternating between two time periods, and is largely told in the third person omniscient mode. It deals with themes that eventually became King staples the power of memory, childhood trauma, and the ugliness lurking behind a facade of traditional small town values.",
		published_date=datetime.date(1986, 9, 1), authors=author1)

session.add(books5)
session.commit()

books6 = Books(title="Under the Dome", cover_url = "https://upload.wikimedia.org/wikipedia/en/0/09/Under_the_Dome_Final.jpg",
		isbn=9781439148501, description="Under the Dome is a science fiction novel by Stephen King published in November 2009. Set in and around a small Maine town, it tells an intricate, multi character and point of view story of how the town's inhabitants contend with the calamity of being suddenly cut off from the outside world by an impassable, invisible barrier that literally drops out of a clear blue sky.",
		published_date=datetime.date(2009, 11, 10), authors=author1)

session.add(books6)
session.commit()


# Menu for Super Stir Fry
author2 = Authors(name="Ray Bradbury")

session.add(author2)
session.commit()


books1 = Books(title="Fahrenheit 451", cover_url = "https://upload.wikimedia.org/wikipedia/en/d/db/Fahrenheit_451_1st_ed_cover.jpg",
		isbn=9780743247221, description="Fahrenheit 451 is a dystopian novel by Ray Bradbury published in 1953. It is regarded as one of his best works. The novel presents a future American society where books are outlawed and \"firemen\" burn any that are found. The title refers to the temperature that Bradbury understood to be the autoignition point of paper.",
		published_date=datetime.date(1953, 1, 1), authors=author2)

session.add(books1)
session.commit()

books3 = Books(title="The Martian Chronicles", cover_url = "https://upload.wikimedia.org/wikipedia/en/4/45/The-Martian-Chronicles.jpg",
		isbn=0, description="The Martian Chronicles is a 1950 science fiction short story collection by Ray Bradbury that chronicles the colonization of Mars by humans fleeing from a troubled and eventually atomically devastated Earth, and the conflict between aboriginal Martians and the new colonists. The book lies somewhere in between a short story collection and an episodic novel, containing stories Bradbury originally published in the late 1940s in science fiction magazines. The stories were loosely woven together with a series of short, interstitial vignettes for publication.",
		published_date=datetime.date(1950,1,1), authors=author2)

session.add(books3)
session.commit()

books4 = Books(title="Something Wicked This Way Comes", cover_url = "https://upload.wikimedia.org/wikipedia/en/2/22/Something_wicked_this_way_comes_first.jpg",
		isbn=671679600, description="Something Wicked This Way Comes is a 1962 fantasy novel by Ray Bradbury. It is about 13-year-old best friends, Jim Nightshade and William Halloway, and their nightmarish experience with a traveling carnival that comes to their Midwestern town on one October. The carnival's leader is the mysterious \"Mr. Dark\" who seemingly wields the power to grant the citizenry's secret desires. In reality, Dark is a malevolent being who lures these individuals into binding themselves in servitude to him. He is revealed to possess a tattoo bearing the likeness of each person he has thus tricked. Mr. Dark's presence is countered by that of Will's father, Charles Halloway, who harbors his own secret desire to regain his youth because he feels as though he is too old for Will.",
		published_date=datetime.date(1962, 1, 1), authors=author2)

session.add(books4)
session.commit()

# Menu for Panda Garden
author1 = Authors(name="Robert A. Heinlein")

session.add(author1)
session.commit()


books1 = Books(title="For Us, The Living: A Comedy of Customs", cover_url = "https://upload.wikimedia.org/wikipedia/en/d/de/RobertAHeinlein_ForUsTheLiving.jpg",
		isbn=74325998, description="For Us, The Living: A Comedy of Customs is a science fiction novel by Robert A. Heinlein, written in 1938 but published for the first time in 2003.[1] Heinlein admirer and science fiction author Spider Robinson titled his introductory essay \"RAH DNA\", as he believes this first, unpublished novel formed the DNA of Heinlein's later works.",
		published_date=datetime.date(2003, 11, 28), authors=author1)

session.add(books1)
session.commit()

books2 = Books(title="Rocket Ship Galileo", cover_url = "https://upload.wikimedia.org/wikipedia/en/4/42/Rsg48hc.jpg",
		isbn=0, description="Rocket Ship Galileo is a science fiction novel by Robert A. Heinlein, published in 1947, about three teenagers who participate in a pioneering flight to the Moon. It was the first in the Heinlein juveniles, a long and successful series of science fiction novels published by Scribner's. The novel was originally envisioned as the first of a series of books called \"Young Rocket Engineers\". It was initially rejected by publishers, because going to the moon was \"too far out\"",
		published_date=datetime.date(1947,5,1), authors=author1)

session.add(books2)
session.commit()

books3 = Books(title="Starship Troopers", cover_url = "https://upload.wikimedia.org/wikipedia/en/f/ff/St59.jpg",
		isbn=450025764, description="The first-person narrative is about a young soldier named Juan \"Johnnie\" Rico and his exploits in the Mobile Infantry, a futuristic military service branch equipped with powered armor. Rico's military career progresses from recruit to non-commissioned officer and finally to officer against the backdrop of an interstellar war between mankind and an arachnoid species known as \"the Bugs\". Rico and the other characters discuss moral and philosophical aspects of suffrage, civic virtue, juvenile delinquency, corporal punishment, capital punishment, and war.",
		published_date=datetime.date(1959, 12, 1), authors=author1)

session.add(books3)
session.commit()

books4 = Books(title="The Cat Who Walks Through Walls", cover_url = "https://upload.wikimedia.org/wikipedia/en/1/12/The_Cat_Who_Walks_Through_Walls.bookcover.amazon.jpg",
		isbn=399131035, description="The Cat Who Walks Through Walls is a science fiction novel by Robert A. Heinlein published in 1985. Like many of his later novels, it features Lazarus Long and Jubal Harshaw as supporting characters.",
		published_date=datetime.date(1985, 1, 1), authors=author1)

session.add(books4)
session.commit()


# Menu for Thyme for that
author1 = Authors(name="Sir Terry Pratchett")

session.add(author1)
session.commit()


books1 = Books(title="The Colour of Magic", cover_url = "https://upload.wikimedia.org/wikipedia/en/4/4d/The_Colour_of_Magic_%28cover_art%29.jpg",
		isbn=86140324, description="The Colour of Magic (also known as The Color of Magic) is a 1983 comic fantasy novel by Terry Pratchett, and is the first book of the Discworld series. The first printing of the British edition consisted of 506 copies. Pratchett has described it as \"an attempt to do for the classical fantasy universe what Blazing Saddles did for Westerns.\"",
		published_date=datetime.date(1983, 12, 24), authors=author1)

session.add(books1)
session.commit()

books2 = Books(title="Good Omens", cover_url = "https://upload.wikimedia.org/wikipedia/en/0/0a/Goodomenscover.jpg",
		isbn=57504800, description="Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch (1990) is a World Fantasy Award-nominated novel written in collaboration between the English authors Terry Pratchett and Neil Gaiman. The book is a comedy about the birth of the son of Satan, the coming of the End Times, and the attempts of the angel Aziraphale and the demon Crowley to avert them, having become accustomed to their comfortable situations in the human world. A subplot features the growing up of the Antichrist, Adam, and his gang, and the gathering of the Four Horsepersons of the Apocalypse. In 2003, the novel was listed at number 68 on the BBC's survey The Big Read.",
		published_date=datetime.date(1990, 5, 1), authors=author1)

session.add(books2)
session.commit()

books3 = Books(title="Nation", cover_url = "https://upload.wikimedia.org/wikipedia/en/5/5c/Terry_Pratchett_Nation.jpg",
		isbn=9780385613705, description="Nation is a novel by Terry Pratchett, published in the UK on 11 September 2008. It was the first non-Discworld Pratchett novel since Johnny and the Bomb (1996). Nation is a low fantasy set in an alternative history of our world in the 1860s. The book received recognition as a Michael L. Printz Honor Book for 2009.",
		published_date=datetime.date(2008,9,11), authors=author1)

session.add(books3)
session.commit()

author1 = Authors(name="H. P. Lovecraft")

session.add(author1)
session.commit()


books1 = Books(title="The Call of Cthulhu", cover_url = "https://upload.wikimedia.org/wikipedia/commons/a/af/Weird_Tales_February_1928.jpg",
		isbn=0, description="\"The Call of Cthulhu\" is a short story by American writer H. P. Lovecraft. Written in the summer of 1926, it was first published in the pulp magazine Weird Tales, in February 1928.",
		published_date=datetime.date(1928, 2, 1),  authors=author1)

session.add(books1)
session.commit()

books2 = Books(title="The Shadow Out of Time", cover_url = "https://upload.wikimedia.org/wikipedia/en/e/e3/ShadowOutOfTime.jpg",
		isbn=0, description="The Shadow Out of Time is a novella by American horror fiction writer H. P. Lovecraft. Written between November 1934 and February 1935, it was first published in the June 1936 issue of Astounding Stories.",
		published_date=datetime.date(1936, 6, 1), authors=author1)

session.add(books2)
session.commit()

books3 = Books(title="At the Mountains of Madness", cover_url = "https://upload.wikimedia.org/wikipedia/en/f/fc/Lovecraft%2C_Mountains_of_Madness.jpg",
		isbn=0, description="The story details the events of a disastrous expedition to the Antarctic continent in September of 1930 and what was found there by a group of explorers led by the narrator, Dr. William Dyer of Miskatonic University. Throughout the story, Dyer details a series of previously untold events in the hope of deterring another group of explorers who wish to return to the continent.",
		published_date=datetime.date(1936, 4, 1), authors=author1)

session.add(books3)
session.commit()

# Menu for Auntie Ann's
author1 = Authors(name="George Orwell")

session.add(author1)
session.commit()

books9 = Books(title="The Road to Wigan Pier", cover_url = "https://upload.wikimedia.org/wikipedia/en/d/dc/Road_to_wigan_pier.jpg",
		isbn=9780141185293, description="The Road to Wigan Pier is a book by the British writer George Orwell, first published in 1937. The first half of this work documents his sociological investigations of the bleak living conditions among the working class in Lancashire and Yorkshire in the industrial north of England before World War II. The second half is a long essay on his middle-class upbringing, and the development of his political conscience, questioning British attitudes towards socialism. Orwell states plainly that he himself is in favour of socialism; but feels it necessary to point out reasons why many people who would benefit from socialism, and should logically support it, are in practice likely to be strong opponents.",
		published_date=datetime.date(1937, 3, 8), authors=author1)

session.add(books9)
session.commit()


books1 =Books(title="Homage to Catalonia", cover_url = "https://upload.wikimedia.org/wikipedia/en/b/b6/Homage_to_Catalonia%2C_Cover%2C_1st_Edition.jpg",
		isbn=0, description="Homage to Catalonia is George Orwell\'s personal account of his experiences and observations in the Spanish Civil War. The first edition was published in the United Kingdom in 1938. The book was not published in the United States until February 1952, when it appeared with an influential preface by Lionel Trilling. The only translation published in Orwell\'s lifetime was into Italian, in December 1948. A French translation by Yvonne Davet with whom Orwell corresponded, commenting on her translation and providing explanatory notes in 1939 was not published until five years after Orwell\'s death.",
		published_date=datetime.date(1938, 4, 25),authors=author1)

session.add(books1)
session.commit()

books2 = Books(title="Animal Farm", cover_url = "https://upload.wikimedia.org/wikipedia/commons/f/fb/Animal_Farm_-_1st_edition.jpg",
		isbn=9780452284241, description="Animal Farm is an allegorical and dystopian novella by George Orwell, first published in England on 17 August 1945. According to Orwell, the book reflects events leading up to the Russian Revolution of 1917 and then on into the Stalin era in the Soviet Union. Orwell, a democratic socialist, was a critic of Joseph Stalin and hostile to Moscow-directed Stalinism, an attitude that was critically shaped by his experiences during the Spanish Civil War. The Soviet Union, he believed, had become a brutal dictatorship, built upon a cult of personality and enforced by a reign of terror. In a letter to Yvonne Davet, Orwell described Animal Farm as a satirical tale against Stalin (\"un conte satirique contre Staline\"),[4] and in his essay \"Why I Write\" (1946), he wrote that Animal Farm was the first book in which he had tried, with full consciousness of what he was doing, \"to fuse political purpose and artistic purpose into one whole\".",
		published_date=datetime.date(1945, 8, 17), authors=author1)

session.add(books2)
session.commit()

books3 = Books(title="Nineteen Eighty-Four", cover_url = "https://upload.wikimedia.org/wikipedia/en/c/c3/1984first.jpg",
		isbn=9780547249643, description="The tyranny is epitomised by Big Brother, the Party leader who enjoys an intense cult of personality but who may not even exist. The Party \"seeks power entirely for its own sake. It is not interested in the good of others; it is interested solely in power.\" The protagonist of the novel, Winston Smith, is a member of the Outer Party, who works for the Ministry of Truth (or Minitrue), which is responsible for propaganda and historical revisionism. His job is to rewrite past newspaper articles, so that the historical record always supports the party line. Smith is a diligent and skillful worker but he secretly hates the Party and dreams of rebellion against Big Brother.",
		published_date=datetime.date(1949, 6, 8), authors=author1)

session.add(books3)
session.commit()


# Menu for Cocina Y Amor
author1 = Authors(name="Orson Scott Card")

session.add(author1)
session.commit()


books1 = Books(title="Ender\'s Game", cover_url = "https://upload.wikimedia.org/wikipedia/en/e/e4/Ender%27s_game_cover_ISBN_0312932081.jpg",
		isbn=312932081, description="Ender's Game is a 1986 military science fiction novel by American author Orson Scott Card. Set in Earth's future, the novel presents an imperiled mankind after two conflicts with the \"buggers\", an insectoid alien species. In preparation for an anticipated third invasion, children, including the novel's protagonist, Ender Wiggin, are trained from a very young age through increasingly difficult games including some in zero gravity, where Ender's tactical genius is revealed.",
		published_date=datetime.date(1985, 1, 15), authors=author1)

session.add(books1)
session.commit()

books2 = Books(title="Seventh Son", cover_url = "https://upload.wikimedia.org/wikipedia/en/9/9d/SeventhSon%281stEd%29.jpg",
		isbn=312930194, description="Seventh Son (1987) is an alternate histor, fantasy novel by Orson Scott Card. It is the first book in Card\'s The Tales of Alvin Maker series and is about Alvin Miller, the seventh son of a seventh son. Seventh Son won a Locus Award and was nominated for both the Hugo and World Fantasy Awards in 1988. Seventh sons have strong \"knacks\" (specific magical abilities), and seventh sons of seventh sons are both extraordinarily rare and powerful. In fact, young Alvin appears to be the only one in the world. His abilities make him the target of The Unmaker, who recognizes Alvin\'s powers as those of a Maker only the second ever, and it had been a long time since the first had walked on water and turned water to wine. The Unmaker works largely through water, trying to kill Alvin in his early years, before he can master his abilities.",
		published_date=datetime.date(1987, 1, 1), authors=author1)

session.add(books2)
session.commit()
