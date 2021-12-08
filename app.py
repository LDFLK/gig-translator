from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
import re

app = Flask(__name__)


@app.route('/', methods=['GET'])
def translate_text():
    lang = request.args.get('lang')
    text = request.args.get('text')
    output_text = ""
    translator = GoogleTranslator(source='auto', target=lang)

    if "</p>" in text:
        text_array = re.split("<<enter>>", text.replace("</p>", "</p><<enter>>"))
    else:
        text_array = re.split("<<enter>>", text.replace("\n\n", "\n\n<<enter>>"))

    translated_array = translator.translate_batch(text_array)

    for paragraph in translated_array:
        output_text = output_text + paragraph

    response = jsonify(output_text)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run()
