"""
An API used to make calls to the Main app modules
"""
from flask import Flask
from flask_restx import Api, Resource, fields
from Main import main  # Importing the main function we created earlier
import logging

# Determine logger format and create separate logger file
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\python\\Varanpy.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()

# Determine logger messages and arrange them by the 5 levels of severity
logger.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print(logger.level)

app = Flask(__name__)
api = Api(app, version='1.0', title='Transcript Analysis API', description='An API to analyze transcript data')

transcript_model = api.model('Transcript', {
    'transcript_id': fields.String(required=True, description='The transcript ID (ENST or NM_)')
})

result_model = api.model('Result', {
    'module3_output': fields.String(description='Output from module3'),
    'module4_output': fields.String(description='Output from module4'),
    'module5_output': fields.String(description='Output from module5')
})

@api.route('/analyze')
class TranscriptAnalysis(Resource):
    @api.expect(transcript_model)
    @api.marshal_with(result_model)
    def post(self):
        data = api.payload
        transcript_id = data['transcript_id']
        result = main(transcript_id)
        return result

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)  # Specify a host and port for the app
