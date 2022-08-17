from flask import Flask, request
import py_eureka_client.eureka_client as eureka_client

rest_port = 8050
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="microservice1",
                   instance_port=rest_port)

app = Flask(__name__)


@app.route("/")
def microservice_service_1():
    return "From microservice_service_1"


@app.route("/call_another_service")
def microservice_1_invoke_another_service():
    try:
        JSON_PAYLOAD = {"name": "David", "mathGrade": 8, "englishGrade": 10, "historyGrade": 7,"scienceGrade": 10}

        res = eureka_client.do_service(app_name="service2",
                                       service="/calculate_grade",
                                       method="POST",
                                       headers={'Content-Type': 'application/json'},
                                       data=JSON_PAYLOAD
                                       )
        return f"Response from Microservice 2 ,{res}"
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=rest_port)
