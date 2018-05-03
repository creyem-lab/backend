from marshmallow import Schema, fields


class Hotspot():
    def __init__(self, _id, case_id, pitch, yaw, cssClass, createTooltipArgs):
        self._id = _id
        self.case_id = case_id
        self.pitch = pitch
        self.yaw = yaw
        self.cssClass = cssClass
        self.createTooltipArgs = createTooltipArgs

    def __repr__(self):
        return '<Hotspot(name={self.id!r})>'.format(self=self)


class HotspotSchema(Schema):
    _id = fields.Str()
    case_id = fields.Str()
    pitch = fields.Number()
    yaw = fields.Number()
    cssClass = fields.Str()
    createTooltipArgs = fields.Str()
