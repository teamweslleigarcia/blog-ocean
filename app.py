from flask import Flask

app = Flask("hello")

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!!"

@app.route("/contato")
def contato():
    return """
    <html>
        <head>
            <title>Contato</title>
            <style>
                body{
                    background-color: #333;
                    color: #ffffff;
                }
                ul{
                    list-style:none
                }
            </style>
        </head>
        <ul>
            <li>Nome: Wesllei Garcia</li>
            <li>Email: wesllei.garcia@gmail.com</li>
            <li>Telefone (92) 99380-5887</li>
        </ul>
    </html>
    """