from .main import bp

def init_app(app):
    """Blueprint - endpoint set registration"""
    app.register_blueprint(bp, url_prefix="/api")