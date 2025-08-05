from .. import ma
from marshmallow import fields, validate
from ..models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "nome", "email","senha", "admin")
      

    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=2, max=80))
    email = fields.Email(required=True)
    senha = fields.Str(load_only=True, required=True)
    admin = fields.Bool(dump_only=True)