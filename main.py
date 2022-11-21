from flask import Flask, jsonify

app=Flask(__name__)

books_db=[
    {
        'name':'secret',
        'price':250

    },
    {
        'name':'deep work',
        'price':350
    }
    

]
#retrieve all the books
@app.route('/')
def home():
    return jsonify({'message':'welcome'})

@app.route('/on')
def on():
    return jsonify({'state':'1'})

@app.route('/off')
def off():
    return jsonify({'state':'0'})



#retrieve one book
app.run(port=5500)
   