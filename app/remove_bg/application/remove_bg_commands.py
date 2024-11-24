from remove_bg.domain.remove_bg_service import RemoveBGService


class RemoveBGCommand:
    def __init__(self, remove_bg_service: RemoveBGService):
        self.remove_bg_service = remove_bg_service

    def execute(self, content: bytes) -> bytes:
        return self.remove_bg_service.apply(content)
