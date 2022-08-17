## Starting Eureka

The first step is to start a Eureka server. You can do this any way you’d like. The easiest way, if you have docker installed is to run the following command

```bash
docker run --name eureka-server --rm=true --detach --publish 8761:8761 medined/eureka-server:2.3.0.RELEASE
```

## Creating a Eureka Client - Flask

```bash
rest_port = 8050
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="microservice1",
                   instance_port=rest_port)
```

```bash
rest_port = 8051
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="microservice2",
                   instance_port=rest_port)
```

And if we check our Eureka Server on localhost:8761 , it's registered and ready to receive requests

## Calling Flask Microservice 2 from Microservice 1 using Eureka

With both of our services up and running, registered to Eureka and able to communicate with each other

Let's send a POST request to our End-User Service, containing some student data, which will in turn send a POST request to the Micro Service 2,retrieve the response, and forward it to us 

```bash
http://localhost:8050/call_another_service
```

## Other API's
### Microservice 1
```bash
http://localhost:8050/
http://localhost:8050/call_another_service
```

### Microservice 1
```bash
http://localhost:8051/
http://localhost:8051/calculate_grade
```