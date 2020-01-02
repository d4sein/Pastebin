from app import ma

from app.paste.models.paste_model import Paste


class PasteSchema(ma.ModelSchema):
    class Meta:
        model = Paste
        include_fk = True
