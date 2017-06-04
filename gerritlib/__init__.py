from .gerrit import Gerrit, GerritWatcher
from . import version

__version__ = version.version_info.version_string_with_vcs()
