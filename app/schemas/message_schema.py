from .. import ma
from marshmallow import fields, validate
from ..models.message import Message
from .comment_schema import CommentSchema
from .user_schema import UserSchema

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        fields = ("id", "content", "created_at","autor", "comments")

    id = fields.Int(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1, max=140))
    created_at = fields.DateTime(dump_only=True)

    # Campo aninhado de comentários
    comments = fields.Nested(CommentSchema, many=True, dump_only=True)
    autor = fields.Nested(UserSchema, dump_only=True)