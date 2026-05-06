# Interview Transcript Summarizer

A simple Python script that converts raw interview transcripts into a clear, structured summary.

The output always includes:
- Topics Covered (4–6 concise points)
- Candidate Profile (role + level with reasoning)
- Candidate Summary (focused, readable paragraph)

This solution prioritizes **clarity, consistency, and control over complexity**.

---

## How to Run

```bash
python summarizer.py sample_transcript_assignment_1.txt
python summarizer.py sample_transcript_assignment_2.txt
```

## API Usage
If OPENAI_API_KEY is set → uses one OpenAI call (gpt-4o-mini)
If not → uses a simple fallback logic
Script never crashes — always produces output
Set API Key

PowerShell
$env:OPENAI_API_KEY="your_key_here"

CMD
set OPENAI_API_KEY=your_key_here

## Model Used
OpenAI gpt-4o-mini
Single prompt call (no multi-step pipelines)

## Output Examples (Fallback Mode)
These outputs were generated without API, using simple keyword-based logic.

### sample_transcript_assignment_1.txt (Operations / Program Profile)

Topics Covered:

- Fraud prevention
- Vendor management
- CRM upgrades
- KPI tracking
- Analytics dashboards
- Dialer integrations

Candidate Profile:
Operations / Program Manager — Mid-level
The candidate shows experience in fraud systems, vendor handling, CRM rollout, and performance tracking.

Candidate Summary:
The candidate has a background in operations and analytics with experience in fraud detection and process improvement. They have worked on CRM systems, dashboards, vendor workflows, and integrations. Their strengths include ownership and execution. A concern is communication clarity in high-stakes stakeholder settings. Overall, they fit well as a mid-level operations or program manager.


### sample_transcript_assignment_2.txt (Software Engineer Profile)

Topics Covered:

- Angular development
- Ionic mobile apps
- API integration
- State management
- Performance optimization
- AI coding tools

Candidate Profile:
Software Engineer — Senior-level
The candidate has strong experience in Angular, React, and mobile development using Ionic.

Candidate Summary:
The candidate has over nine years of experience in software development. They work mainly with Angular, React, and mobile apps. They focus on APIs, reusable components, and performance. They also use AI tools in their workflow. One limitation is less depth in advanced state management tools. Overall, they are a strong senior frontend engineer.


## Prompt Iteration Approach

Instead of forcing a perfect prompt initially, the approach was iterative:

First output was too vague and hard to scan
Added sections → improved readability
Added strict rules → removed randomness and inconsistency

Final result:

Stable structure
Clear separation of information
No unnecessary hallucination

## Design Decisions
Keep logic simple and readable
Use one API call only
Avoid unnecessary abstractions
Add fallback to ensure reliability without API

## Evaluation Focus
This solution is built to demonstrate:
Clear thinking over complex implementation
Ability to control LLM output
Structured reasoning and iteration
Practical engineering decisions under time constraints

##Limitations
Fallback logic is keyword-based (not semantic)
Limited depth without API
Output quality depends on transcript clarity
What I Would Improve
Smarter fallback using lightweight NLP
Better role detection across mixed profiles
Optional multi-step prompting for higher accuracy

##Summary
This project focuses on:
Clarity over complexity
Consistency over randomness
Practical implementation over overengineering

It is intentionally simple, reliable, and easy to reason about.


---

## Reflection

What surprised me was how random the output could be at first. Small changes in the prompt made a big difference in how clean and readable the result was.

If I had more time, I would improve how topics are extracted from the transcript so they are more accurate and less keyword-based.

One limitation is that the output still depends on the transcript quality. If the transcript is unclear, the summary can also be slightly inconsistent.

---


