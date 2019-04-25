from flask import Flask, render_template
from time import sleep
from flask_apscheduler import APScheduler
import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.app = app
    db.init_app(app)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    @app.route('/')
    def index():
        return render_template('index.html', token='yes')

    @app.after_request
    def add_header(r):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True,
            threaded=True, use_reloader=False)
