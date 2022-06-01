from app.extensions.schema import ma
from app.models.tracks import Track


class TrackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track

    id = ma.auto_field(dump_only=True)

class TrackAlbumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track

    id = ma.auto_field()
    name = ma.auto_field()
    albums = ma.List(ma.Nested("AlbumSchema", exclude=("track",)))
