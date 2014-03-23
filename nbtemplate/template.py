from __future__ import absolute_import
import sys, os
import jinja2
from IPython.core.release import version_info as IPYTHON_VERSION

if IPYTHON_VERSION[0] == 2:
    import IPython.nbconvert.exporters.templateexporter as t_exporter
    TemplateExporter = t_exporter.TemplateExporter
elif IPYTHON_VERSION[0] == 1:
    import IPython.nbconvert.exporters.exporter as t_exporter
    TemplateExporter = t_exporter.Exporter
else: pass

class Template(TemplateExporter):
    default_preprocessors = [] # iPython 2.x
    default_transformers = [] # iPython 1.x
    def __init__(self, template_path, preprocessors=[], filters={}, skip_default_filters=False, **kw):
        template_abspath = os.path.abspath(template)
        self.template_dir, self.template_name = os.path.split(template_abspath)
        self.preprocessors = preprocessors # iPython 2.x
        self.transformers = preprocessors # iPython 1.x
        if skip_default_filters: t_exporter.default_filters = {}
        self.filters = filters # In addition to default_filters
        super(Template, self).__init__(**kw)
        self._set_template(template)

    def _init_environment(self, extra_loaders=None):
        """Overrides TemplateExporter's _init_environment method,
        to simplify things, to load only the skeleton templates
        (and not the default templates) by name, and to give the 
        skeleton templates precedence over local templates."""
        module_dir = os.path.dirname(os.path.realpath(t_exporter.__file__))
        loader = jinja2.FileSystemLoader([
            os.path.join(module_dir, self.template_skeleton_path),
            self.template_dir
        ])
        self.environment = jinja2.Environment(
            loader=loader,
            extensions=t_exporter.JINJA_EXTENSIONS
        )
        
    def _set_template(self, name):
        """A simplified alternative to TemplateExporter's
        _load_template, which tries to match variations on the
        template name."""
        self.template = None
        self.log.debug("Loading template %s", name)
        self.template = self.environment.get_template(name)
        return self

# Method alignment 
if IPYTHON_VERSION[0] == 1:
    Template.register_preprocessor = Template.register_transformer
