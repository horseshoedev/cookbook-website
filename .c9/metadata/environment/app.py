{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":61,"position":61,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":11},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","debug=True)"],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":2},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":3}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["f"],"id":4},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["l"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["a"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["s"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["k"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["_"],"id":5},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["p"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["y"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["m"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["o"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["n"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["g"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":[" "],"id":6},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["i"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["p"],"id":7},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["r"],"id":8},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":[" "],"id":9},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["p"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["y"],"id":10},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["m"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["o"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["n"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["g"]},{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":33},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"],"id":12},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":13},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["b"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["s"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["."],"id":14},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["b"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["j"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["e"],"id":15},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["c"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["i"],"id":16},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":[" "],"id":17},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["i"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["m"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["p"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["o"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["r"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":[" "],"id":18},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["O"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["b"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["j"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["c"],"id":19},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["t"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["I"]}],[{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["d"],"id":20}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["a"],"id":22},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["p"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["p"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["."]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["c"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["o"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["n"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["f"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["i"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["g"],"id":23}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":12},"action":"insert","lines":["[]"],"id":24}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":13},"action":"insert","lines":["\"\""],"id":25}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["M"],"id":26},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["O"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["N"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["G"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["O"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["_"],"id":27},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["D"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["B"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["N"],"id":28},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["A"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["M"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["E"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":[" "],"id":29},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":[" "],"id":30}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":31},"action":"insert","lines":["''"],"id":31}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":11},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","debug=True)"],"id":32},{"start":{"row":0,"column":0},"end":{"row":22,"column":11},"action":"insert","lines":["","import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":33}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["t"],"id":34},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["a"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["s"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["k"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["_"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["m"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["a"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["n"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["a"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["g"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["e"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["r"],"id":35}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["c"],"id":36},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["o"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["o"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["k"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["_"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["b"]}],[{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["o"],"id":37},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["o"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["k"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":71},"action":"remove","lines":["os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":38}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":28},"action":"insert","lines":["\"\""],"id":39}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":28},"action":"remove","lines":["\"\""],"id":40}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":28},"action":"insert","lines":["''"],"id":41}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":122},"action":"insert","lines":["mongodb+srv://root:<password>@myfirstcluster-vay7y.mongodb.net/test?retryWrites=true&w=majority"],"id":42}],[{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"remove","lines":[">"],"id":43},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"remove","lines":["d"]},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"remove","lines":["r"]},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"remove","lines":["o"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"remove","lines":["w"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"remove","lines":["s"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"remove","lines":["s"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"remove","lines":["a"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"remove","lines":["p"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"remove","lines":["<"]}],[{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["r"],"id":44},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["o"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["o"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":87},"end":{"row":7,"column":88},"action":"remove","lines":["t"],"id":45},{"start":{"row":7,"column":86},"end":{"row":7,"column":87},"action":"remove","lines":["s"]},{"start":{"row":7,"column":85},"end":{"row":7,"column":86},"action":"remove","lines":["e"]},{"start":{"row":7,"column":84},"end":{"row":7,"column":85},"action":"remove","lines":["t"]}],[{"start":{"row":7,"column":84},"end":{"row":7,"column":85},"action":"insert","lines":["c"],"id":46},{"start":{"row":7,"column":85},"end":{"row":7,"column":86},"action":"insert","lines":["o"]},{"start":{"row":7,"column":86},"end":{"row":7,"column":87},"action":"insert","lines":["o"]},{"start":{"row":7,"column":87},"end":{"row":7,"column":88},"action":"insert","lines":["k"]},{"start":{"row":7,"column":88},"end":{"row":7,"column":89},"action":"insert","lines":["_"]},{"start":{"row":7,"column":89},"end":{"row":7,"column":90},"action":"insert","lines":["b"]}],[{"start":{"row":7,"column":90},"end":{"row":7,"column":91},"action":"insert","lines":["o"],"id":47},{"start":{"row":7,"column":91},"end":{"row":7,"column":92},"action":"insert","lines":["o"]},{"start":{"row":7,"column":92},"end":{"row":7,"column":93},"action":"insert","lines":["k"]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["k"],"id":49}],[{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["s"],"id":50},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["a"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["s"],"id":51}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["r"],"id":52},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["e"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["c"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["i"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["p"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["e"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["s"],"id":53},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["k"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["s"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["a"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["r"],"id":54},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["e"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["c"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["i"],"id":55},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["p"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["e"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["a"],"id":56},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["s"],"id":57},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["k"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["r"],"id":58},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["e"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":32},"action":"remove","lines":["recs"],"id":59},{"start":{"row":15,"column":28},"end":{"row":15,"column":35},"action":"insert","lines":["recipes"]}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":48},"action":"remove","lines":["tasks"],"id":60},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["r"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["e"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":46},"action":"remove","lines":["rec"],"id":61},{"start":{"row":15,"column":43},"end":{"row":15,"column":50},"action":"insert","lines":["recipes"]}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":65},"action":"remove","lines":["tasks"],"id":62},{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["r"]},{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["e"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":63},"action":"remove","lines":["rec"],"id":63},{"start":{"row":15,"column":60},"end":{"row":15,"column":67},"action":"insert","lines":["recipes"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":67},"end":{"row":15,"column":67},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1561681559734,"hash":"51e2b939db4d1d924d565df3eccaa58faae943eb"}