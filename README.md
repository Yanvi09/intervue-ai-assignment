# Interview transcript summarizer

This script reads one transcript file and prints a three-part summary.

**Sample naming:**  
`sample_transcript_assignment_1.txt` holds the operations and program-manager style transcript.  
`sample_transcript_assignment_2.txt` holds the software engineer transcript.

## How to run

```bash
python summarizer.py sample_transcript_assignment_1.txt
python summarizer.py sample_transcript_assignment_2.txt
```

## API usage

- If `OPENAI_API_KEY` is set, the script calls OpenAI once with `gpt-4o-mini`, then prints the reply.
- If the key is missing or the API call fails, the script prints the built-in fallback summary instead.

### Set API key

**PowerShell**

```powershell
$env:OPENAI_API_KEY="your_key_here"
```

**CMD**

```cmd
set OPENAI_API_KEY=your_key_here
```

## Model used

OpenAI **`gpt-4o-mini`**

## Output examples (fallback mode)

These runs used no API key so the simple keyword path produced the output.

### `sample_transcript_assignment_1.txt` (operations / program candidate)

```
Topics Covered:

- Fraud prevention work
- Vendor sourcing and exits
- CRM upgrades and rollout
- Leadership dashboards
- KPIs and incentives
- Dialers and integrations

Candidate Profile:
Operations / Program Manager — Mid-level
The story covers fraud work, CRM changes, scoring, vendor cycles, integrations, dialer upgrades, and reviews.
He gives clear examples of data checks, stakeholder tradeoffs, and calm handling of tough vendor cases.

Candidate Summary:
He comes from mechanical engineering and moved into operations, finance work, fraud control, and analytics. He shows CRM rollouts, vendor work, scoring models, dashboards, and dialer upgrades with strong ownership. He is steady with data in leadership meetings and fair with vendors. The interviewer notes too much Hindi jargon for senior buyer-facing rounds, so English polish matters. Overall he fits an operations or program manager track well.
```

### `sample_transcript_assignment_2.txt` (software engineer candidate)

```
Topics Covered:

- Angular Ionic hybrid mobile work
- API and service layers
- Capacitor camera and files
- AI tools in coding
- Angular and React state tools
- Tailwind design setup

Candidate Profile:
Software Engineer — Senior-level
The talk centers on hybrid mobile work with Ionic, Angular, Capacitor, Tailwind, and React-style state.
The candidate also explains services, errors, performance, and day-to-day use of AI coding tools.

Candidate Summary:
The candidate has over nine years of software development experience. He focuses on Angular, React, Ionic, Capacitor, Tailwind, APIs, and AI helpers like Cursor. His strengths are reusable UI, clear service layers, and practical performance ideas for big lists. One gap is live Redux and Zustand depth was stopped early in this interview. Overall he looks like a strong senior mobile and web engineer.
```

## Reflection

- Worked well: one API attempt plus readable fallback keeps the script easy to demo.
- Limits: Fallback mode only guesses from plain keywords, so thin transcripts stay shallow.
- Next step I would try: tighten topic labels with ten more transcript-specific phrases instead of touching the layout again.
