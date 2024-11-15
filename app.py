from transformers import pipeline
from flask import Flask, render_template, request

# Load models at the start
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# Explicitly set model and tokenizer for paraphraser
paraphraser = pipeline("text2text-generation", model="t5-small", tokenizer="t5-small")

# Initialize Flask app
app = Flask(__name__)


# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Summarize route
@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']  # Get the text from the form
    summary = summarize_text(text)  # Generate summary
    return render_template('index.html', summary=summary)  # Render template with summary


# Paraphrase route
@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    text = request.form['text']  # Get the text from the form
    paraphrased = paraphrase_text(text)  # Generate paraphrased text
    return render_template('index.html', paraphrased=paraphrased)  # Render template with paraphrased text


# Summarize text function with dynamic length handling
def summarize_text(text):
    input_length = len(text.split())
    max_len = min(50, max(10, input_length // 2))
    min_len = max(5, input_length // 4)
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']


# Paraphrase text function with dynamic length handling and improved debugging
def paraphrase_text(text):
    input_length = len(text.split())
    max_len = min(60, int(input_length * 1.2))
    paraphrased = paraphraser("paraphrase: " + text, max_length=max_len, num_return_sequences=1)

    # Debugging: Print the raw output to inspect structure
    print("Raw Paraphrased Output:", paraphrased)

    # Check for 'generated_text' key in output and return accordingly
    if paraphrased and isinstance(paraphrased, list) and 'generated_text' in paraphrased[0]:
        return paraphrased[0]['generated_text']
    else:
        return "Paraphrasing failed: Unexpected output format"


# Temporary route for directly returning paraphrased text to check if the output is correct
@app.route('/paraphrase_direct', methods=['POST'])
def paraphrase_direct():
    text = request.form['text']
    paraphrased = paraphrase_text(text)
    return paraphrased  # Return the paraphrased text directly to the browser


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
