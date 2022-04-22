from typing import Optional

from flask import Flask, g
from flask_graphql import GraphQLView

from models import db_session
from schema.schema import schema

app = Flask(__name__)
app.debug = True

session = db_session.db_init()


@app.before_request
def before_request() -> None:
    g.session = session


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        get_context=lambda: {'session': session}
    )
)

if __name__ == '__main__':
    app.run(port=5100)
