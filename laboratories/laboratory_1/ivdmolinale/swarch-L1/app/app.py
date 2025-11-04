from flask import Flask
from config import Config, db, migrate
import time
import os
from controllers.genre_controller import genre_bp
from controllers.book_controller import book_bp

def create_app():
    app = Flask(__name__)
    print(Config.SQLALCHEMY_DATABASE_URI)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Esperar a que la base de datos esté lista con retries
    max_retries = 10
    retry_delay = 5


    for attempt in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
                break
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Error: {str(e)}")
                time.sleep(retry_delay)
            else:
                break
    
    # Register blueprints
    app.register_blueprint(genre_bp, url_prefix="/genres")
    app.register_blueprint(book_bp, url_prefix="/books")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)