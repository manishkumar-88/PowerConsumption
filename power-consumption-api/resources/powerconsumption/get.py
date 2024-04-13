from database.models.powerConsumption_model import Table
from flask_restful import Resource
from flask import request,make_response
from mongoengine.errors import DoesNotExist,ValidationError
from datetime import datetime


class PowerConsumptionResource(Resource):

    def get(self):
        try:
            start_time_str = request.args.get('startTime')
            end_time_str = request.args.get('endTime')
            value = request.args.get('value',type=float)

            # formatting start and end time for filter query
            if start_time_str is None or end_time_str is None or value is None:
                return {"message": "Invalid Parameter."}, 400
            start_time_str = start_time_str.strip() if start_time_str else ""
            end_time_str = end_time_str.strip() if end_time_str else ""
            if not start_time_str or not end_time_str:
                return {"message": "Invalid start time or end time format."}, 400
            start_time = datetime.fromisoformat(start_time_str)
            end_time = datetime.fromisoformat(end_time_str)

            # searching in db for data on filter query
            result = list(Table.objects.exclude('id')(ts__gte=start_time,ts__lte= end_time).as_pymongo())
            if len(result)==0 or result is None:
                raise DoesNotExist
            filtered_slots = []
            in_slot = False
            start_slot = None

            # Calculating time duration
            for data_point in result:
                if data_point['value'] == value:
                    if not in_slot:
                        in_slot = True
                        start_slot = data_point['ts']
                else:
                    if in_slot:
                        in_slot = False
                        end_slot = data_point['ts']
                        duration = (end_slot - start_slot).total_seconds() / 60
                        filtered_slots.append({'start': str(start_slot), 'end': str(end_slot), 'duration': str(int(duration))})
            if filtered_slots:
                return filtered_slots, 200
            else:
                raise DoesNotExist
        except DoesNotExist:
            return {"message":"No data found"},200
        except Exception as e:
            return  make_response({"message":str(e)}, 500)