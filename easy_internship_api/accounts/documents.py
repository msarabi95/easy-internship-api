import mongoengine as mongo

mongo.connect('easy_internship_api')

class ProfileField(mongo.EmbeddedDocument):
    name = mongo.StringField()
    mongo_class = mongo.StringField()

class ProfileSchema(mongo.Document):
    name = mongo.StringField()
    fields = mongo.EmbeddedDocumentListField(ProfileField)
