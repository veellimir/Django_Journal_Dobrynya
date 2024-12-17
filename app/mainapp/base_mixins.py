class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "competition_name") and self.competition_name:
            return f"{self.competition_name}"
        elif hasattr(self, "name") and self.name:
            return str(self.name)
        elif hasattr(self, "title") and self.title:
            return self.title
        return super().__str__()