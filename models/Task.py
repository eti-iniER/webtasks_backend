from marshmallow import Schema, fields


class TaskSchema(Schema):
    "buildOrQuit": fields.Str()
    "name": fields.Str()
    "description": fields.Str()
    "type": fields.Str()
    "emoji": fields.Str()
    "theme": fields.Str()
    "start": fields.Str()
    "goal": fields.Int()
    "weekdays": fields.Dict()
    "frequency": fields.Str()
    "seconds": fields.Str()
    "minutes": fields.Str()
    "hours": fields.Str()
    "occurence": fields.Int()
