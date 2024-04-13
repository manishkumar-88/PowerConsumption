from flask_restful import Api
from flask import Flask
from database.connect import initialize_db,DB_URI
from resources.routes import initialize_routes

app=Flask(__name__)
app.config['MONGODB_SETTINGS'] ={'host':DB_URI}
api=Api(app)

#db and route initialized
initialize_db()
initialize_routes(api)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug=True) 
