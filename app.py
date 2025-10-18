# ===================== app.py (Flask Backend) =====================
from flask import Flask, request, jsonify, send_file
import google.generativeai as genai
import requests

app = Flask(__name__)

# 🔑 API Keys
GEMINI_API_KEY=genai.configure(api_key="AIzaSyAfSKFkki7qfSbvCUTyb_8b1e0pCpGl5b8")
YOUTUBE_API_KEY = "AIzaSyCToJ5AeKMvmyT8ScMPE4d6xFLEcpylbs4"

@app.route('/')
def home():
    return send_file("index.html")


# --- Main AI Career Path Finder ---
@app.route('/get_career_paths', methods=['POST'])
def get_career_paths():
    data = request.get_json()
    subjects = data.get('subjects', '')
    coding = data.get('coding', '')
    communication = data.get('communication', '')
    skills = data.get('skills', [])
    goal = data.get('goal', '').strip()

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        if goal == "":
            # --- User didn’t give a career goal ---
            prompt = f"""
You are a professional AI career advisor.

User Information:
- Favorite Subjects: {subjects}
- Coding Experience: {coding}
- Communication Skills: {communication}
- Skills: {skills}

Suggest the 5 most suitable career paths for this user.
For each career, include:
1️⃣ Career Name
2️⃣ Short reason (why it fits the user)
3️⃣ Future growth or salary potential in India

Format output as clean HTML cards:
Each card must look like this:
<div style='background: #000; color: white; padding:15px; margin:10px; border-radius:15px; border:1px solid cyan; box-shadow:0 0 10px cyan;'>
  <h2 style='color:#00ffff;'>💼 Career Name</h2>
  <p>Reason text here</p>
  <p>📈 Growth Info here</p>
</div>

At the end say:
👉 Choose one career you like to get your full roadmap next!
"""
            response = model.generate_content(prompt)
            formatted = response.text
            html_output = f"""
            <div style='background:black; padding:20px; border-radius:10px; color:white;'>{formatted}</div>
            """
        else:
            # --- User gave a career goal ---
            prompt = f"""
You are a professional career planner.

User's Goal: {goal}
User Details:
- Subjects: {subjects}
- Coding: {coding}
- Communication: {communication}
- Skills: {skills}

Create a detailed roadmap with:
1. Step-by-step career plan (with timelines)
2. Skills to learn
3. Recommended projects/internships
4. Job preparation strategy
5. Future growth & salary expectations (in INR)
6. Attractive formatting with <br> and <div> tags.
"""
            response = model.generate_content(prompt)
            formatted = response.candidates[0].content.parts[0].text if response.candidates else "No response from Gemini."

            html_output = f"""
            <div style='background:white; color:black; border-radius:15px; padding:25px;'>{formatted}</div>
            """

        return jsonify({"response": html_output})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})


# --- Fetch YouTube Videos ---
def fetch_youtube_videos(query, max_results=5):
    search_query = f"{query} tutorial OR course OR for beginners"
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": search_query,
        "key": YOUTUBE_API_KEY,
        "maxResults": max_results,
        "type": "video",
        "safeSearch": "strict"
    }
    response = requests.get(url, params=params).json()
    videos = []
    for idx, item in enumerate(response.get("items", []), start=1):
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        link = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        thumbnail = item["snippet"]["thumbnails"]["medium"]["url"]
        videos.append(f"""
        <div style='margin:10px; background:white; color:black; padding:10px; border-radius:10px;'>
        <img src='{thumbnail}' width='450' style='border-radius:8px;'><br>
        <b style='color:#007bff;'>{idx}. {title}</b><br>
        🎓 {channel}<br>
        <a href='{link}' target='_blank' style='color:#ff6600;'>Watch</a>
        </div>
        """)
    return "<br>".join(videos) if videos else "No videos found."


# --- Get Learning Resources ---
@app.route('/get_resources', methods=['POST'])
def get_resources():
    data = request.get_json()
    category = data.get('category', '')
    goal = data.get('goal', '')

    try:
        if category == "YouTube Videos":
            result_html = fetch_youtube_videos(goal)
        else:
            prompt = f"""
Suggest top 4 {category} related to "{goal}".
Include free and best options.
Format with:
<b>Title</b> — short description<br>
<a href='URL' target='_blank'>Access Here</a>
"""
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            response = model.generate_content(prompt)
            result_html = response.text.replace("\n", "<br>")

        return jsonify({"response": f"<div style='padding:20px;'>{result_html}</div>"} )
    except Exception as e:
        return jsonify({"response": f"Error fetching resources: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)


