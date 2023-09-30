from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        selected_option = request.form['dropdown']
        hidden_id = request.form['id']
        textbox_content = request.form['textbox']

        # Process the data (you can add your logic here)

        # Sample JSON response with selected content and hidden ID
        response_data = {
            'id': hidden_id,
            'selected_option': selected_option,
            'textbox_content': textbox_content
        }

        return jsonify(response_data)
    else:
        return render_template('ss.html')

if __name__ == '__main__':
    app.run(debug=True)
