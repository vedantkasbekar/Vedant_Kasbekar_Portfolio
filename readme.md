# 🤖 Vedant Kasbekar — AI Developer Portfolio

> **Live Site →** [vedant-kasbekar-portfolio.onrender.com](https://vedant-kasbekar-portfolio.onrender.com/)

A full-stack personal portfolio built with **Flask + Jinja2**, featuring an animated dark-mode UI, a dedicated blogs & conferences page, an AI-powered skills neural network, and a working contact form — all hosted on Render.

---

## ✨ Features

- **Animated Hero** — particle background, glitch name effect, scrollreveal entrance animations
- **Work Experience Timeline** — collapsible accordion with 7 production projects at Eelanos
- **Projects Section** — bullet-point cards with animated neon glow borders and staggered entrance
- **AI Skills Neural Network** — interactive SVG graph visualising tech stack relationships
- **Blogs & Conferences Page** — searchable/filterable blog reader + photo gallery for conferences
- **Contact Form** — sends emails via SMTP (Gmail) directly to inbox
- **Dark / Light Mode** — persistent theme toggle
- **Fully Mobile-Responsive** — hamburger drawer nav, single-column layouts, touch-friendly UI
- **Hosted on Render** — auto-deploys from GitHub on every push

---

## 🗂️ Project Structure

```
portfolio/
│
├── app.py                  # Flask app — routes, portfolio data, SMTP email
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
│
├── templates/
│   ├── index.html          # Main portfolio page
│   └── blogs.html          # Blogs & conferences page
│
└── static/
    ├── style.css           # Main stylesheet (dark/light mode, animations)
    ├── blogs.css           # Blogs page stylesheet
    ├── blogs_data.js       # Blog posts & conference data (edit to add new content)
    ├── particles.json      # Particle animation config
    └── images/             # Profile photo, conference photos, blog covers
```

---

## 🚀 Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/vedantkasbekar/portfolio.git
cd portfolio
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
SMTP_EMAIL=your_gmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_TO=your_inbox@gmail.com
```

> **Note:** Use a [Gmail App Password](https://support.google.com/accounts/answer/185833), not your regular Gmail password.

### 5. Run the app

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## ⚙️ Environment Variables

| Variable        | Description                              | Default                        |
|-----------------|------------------------------------------|--------------------------------|
| `SMTP_EMAIL`    | Gmail address used to send contact emails | `vedantkasbekar15@gmail.com`  |
| `SMTP_PASSWORD` | Gmail App Password                        | *(required)*                  |
| `SMTP_TO`       | Inbox where contact form emails arrive    | `vedantkasbekar15@gmail.com`  |

---

## 📦 Dependencies

```txt
Flask
python-dotenv
```

All frontend libraries are loaded via CDN — no npm or build step needed:

| Library | Purpose |
|---|---|
| [particles.js](https://vincentgarreau.com/particles.js/) | Animated particle background |
| [ScrollReveal](https://scrollrevealjs.org/) | Scroll entrance animations |
| [Font Awesome 6](https://fontawesome.com/) | Icons |
| [Google Fonts](https://fonts.google.com/) — Orbitron, Rajdhani, Fira Code | Typography |

---

## 🌐 Deploying to Render

This portfolio is live at **[vedant-kasbekar-portfolio.onrender.com](https://vedant-kasbekar-portfolio.onrender.com/)**.

To deploy your own fork:

1. Push the repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service** → connect your repo
3. Set the following in Render's **Environment** settings:
   ```
   SMTP_EMAIL      = your_gmail@gmail.com
   SMTP_PASSWORD   = your_app_password
   SMTP_TO         = your_inbox@gmail.com
   ```
4. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
5. Add `gunicorn` to `requirements.txt` if not already there
6. Deploy — Render auto-rebuilds on every push to `main`

---

## ✏️ Adding Content

### Add a new blog post
Open `static/blogs_data.js` and add an object to the `BLOGS` array:

```js
{
    title:    "Your Post Title",
    date:     "2026-06-13",         // YYYY-MM-DD
    tag:      "AI",                  // tag shown on card
    summary:  "One-line preview...",
    content:  `Full blog content here...`,
    readTime: 5,                     // minutes
    pdf:      "/static/blogs/your_post.pdf"  // optional
}
```

### Add a new conference
Add an object to the `CONFERENCES` array in `static/blogs_data.js`:

```js
{
    name:      "Conference Name",
    date:      "2026-05-10",
    location:  "City, Country",
    role:      "Speaker",           // or "Attendee"
    topic:     "AI · LLMs",
    learnings: `What you learned...`,
    photos:    ["/static/images/conf1.jpg"],
    linkedinUrl: "https://linkedin.com/posts/..."
}
```

### Update portfolio data
All personal info, skills, experience, projects, and education live in the `portfolio_data` dict in `app.py` — edit directly.

---

## 📸 Screenshots

| Section | Preview |
|---|---|
| Hero | Animated particle background with glitch name effect |
| Experience | Collapsible accordion with 7 production SaaS projects |
| Projects | Neon glow card grid with bullet-point feature lists |
| Skills | Interactive AI neural network SVG |
| Blogs | Searchable blog reader + conference photo galleries |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Built by **Vedant Kasbekar** · [LinkedIn](https://linkedin.com/in/vedant-kasbekar) · [GitHub](https://github.com/vedantkasbekar)

</div>