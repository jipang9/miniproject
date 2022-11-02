from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.idcaqc8.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 루트 경로 -> 메인화면
@app.route('/')
def home():
    return render_template('index.html')

# 페이지 이동부분
@app.route('/jihwan')
def mypage_jihwan():
    return render_template('jihwan.html')

@app.route('/miran')
def mypage_miran():
    return render_template('miran.html')

@app.route('/donghyun')
def mypage_donghyun():
    return render_template('donghyun.html')

@app.route('/sangwook')
def mypage_sangwook():
    return render_template('sangwook.html')


#  데이터 전송(url 확인할 것)
@app.route('/jihwan/post', methods = ["POST"])
def comment_post():
    id_receive = request.form['id_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    post = {
        'id':id_receive,
        'name':name_receive,
        'comment':comment_receive
    }
    db.myComment.insert_one(post)

    return jsonify({'msg':'방명록 작성 감사합니다.'})

@app.route('/jihwan/get', methods=["GET"])
def comment_get():
    content_list=list(db.myComment.find({},{'_id':False}))
    return jsonify({'comment':content_list})

@app.route('/jihwan/delete',methods=["DELETE"])
def comment_delete():
    id_receive=request.form['id_delete']
    db.myComment.delete_one({'id':id_receive})
    return render_template('jihwan.html')



@app.route("/miran/post", methods=["POST"])
def miniproject_post():
   name_receive = request.form["name_give"]
   comment_receive = request.form["comment_give"]
   doc = {
       'name': name_receive,
       'comment': comment_receive
   }
   db.mirancomment.insert_one(doc)
   return jsonify({'msg': '방명록이 작성되었습니다'})

@app.route("/miran/get", methods=["GET"])
def miniproject_get():
    comment_list = list(db.mirancomment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/donghyun/post", methods=["POST"])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.dongComment.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@app.route("/donghyun/get", methods=["GET"])
def homework_get():
    comment_list = list(db.dongComment.find({},{'_id':False}))
    return jsonify({'comments':comment_list})

@app.route('/sangwook/get', methods=['GET'])
def comments_get():
   comment_list = list(db.sangComment.find({}, {'_id': False}))
   return jsonify({'comments': comment_list})

@app.route('/sangwook/post', methods=['POST'])
def comments_post():
   name_receive = request.form['name_give']
   comment_receive = request.form['comment_give']

   doc = {
      'name':name_receive,
      'comment':comment_receive
   }
   db.sangComment.insert_one(doc)

   return jsonify({'result':'success', 'msg': '등록 완료!'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
