class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "manager":
            return "default"
        elif model._meta.app_label == "news_scraper":
            return "news_scraper"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "manager":
            return "default"
        elif model._meta.app_label == "news_scraper":
            return "news_scraper"
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the auth or contenttypes apps is
    #     involved.
    #     """
    #     if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
    #         return True
    #     return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "manager":
            return db == "default"
        elif app_label == "news_scraper":
            return db == "news_scraper"
        return None
