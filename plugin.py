import os
import sys

plugin_dir = os.path.dirname(os.path.abspath(__file__))
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)

from artillery import artillery, init_artillery

def init_plugin(app, db, plugin_info=None):
    """Initialize the GalleryDL plugin."""
    if "artillery" not in app.blueprints:
        artillery.template_folder = os.path.join(plugin_dir, "templates")
        app.register_blueprint(artillery)
        init_artillery(app)
