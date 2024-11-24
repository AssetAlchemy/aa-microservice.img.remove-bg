from rembg import remove, new_session

from remove_bg.domain.remove_bg_service import RemoveBGService


class RembgRemoveBGService(RemoveBGService):
    def apply(self, content: bytes, model: str = "silueta") -> bytes:
        try:
            return remove(content, session=new_session(model))
        except Exception:
            raise Exception("Error to remove background")
