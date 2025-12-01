from flask import Flask, render_template, request
import pandas as pd
from analysis import create_butterfly_plot 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    stats_html = None
    error_message = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        
        file = request.files['file']
        
        if file.filename == '':
            error_message = "Please select a file before clicking upload."
        
        else:
            try:
                df = pd.read_csv(file)
                
                plot_url = create_butterfly_plot(df)

                stats_html = df.describe().to_html(classes='table table-striped table-bordered')

            except Exception as e:
                error_message = f"Error processing file: {str(e)}"

    return render_template('index.html', plot_url=plot_url, stats=stats_html, error=error_message)

if __name__ == '__main__':
    # Host must be 0.0.0.0 for Docker to expose it
    app.run(debug=True, host='0.0.0.0', port=5000)