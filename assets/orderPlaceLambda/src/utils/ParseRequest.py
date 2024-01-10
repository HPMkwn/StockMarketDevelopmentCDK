import json
import base64
from exceptions.RequestParseError import RequestParseError
class RequestParcer():

    def extractBody(event):
        """Parses the JSON body of an event into a Python object."""
        try : 
            if not event.get('body'):
                return {}
            if event.get('isBase64Encoded'):
                body = base64.b64decode(event['body'])
            else:
                body = event['body']
            if isinstance(body, str):
                body = json.loads(body)
            elif not isinstance(body, dict):
                raise ValueError('Body must be a JSON object')
        except Exception as e:
            return event['body']

        return body