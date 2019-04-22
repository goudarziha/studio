from flask import Flask, render_template


def create_app(config_filename):
    app = Flask(__name__)

    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

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
    app = create_app("config")
    app.run(debug=True)
