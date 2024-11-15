from flask import Flask, render_template, request
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os
import uuid

# Set a custom cache directory
os.environ["HF_HOME"] = os.path.expanduser("~/huggingface_cache")

# Load models at the start
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
paraphraser = pipeline("text2text-generation", model="t5-small", tokenizer="t5-small")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Initialize Flask app
app = Flask(__name__)

# Ensure static folder exists for saving uploaded images
os.makedirs("static", exist_ok=True)

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

# Image Captioning route
@app.route('/generate-caption', methods=['POST'])
def generate_caption():
    image = request.files['image']

    # Validate file type
    if image.mimetype not in ['image/jpeg', 'image/png']:
        return "Invalid file type. Please upload a valid image."

    # Generate a unique filename and save image to static folder
    unique_filename = f"{uuid.uuid4().hex}_{os.path.basename(image.filename)}"
    image_path = os.path.join("static", unique_filename)
    image.save(image_path)

    try:
        # Process the image and generate a caption
        img = Image.open(image)
        inputs = processor(images=img, return_tensors="pt")
        output = model.generate(**inputs, max_new_tokens=50)  # Use max_new_tokens to control output length
        caption = processor.decode(output[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error generating caption: {str(e)}"

    return render_template('result.html', caption=caption, image_url=f"/static/{unique_filename}")

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
