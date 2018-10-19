from flask import Flask, request

# flaskを継承する使い方例。
# ふつうにやると、SQLやファイルへの保存無しでは、
# アクセスごとにrequest等でpostやgetの値をもらわないと、
# 変数を保持できない。
# Flaskを継承したクラスを作ることで、
# メンバシップ変数、インスタンスでデータを保持したり、
# メソッドを追加したりできる。

# 本プログラムを実行すると、アクセスのたびに表示される数値が増える。

class SampleClass(Flask):

    def __init__(self, name):
        super().__init__(name)
        self.classValue = 0

    def index(self):
        self.incValue()
        return str(self.classValue)

    def incValue(self):
        self.classValue+=1

app = SampleClass(__name__)

@app.route("/")
def index():
    return app.index()

if __name__ == '__main__':
    app.run(debug = True)
