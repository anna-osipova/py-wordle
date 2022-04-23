from flask_failsafe import failsafe
from flask import Flask, g


@failsafe
def create_app() -> Flask:
    from app import app
    return app


if __name__ == "__main__":
    create_app().run(port=5100)
