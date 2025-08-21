import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template
from ckan.model import Group  # Import model langsung dari CKAN

# Contoh helper untuk snippet
def groups_list():
    """Mengambil semua groups (categories) dari CKAN"""
    return Group.all()


def hello_plugin():
    return u'Hello from the Datopian Theme extension'


class DatopianPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):
        # Tambahkan template, public, dan assets
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'datopian')

    # IBlueprint
    def get_blueprint(self):
        """Return a Flask Blueprint object"""
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        # URL plugin
        blueprint.add_url_rule('/hello_plugin', '/hello_plugin', hello_plugin)
        return blueprint
