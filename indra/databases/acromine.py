import requests
from indra import has_config, get_config

acromine_url = 'http://nactem.ac.uk/AcromineDisambiguationV2/' \
               'services/rest/disambiguate'

# Try to read the API key from a file
if not has_config('ACROMINE_API_KEY'):
    logger.error('Acromine API key could not be found in config file or ' + \
                 'environment variable.')
else:
    api_key = get_config('ACROMINE_API_KEY')


text = 'ER has also been shown to inhibit p53 degradation by HDM2 via direct binding to p53 and HDM2.'

data = {'key': api_key, 'text': text}

resp = requests.post(acromine_url, data)
