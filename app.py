from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def home():
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story', methods=['POST'])
def generate_story():
    answers = {prompt: request.form[prompt] for prompt in story.prompts}
    generated_story = story.generate(answers)
    return render_template('story.html', story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
