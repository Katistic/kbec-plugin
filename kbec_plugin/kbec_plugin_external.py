from .kbec_plugin import KbecPlugin

class KBecPluginExternal(KbecPlugin):
    def __init__(self, config_path: str, kbec_client: object, ftp_manager: object):
        super().__init__(config_path, kbec_client)
        self._ftp_manager = ftp_manager