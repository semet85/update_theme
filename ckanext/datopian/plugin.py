import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint

# Helper function untuk mengembalikan semua groups
def groups_list():
    '''
    Ambil semua groups dari CKAN
    '''
    model = toolkit.model
    context = {'model': model, 'session': model.Session}
    return toolkit.get_action('group_list')(context)


def hello_plugin():
    return u'Hello from the Datopian Theme extension'


class DatopianPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'datopian')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'groups_list': groups_list,
            'hello_plugin': hello_plugin
        }

    # IBlueprint
    def get_blueprint(self):
        '''Return a Flask Blueprint object to be registered by the app.'''
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = 'templates'
        # Tambahkan route contoh
        blueprint.add_url_rule('/hello_plugin', '/hello_plugin', hello_plugin)
        return blueprint
