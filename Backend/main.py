from flask import Flask, render_template, request, jsonify
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from langchain.agents import load_tools
import os
# import os
os.environ['OPENAI_API_KEY'] = ""
os.environ['SERPAPI_API_KEY'] = ""
app = Flask(__name__, template_folder='templates')

llm = OpenAI(model_name="gpt-3.5-turbo-0125", temperature=0, acomplete)

tool_names = ["serpapi"]
tools = load_tools(tool_names)


agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

@app.route('/')
def index():
    return render_template('index.html', chats=[])

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    # Simulating bot response, you can replace this with actual logic
    message = agent.run(message)
    bot_response = ": " + message
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
