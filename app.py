from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# ── Email config ──
SMTP_EMAIL    = os.environ.get("SMTP_EMAIL", "vedantkasbekar15@gmail.com")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_TO       = os.environ.get("SMTP_TO", "vedantkasbekar15@gmail.com")

portfolio_data = {
    "name": "Vedant Kasbekar",
    "tagline": "AI Developer & Machine Learning Engineer",
    "email": "vedantkasbekar@gmail.com",
    "phone": "7559115119",
    "location": "Chhatrapati Sambhajinagar, India",
    "linkedin": "https://linkedin.com/in/vedant-kasbekar",
    "github": "https://github.com/vedantkasbekar",
    "profile_summary": "AI Developer with 1 year of experience building LLM-powered SaaS products, NLP pipelines, and RAG systems. Skilled in Python, LangChain, and OpenAI APIs. Passionate about applying GenAI to real-world business problems.",
    "skills": {
        "Languages": ["Python", "SQL"],
        "LLMs & GenAI": ["LangChain", "LLM APIs", "Hugging Face", "Ollama", "RAG", "Gemini Embeddings", "Prompt Engineering", "Agentic AI"],
        "AI/ML": ["Machine Learning", "NLP", "spaCy", "TensorFlow", "Computer Vision"],
        "Backend & Tools": ["Flask", "FastAPI", "Streamlit", "PyPDF2", "gTTS", "deep_translator"],
        "Databases": ["MySQL", "ChromaDB", "FAISS", "PostgreSQL", "SQLite"],
        "Data & Analytics": ["Power BI", "Pandas", "NumPy", "Plotly", "Matplotlib"]
    },
    # --- Work Experience (separate from achievements) ---
    "experience": [
        {
            "role": "AI Developer",
            "company": "Eelanos",
            "duration": "Aug 2025 – Present",
            "highlights": [
                { "icon": "🤖", "text": "7 AI-powered SaaS products shipped in production" },
                { "icon": "⚡", "text": "Eliminated manual CV shortlisting entirely with Gemini AI screening" },
                { "icon": "🔒", "text": "Built fully offline medical AI using local LLMs — zero cloud dependency" },
                { "icon": "📊", "text": "GPT-4o BI dashboard lets teams query live data in plain English" }
            ],
            "projects": [
                {
                    "month": "Aug 2025",
                    "title": "Financial Data Extraction System",
                    "desc": "Scrapes and aggregates financial statements (P&L, Balance Sheet, Cash Flow) from financial sites for multiple companies. Displays data in an interactive dashboard with multi-company comparison and export options.",
                    "type": "Data Engineering",
                    "tech": ["Python", "Streamlit", "BeautifulSoup", "Pandas", "OpenPyXL"]
                },
                {
                    "month": "Sep 2025",
                    "title": "AI Recruitment SaaS Platform",
                    "desc": "AI-powered, multi-portal recruitment SaaS platform where AI automatically screens and scores uploaded CVs against job descriptions using Gemini 2.5 Flash, eliminating manual shortlisting entirely.",
                    "type": "GenAI · SaaS",
                    "tech": ["Flask", "SQLite", "SQLAlchemy", "Google Gemini 2.5 Flash", "pdfplumber", "python-docx", "Jinja2", "HTML/CSS/JS"]
                },
                {
                    "month": "Oct 2025",
                    "title": "AI-Powered LMS (Learning Management System)",
                    "desc": "AI-powered, multi-portal SaaS LMS that scores open-ended answers in real time using Google Gemini AI/NLP, issues PDF certificates, and ships with OTP login recovery and an embedded AI chatbot — all in one platform.",
                    "type": "GenAI · SaaS",
                    "tech": ["Flask", "SQLite", "Python", "HTML/CSS/JS", "Google Gemini 2.5 Flash-Lite", "JWT", "bcrypt", "ReportLab", "SMTP"]
                },
                {
                    "month": "Nov 2025",
                    "title": "Data Management SaaS Platform",
                    "desc": "AI-powered, multi-portal data management SaaS platform with role-based access control and data visualisations for intuitive business data understanding across departments.",
                    "type": "SaaS · BI",
                    "tech": ["Flask", "Python", "Jinja2", "SQLAlchemy", "HTML/CSS", "JavaScript", "SQLite", "PostgreSQL"]
                },
                {
                    "month": "Dec 2025",
                    "title": "Learning & Development Portal",
                    "desc": "Flask + SQLite powered multi-portal SaaS platform with a 5-tier role hierarchy (Super Admin → Admin → Mentor → Coach → Learner), featuring self-paced programs, progress tracking, a coin rewards system, support tickets, and real-time notifications.",
                    "type": "SaaS · EdTech",
                    "tech": ["Python", "Flask", "SQLAlchemy", "HTML/CSS", "Jinja2", "JavaScript"]
                },
                {
                    "month": "Jan 2026",
                    "title": "Local LLM Medical Report Analyser",
                    "desc": "Ollama-powered fully offline tool that reads patient lab report CSVs, flags abnormal values, and generates calm, doctor-toned health summaries — built for the Elanaura app with zero cloud dependency.",
                    "type": "Local AI · Healthcare",
                    "tech": ["Python", "Ollama", "LangChain", "Pandas", "MySQL"]
                },
                {
                    "month": "Feb 2026",
                    "title": "AI Business Intelligence Dashboard",
                    "desc": "Flask & GPT-4o powered BI portal that lets manufacturing teams query live MySQL sales, inventory, and stock-ageing data in plain English — auto-generating SQL, rendering dynamic Chart.js visualisations, and delivering CFO-grade insights through a secure conversational AI dashboard.",
                    "type": "GenAI · BI",
                    "tech": ["Python", "Flask", "OpenAI GPT-4o", "GPT-4o-mini", "MySQL", "Chart.js", "HTML/CSS"]
                }
            ]
        }
    ],
    "projects": [
        {
            "title": "ResearchIQ: AI-Powered Research Assistant",
            "date": "June 2024",
            "bullets": [
                "Scrapes 8+ URLs & parses PDF/DOCX files with instant per-source credibility scoring (domain authority, recency, political bias)",
                "Dual query modes — RAG pipeline (Gemini Embeddings + NumPy cosine similarity) and full-context Gemini — both with multi-turn chat",
                "Auto-suggests related articles per response and tracks session analytics (query frequency, topic trends, source usage)",
                "80+ language translation, text-to-speech audio output, and auto-detecting Plotly visualisations"
            ],
            "tech_stack": ["Python", "Streamlit", "Google Gemini 2.5 Flash", "Gemini Embeddings", "LangChain", "NumPy", "PyPDF2", "SQLite", "Plotly", "gTTS", "deep_translator", "RAG"],
            "github_link": "https://github.com/vedantkasbekar/ResearchIQ",
            "type": "GenAI · RAG"
        },
        {
            "title": "Resumatch: AI-Powered ATS Resume Evaluator",
            "date": "Dec 2024",
            "bullets": [
                "5-module ATS platform: Job Seeker (resume scoring), Recruiter (resume comparison), AI Resume Builder, NLP offline analysis & Company Research",
                "Gemini 2.5 Flash generates match scores, missing keyword analysis, AI candidate summaries & personalised improvement tips",
                "spaCy + pyresparser NLP pipeline for offline skill, education & experience extraction — no API key required",
                "Admin portal with analytics dashboard, average scores, top matched skills & paginated logs"
            ],
            "tech_stack": ["Python", "Flask", "SQLAlchemy", "SQLite", "Gemini API", "spaCy", "NLP", "Chart.js", "JavaScript"],
            "github_link": "https://github.com/vedantkasbekar/resumatch",
            "type": "GenAI"
        },
        {
            "title": "BlinkGuard: Sleep Detection Glasses",
            "date": "June 2022",
            "bullets": [
                "Drowsiness detection wearable using an IR Eye Blink Sensor with Arduino Pro Mini",
                "Monitors real-time eye-closure patterns and triggers buzzer + vibration alerts on prolonged closure",
                "Compact, low-power design — fully self-contained with no external compute required"
            ],
            "tech_stack": ["Arduino", "IR Sensor", "IoT", "C++"],
            "github_link": "#",
            "type": "Hardware AI"
        }
    ],
    # --- Positions of Responsibility (separate from achievements) ---
    "positions": [
        {
            "title": "Design Director",
            "org": "TEDxDIETMS",
            "duration": "Jul 2023 – Sep 2023",
            "description": "Led design and visual branding for the college TEDx event.",
            "icon": "🎨",
            "photos": ["tedx1.jpg", "tedx2.jpg", "tedx3.jpg"]
        },
        {
            "title": "Delegate of Saudi Arabia",
            "org": "Model United Nations – DISEC",
            "duration": "Apr 2024",
            "description": "Represented Saudi Arabia in DISEC, demonstrating research, negotiation, and public speaking skills to address global security issues.",
            "icon": "🌍",
            "photos": ["mun1.jpg", "mun2.jpg", "mun3.jpg"]
        }
    ],
    # --- Achievements / Extracurricular (separate from positions) ---
    "achievements": [
        {
            "title": "Speaker – DevConf 2026",
            "org": "MIT World Peace University",
            "date": "2026",
            "description": "Delivered a technical session on Prompt Engineering 2.0 to 200+ developers and students, covering advanced prompting strategies, chain-of-thought reasoning, and real-world LLM application design.",
            "icon": "🎤",
            "photos": ["devconf1.jpg", "devconf2.jpg", "devconf3.jpg"]
        },
        {
            "title": "Rank 12 – SUNHACK Hackathon",
            "org": "36-Hour Coding Marathon",
            "date": "Apr 2024",
            "description": "Secured 12th rank out of 250+ teams building an AI solution in a 36-hour coding marathon.",
            "icon": "🏆",
            "photos": ["sunhack1.jpg", "sunhack2.jpg", "sunhack3.jpg"]
        }
    ],
    "education": [
        {
            "degree": "B.Tech in CSE (Artificial Intelligence & Machine Learning)",
            "institution": "Deogiri Institute of Engineering and Management Studies, DBATU University",
            "years": "2021 – 2025"
        },
        {
            "degree": "HSE – Science Stream",
            "institution": "Vidyadham Science Jr. College, Chhatrapati Sambhajinagar",
            "years": "2019 – 2021"
        }
    ],
    "certifications": [
        "What Is Generative AI?",
        "Generative AI: The Evolution of Online Search",
        "Streamlining Work with Microsoft Bing Chat",
        "Microsoft 365 Copilot First Look"
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()

        name    = data.get('name', 'Unknown')
        email   = data.get('email', '')
        phone   = data.get('phone', 'Not provided')
        subject = data.get('subject', 'Portfolio Contact')
        message = data.get('message', '')

        # ── Build email ──
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"[Portfolio] {subject} — from {name}"
        msg['From']    = SMTP_EMAIL
        msg['To']      = SMTP_TO
        msg['Reply-To'] = email

        html_body = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #0d1117; color: #e6edf3; padding: 32px; border-radius: 12px; border: 1px solid #30363d;">
            <div style="border-bottom: 2px solid #00f3ff; padding-bottom: 16px; margin-bottom: 24px;">
                <h2 style="color: #00f3ff; margin: 0;">📬 New Portfolio Message</h2>
                <p style="color: #8b949e; margin: 4px 0 0;">From your portfolio contact form</p>
            </div>
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="padding: 10px 0; color: #8b949e; width: 100px; vertical-align: top;">Name</td>
                    <td style="padding: 10px 0; color: #e6edf3; font-weight: bold;">{name}</td>
                </tr>
                <tr>
                    <td style="padding: 10px 0; color: #8b949e; vertical-align: top;">Email</td>
                    <td style="padding: 10px 0;"><a href="mailto:{email}" style="color: #00f3ff;">{email}</a></td>
                </tr>
                <tr>
                    <td style="padding: 10px 0; color: #8b949e; vertical-align: top;">Phone</td>
                    <td style="padding: 10px 0; color: #e6edf3;">{phone}</td>
                </tr>
                <tr>
                    <td style="padding: 10px 0; color: #8b949e; vertical-align: top;">Subject</td>
                    <td style="padding: 10px 0; color: #e6edf3; font-weight: bold;">{subject}</td>
                </tr>
            </table>
            <div style="margin-top: 20px; background: #161b22; border-radius: 8px; padding: 20px; border-left: 3px solid #00f3ff;">
                <p style="color: #8b949e; margin: 0 0 8px; font-size: 0.85rem;">MESSAGE</p>
                <p style="color: #e6edf3; margin: 0; line-height: 1.7;">{message}</p>
            </div>
            <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid #30363d; color: #8b949e; font-size: 0.8rem;">
                Sent from vedantkasbekar.portfolio
            </div>
        </div>
        """

        msg.attach(MIMEText(html_body, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, SMTP_TO, msg.as_string())

        return jsonify({"status": "success", "message": "Email sent successfully"})

    except Exception as e:
        print(f"Email error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)