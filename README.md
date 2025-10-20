
🌟 AI Powered Career Path Adviser

🚀 Discover your perfect career path with AI

This web app uses Google Gemini AI to generate personalized career guidance, step-by-step roadmaps, and curated learning resources (Books, YouTube, Websites, Apps) — all based on your interests, skills, and goals.


---

🧠 Project Overview

The AI Powered Career Path Finder helps students and professionals explore their ideal career direction.
It collects key details like your favourite subjects, coding experience, communication skills, and known skills, then the AI suggests:

🎯 Best Career Paths for your profile

🪜 Step-by-step roadmap to reach your career goal

📚 Recommended resources (Books, YouTube videos, Websites, Apps)

💾 Save your career history and download plans as PDF


This app combines Flask (Python backend) + Gemini AI + modern HTML/CSS/JS frontend.


---

🖥️ Tech Stack

Layer	Technology

💻 Frontend	HTML5, CSS3, JavaScript
🧩 Backend	Flask (Python)
🤖 AI Model	Google Gemini 2.5 Flash
🎥 YouTube API	For fetching top learning videos
📄 PDF Export	jsPDF + html2canvas
💾 Storage	LocalStorage (for saving search history)



---

✨ Key Features

✅ AI Career Recommendations – Finds top 5 career paths based on your interests and skills.
✅ Custom Career Roadmap – When you mention a specific goal (like AI Engineer), it gives a detailed roadmap with timeline, projects, and salary scope.
✅ Resource Finder – Fetches best Books, YouTube tutorials, Websites, and Mobile Apps for your goal.
✅ Search History – Saves your previous career searches locally.
✅ PDF Download – Export your AI-generated career plan as a high-quality PDF.
✅ Modern UI – Gradient background, responsive glassmorphism design, and mobile-friendly layout.


---

🧩 Folder Structure

📁 AI-Career-Path-Finder
│
├── 📄 index.html        # Frontend HTML (UI + JS)
├── 🐍 app.py            # Flask backend
├── 📁 static/           # (Optional) Add CSS or assets here
│
└── README.md            # Project documentation


---

⚙️ Setup & Installation

Follow these steps to run the project locally 👇

1️⃣ Clone the Repository

git clone https://github.com/24KQ1A05H7-LOKESH/AI-Career-Path-Adviser.git
cd AI-Career-Path-Finder

2️⃣ Install Dependencies

Make sure Python (≥3.10) is installed. Then run:

pip install flask google-generativeai requests

3️⃣ Add Your API Keys

Open app.py and replace these with your own keys:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

4️⃣ Run the Flask Server

python app.py

5️⃣ Open in Browser

Go to 👉 http://127.0.0.1:5000


---

🧭 How It Works

1. User Inputs:

Favourite subjects

Coding experience

Communication skills

Known skills

Career goal (optional)



2. AI Process:

Sends the details to the Flask backend

Gemini model generates personalized suggestions or roadmaps



3. Outputs:

AI career plan

Clickable learning resources

PDF download option

History saved in browser





---

🔍 API Endpoints

Endpoint	Method	Description

/	GET	Serves the frontend (index.html)
/get_career_paths	POST	Generates AI-based career suggestions or roadmap
/get_resources	POST	Fetches learning resources (Books, YouTube, Websites, Apps)



---

🧠 Example Prompts to Try

Input	Expected Result

Subjects: Computer Science <br> Coding: Beginner	Top 5 career suggestions like Web Developer, Data Analyst, etc.
Goal: Become a Data Scientist	Step-by-step roadmap with skill plan, projects, and salary info
Goal: Android Developer	YouTube + Book resources for Android app development



---

🪄 PDF Feature

You can click “📄 Download PDF” to save your AI-generated career plan as a polished PDF — perfect for sharing or printing.


---

💡 Future Improvements

🔐 Add user login system (for cloud history saving)

🧩 Integrate Gemini Pro model for richer advice

🗂️ Add AI resume generator feature

🌐 Deploy on Render / Vercel / Hugging Face Spaces



---

🧑‍💻 Author

👋 Lokesh
📍 First-year CSE Student @ PACE College, Ongole
🚀 Passionate about AI, Web Development, and Innovation

> “From Zero to Hero in AI Career Guidance!”




---

📜 License

This project is open-source under the MIT License.
Feel free to fork, modify, and improve it!

