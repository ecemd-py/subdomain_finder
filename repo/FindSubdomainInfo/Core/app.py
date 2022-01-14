from flask import Flask, request
from DatabaseOperations import DatabaseOperations

app = Flask(__name__)
db_ops = DatabaseOperations()
description =   """
                <!DOCTYPE html>
                <head>
                <title>API Landing</title>
                </head>
                <body>  
                    <h3>API using Flask</h3>
                    <h4>Send sample request:</h4>
                    <a href="http://localhost:5000/get_info?domainName=computerhope.com">sample request</a>
                    <h4>Send request by entering domain name:</h4>
                    <form id="sendreqwithdomain">
                        Domain Name: <input type="text" id="domain" name="domain" />
                        <input type="button" value="Send Request"
                            onclick="sendRequest(document.getElementById('domain').value);" />
                    </form>
                    <script>
                        function sendRequest(value) {
                            window.open("http://localhost:5000/get_info?domainName=" + value)
                        }
                    </script>    
                    <h4>See database:</h4>   
                    <a href="http://localhost:5000/show_db">show db</a>           
                </body>
                """

@app.route('/')
def hello_world():
    return description

@app.route('/get_info', methods=["GET"])
def get_info():
    if not all(k in request.args for k in (["domainName"])):
        error_message =     f"\
                            Required paremeters : 'domainName'<br>\
                            Supplied paremeters : {[k for k in request.args]}\
                            "
        return error_message
    else:
        domain_name = request.args['domainName']
        print("INPUT:" + domain_name)
        
        result = db_ops.select_domain_data(domain_name)

        return result

@app.route('/show_db', methods=["GET"])
def show_db():
    result = db_ops.select_all_data()
    return result


if __name__ == "__main__":
	# for debugging locally
	# app.run(debug=True, host='0.0.0.0',port=5000)
	
	# for production
    app.run(host='localhost', port=5000)
