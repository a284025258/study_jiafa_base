from flask import Flask


# 默认运行地址：http://127.0.0.1:5000/
# 创建服务
app = Flask(__name__)

# 指定根目录（必须）
@app.route('/')
def index():
    return 'hello world'

# 指定其他地址（可选）
@app.route('/login', methods=['post', 'get'])
def login():
    return 'log in the world'

# 运行服务 debug 开启debug模式，修改代码会重新部署
app.run(debug=True)
