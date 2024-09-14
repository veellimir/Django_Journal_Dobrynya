class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "name"):
            return str(self.name)
        elif hasattr(self, "title"):
            return self.title
        return super().__str__()