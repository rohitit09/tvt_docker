import sys
import json
from flask import Flask,request,jsonify
app=Flask(__name__)

def main(a,b,c):
    '''
    params
        a: int
        b: int
        c: int
    return 
        sum : sum of above number based on condition
    '''
    temp=[13,14,17,18,19]
    sum=a+b+c
    sum= sum-a if a in temp else sum
    sum= sum-b if b  in temp else sum
    sum= sum-c if c  in temp else sum
    return sum


@app.route('/')
def index():
    return jsonify({'hello': 'test'})

@app.route('/sum',methods=['PUT'])
def sum():
    try:
        a,b,c=json.loads(request.data)
    except json.decoder.JSONDecodeError as et:
        return jsonify({"status": 400, "error": 'input format not correct'})
    except ValueError as e:
        return jsonify({"status": 400, "error": 'Exactly 3 numbers are required'})
    else:
        try:
            a,b,c=map(int,[a,b,c])
        except ValueError as es:
            return jsonify({"status": 400, "error": 'All inputs must be numeric'})
        else:
            result=main(a,b,c)
            return jsonify({"status": 200, "result": result})


if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)


