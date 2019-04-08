import pandas as pd
from goodreads import client
from credentials import key, secret

gc = client.GoodreadsClient(key, secret)

search_results = gc.search_books("Plantagenets")
search_results[1].popular_shelves
