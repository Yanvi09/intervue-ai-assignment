# Prompt iterations

## Iteration 1

### Full prompt

```
Summarize this interview transcript in a helpful way:

{transcript}
```

### Small transcript excerpt

`Candidate: I have nine plus years in software development. Core stack is Angular, React, Ionic...`

### Output

"The candidate has over nine years of experience in software development, primarily working with Angular, React, and Ionic. They have built mobile applications and worked on various frontend technologies, including APIs, dashboards, and responsive design. The candidate also discussed topics such as performance optimization, state management, and reusable components. Overall, the candidate seems like a strong senior frontend developer."

### Reasoning

- The output was hard to scan and everything was mixed together.
- It was one long paragraph, so it was difficult to understand what was actually important.
- It was also unclear what exactly was being said, because topics, strengths, and summary were all combined.
- So I decided to break the output into sections and separate the information.

---

## Iteration 2

### Full prompt
```
You are analyzing an interview transcript.

Return three sections:

1. Topics Covered
2. Candidate Profile
3. Candidate Summary

Transcript:

{transcript}
```
### Small transcript excerpt

`Candidate: I built CRM and dashboards around fraud KPIs and managed vendors nationwide...`

### Output

Topics: fraud KPI vendor CRM dashboards leadership BPO stakeholder tradeoffs escalation.

Profile: Program manager with fraud background.

Summary: Candidate worked on fraud dashboards and coordinated vendors...

### Reasoning

- This version was easier to read because the content was separated into sections.
- But it was still not clean enough.
- Topics were not clearly defined and sometimes too long.
- The format was still inconsistent and could change between runs.
- So I decided to add stricter rules and better structure to control the output.

---

## Iteration 3 (Final)

### Full prompt
```
You are an AI assistant that analyzes interview transcripts.

Your task is to generate a structured summary with exactly 3 sections:

1. Topics Covered
   - List 4–6 main topics
   - Keep each topic short (2–5 words)
2. Candidate Profile
   - Predict role and level
   - Give 1–2 line reason
3. Candidate Summary
   - 3–6 sentences
   - Include background, strengths, concerns, impression

Rules:

   Keep it simple
   Do not hallucinate
   Use only transcript content

Output Format:

Topics Covered:

...
...

Candidate Profile:
<Role — Level>
<1–2 line reason>

Candidate Summary:
<3–6 clean sentences>

Transcript:
{transcript}

```
### Small transcript excerpt

`Interview focus stays on Ionic grid performance... pagination... capacitor camera filesystem... Angular modules plus NgRx for scale...`

### Output

Topics Covered:
- Angular Ionic development
- API integration
- Capacitor plugins
- State management
- Performance optimization

Candidate Profile:
Software Engineer — Senior-level
Strong experience in Angular, Ionic, and mobile-first development.

Candidate Summary:
The candidate has around nine years of experience in software development. They work mainly with Angular, React, and mobile apps using Ionic. They show good understanding of APIs, reusable components, and performance. One limitation is less depth in some advanced state tools. Overall, they fit well as a senior frontend engineer.

### Reasoning

- In this version, I focused on making the output readable and structured.
- I added clear sections so the intent is visible from the beginning.
- I also added limits and rules to avoid randomness.
- The format now stays consistent and is easy to scan.
- It works for different transcripts without breaking structure.