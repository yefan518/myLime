from flask import Flask, request, jsonify
from flask import render_template
import random
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def run():
  return render_template('index.html')

@app.route('/upload',methods=['post'])
def upload():
  if request.method == 'POST':
    text=request.form.get('text')
    model_type = request.form.get('model_type')
  if model_type == 'model1':
    res = {}
    res['class_name'] = ["republican", "democrat"]
    res['class_proba'] = [0.9, 0.1]
    res['feature_weights'] = [["TaxReform", -0.020770347480948175], ["FoxBusiness", -0.017348559557315277], ["Chairman", -0.016276587467941726], ["FoxNews", -0.014993825621698636], ["RepKevinBrady", -0.00954154749073416], ["https", 0.007872493594009546], ["highlights", -0.004874949990182821], ["benefits", -0.004290721079843876], ["the", 0.001588871746664454], ["and", -0.0015407369063189303]]
    # [[word, index, weight]]
    res['feature_view'] = [["TaxReform", 81, -0.020770347480948175], ["FoxBusiness", 41, -0.017348559557315277], ["Chairman", 0, -0.016276587467941726], ["FoxNews", 28, -0.014993825621698636], ["RepKevinBrady", 10, -0.00954154749073416], ["https", 111, 0.007872493594009546], ["highlights", 97, -0.004874949990182821], ["benefits", 68, -0.004290721079843876], ["the", 64, 0.001588871746664454], ["and", 36, -0.0015407369063189303]]
    res['raw_str']="Chairman @RepKevinBrady on @FoxNews and @FoxBusiness to discuss the benefits of #TaxReform. Some highlights \u2b07\ufe0f https://t.co/urDcaXeWjF"
    return render_template("result.html", data = res, text = text)
  else:
    return render_template('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8888,debug = True)
