from resources.powerconsumption.get import PowerConsumptionResource

def initialize_routes(api):
    # routes for the power consumption service
    api.add_resource(
        PowerConsumptionResource, "/api/v1/data",
    )