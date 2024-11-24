from rembg import remove

from remove_bg.domain.remove_bg_service import RemoveBGService


class RembgRemoveBGService(RemoveBGService):
    def apply(self, content: bytes) -> bytes:
        try:
            return remove(content)
        except Exception:
            raise Exception("Error to remove background")
