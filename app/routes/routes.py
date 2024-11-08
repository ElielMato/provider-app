class Route():
    
    def init_app(self, app):
        self.app = app
        from app.controllers import user_bp
        app.register_blueprint(user_bp, url_prefix='/api/v1')
        from app.controllers import home_bp
        app.register_blueprint(home_bp, url_prefix='/api/v1')
        from app.controllers import product_bp
        app.register_blueprint(product_bp, url_prefix='/api/v1')
        from app.controllers import order_bp
        app.register_blueprint(order_bp, url_prefix='/api/v1')