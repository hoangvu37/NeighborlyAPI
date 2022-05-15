import json
import logging
from bson.json_util import dumps
import azure.functions as func


def main(event: func.EventGridEvent):
    data = {
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    }
    result = dumps(data)

    logging.info('Python EventGrid trigger processed an event: %s', result)
