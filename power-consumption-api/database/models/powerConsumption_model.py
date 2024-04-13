from mongoengine import Document,DateTimeField,StringField,IntField,FloatField
from database.connect import collection

# we can define the model of the collection here
class Table(Document):
    ts =DateTimeField()
    Global_active_power =FloatField()
    Global_reactive_power=FloatField()
    Voltage=FloatField()
    Global_intensity=FloatField()
    Sub_metering_1 =IntField()
    value=IntField()
    Sub_metering_3=IntField()
    meta={
        'collection':collection,
    }
