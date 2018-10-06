from . import golime


_playground = None
GOLIME_DAEMON_URL = "http://localhost:8601/cmd"


def plugin_loaded():
    golime.start_golime()


def plugin_unloaded():
    golime.stop_golime()
