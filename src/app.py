from flask import Flask
from flask_graphql import GraphQLView

import models.db_session as db_session
from schema.schema import schema

db_session.global_init()

session = db_session.factory()

app = Flask(__name__)
app.debug = True

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
