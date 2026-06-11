// ════════════════════════════════════════
// BLOGS
// Add new blog posts here.
// Fields: title, date (YYYY-MM-DD), tag, summary, content, readTime, link, cover, pdf, photos
// ════════════════════════════════════════
const BLOGS = [
    {
        title:    "From Zero to Four SaaS Products",
        date:     "2026-06-11",
        tag:      "SaaS",
        summary:  "When I started building my first SaaS product, I didn't really know what I was doing. Now I've built four full-stack platforms — and the journey genuinely transformed how I think about software.",
        content:  `When I started building my first SaaS product, I didn't really know what I was doing. I knew how to write code. I had a solid background in AI and Machine Learning. But "SaaS architecture"? Multi-portal hierarchy? Role-based access? These were just buzzwords I'd read about online.

Now I've built four full-stack platforms: an L&D portal, an AI-powered LMS called Saksham, a data management platform (QBER), and an AI recruitment intelligence platform, and I'm writing this because the journey genuinely transformed how I think about software.

1. My First Shock: SaaS Is About Layers, Not Just Pages

When I built my very first portal, I thought of it simply: one login page, one dashboard. Maybe two if I needed an admin.

That's not SaaS. That's a website with a login screen.

The real insight came when I started thinking in hierarchies. My first platform — the L&D Portal — shipped with a 5-tier role architecture: Super Admin → Admin → Mentor → Coach → Learner. Every single role had its own dedicated, locked dashboard. A Coach couldn't see what a Super Admin sees. A Learner couldn't stumble into Admin territory.

This wasn't complexity for complexity's sake. It was an intentional design. Each role gets exactly the tools they need, nothing more, nothing less. That principle became a design mantra I carried into every product after it.

2. Confidence Comes From Shipping, Not Reading

Before I started, I'd consumed plenty of documentation, tutorials, and YouTube videos about SaaS architecture. But nothing, genuinely nothing, built confidence the way completing a product did.

After the L&D Portal, I understood cascade user management: one admin action can create, assign, and manage an entire sub-hierarchy. After Saksham, I understood multi-tenancy and how to isolate company-level data properly. After QBER, I got comfortable with module-based access control and dynamic user limit enforcement. After the Recruitment Platform, I could architect a 4-tier system from scratch and know exactly where the seams would be.

Four products mean four times you pushed through the part where you weren't sure it would work. That repetition is irreplaceable.

3. My AIML Background Wasn't a Detour — It Was the Superpower

Here's something I didn't expect: coming from an AI/ML background turned out to be an enormous advantage in SaaS development, not a distraction from it.

In Saksham, instead of writing rigid rubrics for quiz scoring, I plugged in Google Gemini 2.5 Flash-Lite to evaluate open-ended learner answers across semantic understanding, concept coverage, and answer depth — things a rule-based system could never handle well. The accuracy jumped. Facilitators loved it.

In the Recruitment Platform, I built a dual-engine CV analysis system: Gemini handles the deep semantic matching against job descriptions, while a parallel rule-based engine runs 18 deterministic checks on formatting, readability, and professionalism. Neither engine alone would've been enough. Together, they eliminated manual CV screening entirely.

Even the embedded AI chatbot I built into every Saksham portal — a feature most platforms charge enterprise pricing for — came naturally because I already understood how to prompt and chain LLM responses.

4. Security Is Infrastructure, Not an Afterthought

Early on, I thought of authentication as just "the login part." Build it once, move on.

By the time I built Saksham, I had JWT-secured APIs, bcrypt-hashed passwords, and OTP-based password recovery via SMTP email. Not because I wanted to gold-plate the project, but because I'd seen, through iteration, how every security hole creates downstream problems across every role in the hierarchy.

When you have 6 user roles and multi-tenant data isolation, a poorly secured API isn't just one vulnerability. It's a skeleton key. That realisation made me treat security as a first-class architectural concern, not a layer painted on at the end.

5. Great UX Comes From Role Empathy, Not Just Good Design

One thing that quietly improved across all four products was how I thought about UX. Not visual design but role empathy: the practice of genuinely inhabiting each user type and asking "what does this person actually need right now?"

A Learner on the L&D portal needs to see their progress, their earned coins, and their next module. They don't need to see support ticket statistics or user management tables. Showing them those things isn't neutral — it's noise that makes the product feel harder.

A Data Entry user on QBER needs a clean, fast data input workflow. A Viewer user needs rich, filterable dashboards with Excel-style sorting and grouping. Same platform. Entirely different experiences. Both optimised.

6. Features You're Proud Of Are Usually the Ones You Invented Under Constraints

Some of the features I'm proudest of across these four platforms came from constraints, not freedom.

AI-generated PDF certificates in Saksham? That came from not wanting to manually create certificates for every learner at scale. The coin-based rewards engine in the L&D Portal? That came from trying to drive engagement without a gamification library. Tiered subscription enforcement in the Recruitment Platform? That came from needing a real monetisation model, not just a demo product.

Constraints forced creative solutions. And those solutions ended up being the differentiating features — the things that made each platform genuinely useful rather than just technically functional.

Four SaaS products in, here's what I know:

I started thinking SaaS was about code. It's actually about structure, role hierarchies, data isolation, permission boundaries, and user flows designed around real workflows. Code is just how you express that structure.

I started thinking my AIML background was separate from "real" software engineering. It turned out to be the thing that made my products genuinely smarter than what a pure web developer would build.

And I started thinking confidence was something you needed before you built. It's actually something you earn by building — product by product, mistake by mistake, one developed feature at a time.

If you're standing where I was at the beginning — with a skill set, a vague idea, and a lot of uncertainty — my advice is simple: build the thing. The knowledge will come. The confidence will follow.`,
        readTime: 7,
        link:     "",
        cover:    "",
        pdf:      "/static/blogs/from_zero_to_4_SAAS_platforms.pdf"
    },
];


// ════════════════════════════════════════
// CONFERENCES
// Add new conference entries here.
// Fields: name, date (YYYY-MM-DD), dateEnd, location, role, topic, learnings, cert, photos, linkedinUrl, linkedinUrl2
// ════════════════════════════════════════
const CONFERENCES = [
    {
        name:     "Prompt Engineering Session",
        date:     "2025-09-15",
        location: "India",
        role:     "Speaker",
        topic:    "Prompt Engineering · AI",
        learnings: `Got the chance to deliver a short session on Prompt Engineering and honestly it was a great experience.

I kept it practical — no theory slides, just real examples of the same prompt giving wildly different results depending on how it's written.

What I covered:

→ Why "just ask ChatGPT" isn't prompt engineering
→ Zero-shot vs few-shot vs chain-of-thought — when to use each
→ How role prompting changes model behaviour completely
→ System prompts and why they matter more than the user prompt
→ Common mistakes: vague instructions, no output format, not iterating

The moment I showed a bad prompt vs a well-structured one producing completely different outputs — that's when it clicked for everyone.

If you're building anything with LLMs, spending 2 hours on prompt engineering properly will save you days of debugging.`,
        cert:     "",
        photos:   [
            "/static/images/prompt_session_1.jpg",
            "/static/images/prompt_session_2.jpg"
        ],
        linkedinUrl: "https://www.linkedin.com/posts/vedant-kasbekar_promptengineering-artificialintelligence-activity-7389137658607788032-lTFE"
    },
    {
        name:     "API Conference — APIs & AI",
        date:     "2025-06-01",
        location: "India",
        role:     "Attendee",
        topic:    "APIs · AI",
        learnings: `Walked in thinking I knew APIs well enough. Walked out with a notepad full of things to rethink.

The day was about how API design is being rebuilt for AI workloads — not just adding an LLM endpoint, but rethinking contracts, versioning, and how data moves at scale.

What stuck:

→ Streaming is non-negotiable. No streaming support = already behind.
→ Versioning breaks differently when AI apps are downstream — one schema change and the whole chain fails silently.
→ Rate limiting for LLMs isn't request counts. It's tokens, context windows, and 30-second timeouts.
→ Pure REST isn't built for async inference. Webhooks and SSE are taking over.

Deals with all of this daily at Eelanos. Glad I went.`,
        cert:     "",
        photos:   [
            "/static/images/conf_api_1.jpg",
            "/static/images/conf_api_2.jpg",
            "/static/images/conf_api_3.jpg",
            "/static/images/conf_api_4.jpg"
        ],
        linkedinUrl: "https://www.linkedin.com/posts/vedant-kasbekar_apiconference-apis-ai-activity-7376110595101777920-7pEA"
    },
    {
        name:     "DevConf.IN 2026 — Speaker",
        date:     "2026-02-13",
        dateEnd:  "2026-02-14",
        location: "MIT World Peace University, Pune",
        role:     "Speaker",
        topic:    "Prompt Engineering 2.0",
        learnings: `DevConf.IN is Red Hat's annual open source conference in India. The audience knows their stuff — contributors, engineers, actual builders. So I had to bring depth.

My session was Prompt Engineering 2.0 — moving past basic prompting into agent design, structured outputs, and building LLM pipelines that actually hold up in production.

What I covered:

→ Why prompt engineering still matters even with reasoning models
→ Where chain-of-thought breaks and how to catch it
→ Structured output prompting for real SaaS applications
→ Multi-step agent prompts that don't hallucinate mid-chain
→ Live examples from products I've built at Eelanos

The Q&A ran long — always a good sign. Got some sharp pushback on agent reliability which turned into a great conversation after the session ended.

Speaking in front of 200+ developers at a Red Hat conference was genuinely one of the better experiences I've had.`,
        cert:     "",
        photos:   [
            "/static/images/devconf1.jpg",
            "/static/images/devconf2.jpg",
            "/static/images/devconf3.jpg",
            "/static/images/devconf4.jpg",
            "/static/images/devconf5.jpg"
        ],
        linkedinUrl: "https://www.linkedin.com/posts/vedant-kasbekar_devconfin-opensource-techcommunity-activity-7428683592769363968-baBQ"
    },
    {
        name:     "PyConf Hyderabad 2025",
        date:     "2025-02-15",
        dateEnd:  "2025-02-16",
        location: "Hyderabad, India",
        role:     "Attendee",
        topic:    "Python · AI · ML",
        learnings: `Two days. Lots of Python. Even more AI. PyConf Hyderabad is run by the HydPy community and it shows — good speakers, well organised, and the kind of crowd that has actual opinions.

Day 1 was talks — GenAI pipelines, LLM tooling, deep learning. The AI track was packed. People are building things, not just talking about them.

Day 2 was more hands-on — workshops, smaller rooms, hallway conversations that were honestly as valuable as any scheduled session.

What I took away:

→ The Python + LLM ecosystem is maturing fast. LangChain, LlamaIndex, local models — all seeing real production use.
→ LLM evaluation and testing is still the unsolved problem. Nobody has a clean answer.
→ Open source is moving faster than enterprise tooling. By a lot.
→ Met some genuinely interesting builders. That alone made the trip worth it.

Would go again.`,
        cert:     "",
        photos:   [
            "/static/images/pyconf1.jpg",
            "/static/images/pyconf2.jpg",
            "/static/images/pyconf3.jpg",
            "/static/images/pyconf4.jpg",
            "/static/images/pyconf5.jpg",
            "/static/images/pyconf6.jpg",
            "/static/images/pyconf7.jpg",
            "/static/images/pyconf8.jpg",
            "/static/images/pyconf9.jpg",
            "/static/images/pyconf10.jpg"
        ],
        linkedinUrl:  "https://www.linkedin.com/posts/vedant-kasbekar_pyconfhyderabad-pyconindia-ai-activity-7440972953825132545-KwaI",
        linkedinUrl2: "https://www.linkedin.com/posts/vedant-kasbekar_pyconfhyderabad-ai-machinelearning-activity-7442419821587226624-SiRX"
    },
];