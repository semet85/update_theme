import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.model import Group

class DatopianPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)  # <- penting

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')

    # IBlueprint
    def get_blueprint(self):
        from flask import Blueprint
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        return blueprint

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'groups_list': self.groups_list  # daftarkan ke Jinja
        }

    # Fungsi helper
    def groups_list(self):
        return list(Group.all())
