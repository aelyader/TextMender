<h1 align="center">TextMender: User Guide and README</h1>
<p align="center">
  <img src="images/textmender_2final.jpg" width="400" height="400">
</p>

# Welcome to **TextMender**

TextMender is a completely ***_FREE_***, locally-run web application for text summarization and paraphrasing. Leveraging state-of-the-art language models from Hugging Face’s Transformers library, TextMender is ideal for condensing large pieces of text into concise summaries or generating rephrased content while maintaining the original meaning. Since TextMender runs entirely on your **local machine**, no data is sent to external servers, ensuring privacy and control over your content.

---

## **Setting Up Your Environment**

**YouTube Tutorial**
[![TextMender Tutorial](https://raw.githubusercontent.com/your-username/TextMender/main/images/youtube_thumbnail.png)](https://youtu.be/your_video_link "Click to watch the video")

### **Prerequisites**

- **Python**: 3.7 or higher
- **Memory**: Minimum of 8GB of RAM for optimal performance
- **Browser**: Chrome, Firefox, or any modern browser

### **Installation**

1. **Clone the Repository**: Clone the TextMender GitHub repository to your local machine:
    
    ```bash
    git clone https://github.com/your-username/TextMender.git
    ```
    
    Navigate to the cloned directory:
    
    ```bash
    cd TextMender
    ```

2. **Set Up Virtual Environment**:
    
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Required Packages**:
    
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Models**:  
   The necessary NLP models (BART for summarization and T5 for paraphrasing) are downloaded automatically on the first run.

---

## **Running TextMender**

1. **Start the Flask Server**:
    
    ```bash
    python app.py
    ```

2. **Access the Application**:  
   Open your browser and go to `http://127.0.0.1:5000` to access TextMender.

---

## **Using TextMender**

1. **Summarize Text**:
   - Input your text in the **Summarize Text** section.
   - Click **Summarize** to generate a concise version of the input text.

2. **Paraphrase Text**:
   - Input your text in the **Paraphrase Text** section.
   - Click **Paraphrase** to generate a rephrased version of the text.

3. **Output Display**:
   - The output is displayed directly below each section, with preserved formatting for readability.

---

## **Technical Details**

- **Backend**: Flask framework for web server functionality.
- **Frontend**: HTML and CSS for user interface.
- **Models**:
  - **Summarization**: Uses `facebook/bart-large-cnn` for generating summaries.
  - **Paraphrasing**: Uses `t5-base` for generating paraphrased text.
- **Dynamic Length Handling**:
  - Summarization and paraphrasing functions dynamically adjust output length based on input length for coherence and readability.
- **Key Libraries**:
  - **Transformers**: For loading and utilizing pre-trained NLP models.
  - **Flask**: For serving the web application.

---

## **Troubleshooting**

- **Model Load Issues**: Ensure a stable internet connection for initial model downloads.
- **Performance**: For slower machines, closing other applications may improve performance.
- **Display**: If output is misaligned, check that `white-space: pre-wrap;` is applied to the output text in the HTML.

---

## **TextMender Output Files**

TextMender does not generate downloadable output files but displays the summarization and paraphrasing results directly within the web interface. However, you can copy results for further use.

### **1. Summary Output**
   - Displays the concise summary based on the input text.

### **2. Paraphrased Text Output**
   - Shows the rephrased version of the input text with preserved meaning.

---

## **Additional Notes**

- **Preserving Line Breaks**: TextMender’s output displays line breaks and formatting, making it easy to read.
- **Running in Production**: Use a production-grade WSGI server like Gunicorn when deploying TextMender for production use, as Flask’s development server is not intended for public use.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/your-username/TextMender/main/images/TextMender_screenshot.png" width="700" height="400">
</p>

For issues or further assistance, please refer to the GitHub issues page or contact the development team.

## **Contributors**

- **Your Name** - Initial development and project management
- **OpenAI ChatGPT** - Assisted with development suggestions and optimization

---

This guide is designed to facilitate an easy and effective user experience with TextMender, providing accurate summarization and paraphrasing for various textual needs.

