from flask import Flask, request
import pandas as pd
import py_eureka_client.eureka_client as eureka_client

rest_port = 8051
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="microservice2",
                   instance_port=rest_port)

app = Flask(__name__)


@app.route("/")
def microservice_2():
    return "From microservice_service_2"


@app.route("/calculate_grade", methods=['POST'])
def microservice_2_calculate_grades():
    try:
        data = request.json
        df = pd.DataFrame(data, index=[0])
        df['Sum'] = df['mathGrade'] + df['englishGrade'] + df['historyGrade'] + df['scienceGrade']
        return f'The total Marks for the student {df.loc[0,"name"]} : {df.loc[0,"Sum"]}'
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=rest_port)
