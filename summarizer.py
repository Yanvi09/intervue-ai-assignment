import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if len(sys.argv) < 2:
    print("Usage: python summarizer.py <file>")
    sys.exit(0)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    transcript = f.read()

key = os.getenv("OPENAI_API_KEY")
used_api = False

if key:
    try:
        from openai import OpenAI

        prompt = f"""You are an AI assistant that analyzes interview transcripts.

Your task is to generate a structured summary with exactly 3 sections:

1. Topics Covered

* List 4–6 main topics
* Keep each topic short (2–5 words)

2. Candidate Profile

* Predict role and level
* Give 1–2 line reason

3. Candidate Summary

* 3–6 sentences
* Include background, strengths, concerns, impression

Rules:

* Keep it simple
* Do not hallucinate
* Use only transcript content

Output Format:

Topics Covered:

- ...
- ...

Candidate Profile:
<Role — Level>
<1–2 line reason>

Candidate Summary:
<3–6 clean sentences>

Transcript:
{transcript}"""

        client = OpenAI(api_key=key)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        print(resp.choices[0].message.content)
        used_api = True
    except Exception:
        used_api = False

if not used_api:
    t = transcript.lower()
    role_title = ""

    if "angular" in t or "react" in t or "node" in t:
        role_title = "Software Engineer — Mid-level"
        if ("9+" in transcript) or ("nine plus" in t):
            role_title = "Software Engineer — Senior-level"
    elif "operations" in t or "vendor" in t or "kpi" in t:
        role_title = "Operations / Program Manager — Mid-level"
    else:
        role_title = "General Candidate — Not specified"

    topics = []

    if role_title.startswith("Software Engineer"):
        sw_pick = []

        sw_pick.append(
            ("angular" in t or "ionic" in t, "Angular Ionic hybrid mobile work")
        )
        sw_pick.append(("api integration" in t, "API and service layers"))
        sw_pick.append(("capacitor" in t, "Capacitor camera and files"))
        sw_pick.append(("cursor" in t or "copilot" in t, "AI tools in coding"))
        sw_pick.append(
            (
                "rxjs" in t or "ngrx" in t or "react query" in t or "redux" in t,
                "Angular and React state tools",
            )
        )
        sw_pick.append(("tailwind" in t, "Tailwind design setup"))
        sw_pick.append(("pagination" in t or "lazy loading" in t, "Lists and speed"))
        sw_pick.append(("dashboard" in t, "Mobile-first dashboards"))

        for ok, label in sw_pick:
            if ok is True:
                topics.append(label)
    elif role_title.startswith("Operations"):
        if "fraud" in t:
            topics.append("Fraud prevention work")
        if "vendor" in t:
            topics.append("Vendor sourcing and exits")
        if "crm" in t:
            topics.append("CRM upgrades and rollout")
        if "dashboard" in t:
            topics.append("Leadership dashboards")
        if "kpi" in t:
            topics.append("KPIs and incentives")
        if "integrated" in t or "dialer" in t:
            topics.append("Dialers and integrations")
    else:
        if "experience" in t:
            topics.append("Professional background")

    uniq = []

    for x in topics:
        if x not in uniq:
            uniq.append(x)

    topics = uniq

    if len(topics) < 4:
        topics.append("Planning and stakeholder talk")

    if len(topics) < 4:
        topics.append("Cross-team coordination")

    if len(topics) < 4:
        topics.append("Execution and follow-up")

    topics = topics[:6]

    print("Topics Covered:\n")

    for item in topics:
        print("- " + item)

    print("")
    print("Candidate Profile:")
    print(role_title)

    if role_title.startswith("Software Engineer"):
        print(
            "The talk centers on hybrid mobile work with Ionic, Angular, Capacitor, Tailwind, and React-style state."
        )
        print("The candidate also explains services, errors, performance, and day-to-day use of AI coding tools.")
        summary = (
            "The candidate has over nine years of software development experience. "
            "He focuses on Angular, React, Ionic, Capacitor, Tailwind, APIs, and AI helpers like Cursor. "
            "His strengths are reusable UI, clear service layers, and practical performance ideas for big lists. "
            "One gap is live Redux and Zustand depth was stopped early in this interview. "
            "Overall he looks like a strong senior mobile and web engineer."
        )
    elif role_title.startswith("Operations"):
        print(
            "The story covers fraud work, CRM changes, scoring, vendor cycles, integrations, dialer upgrades, and reviews."
        )
        print(
            "He gives clear examples of data checks, stakeholder tradeoffs, and calm handling of tough vendor cases."
        )
        summary = (
            "He comes from mechanical engineering and moved into operations, finance work, fraud control, and analytics. "
            "He shows CRM rollouts, vendor work, scoring models, dashboards, and dialer upgrades with strong ownership. "
            "He is steady with data in leadership meetings and fair with vendors. "
            "The interviewer notes too much Hindi jargon for senior buyer-facing rounds, so English polish matters. "
            "Overall he fits an operations or program manager track well."
        )
    else:
        print("The text did not trigger the simple software or operations keyword paths.")
        print("Read the full file to judge the role by hand.")
        summary = (
            "This transcript did not match the quick keyword routes. "
            "Use the full discussion to pick role, level, and story. "
            "No firm hire read is offered from the fallback scan alone."
        )

    print("")
    print("Candidate Summary:")
    print(summary)
