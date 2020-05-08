import urllib.request,json
from .models import Quote

quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():

    with urllib.request.urlopen(quotes_url) as url:
        quotes_data = url.read()
        quotes_response = json.loads(quotes_data)

        quote_object = None
        if quotes_response:
            id = quotes_response.get('id')
            author = quotes_response.get('author')
            quote = quotes_response.get('quote')

            quote_object = Quote(id,author,quote)

    return quote_object