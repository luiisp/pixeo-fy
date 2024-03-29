from django.apps import AppConfig


class UsrpixeoConfig(AppConfig):
    """
    AppConfig class for the 'usrpixeo' app.

    This class represents the configuration for the 'usrpixeo' app in the Django project.
    It specifies the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The default auto field to use for models in the app.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usrpixeo'
