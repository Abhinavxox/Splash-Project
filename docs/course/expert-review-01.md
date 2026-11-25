## Context & Purpose

SPLASH places you in charge of investigating a real problem and developing a software-based intervention within a larger system. Unlike a conventional software development assignment, neither the problem-solving approach nor the engineering process is prescribed. **Your team must establish both.**

The first Expert Review provides an opportunity to examine the foundations of your project while important decisions, assumptions, and uncertainties can still be challenged.

At this stage, the objective is not to demonstrate a completed design or a substantial amount of implemented software. The objective is to demonstrate that your team has begun to understand the problem, has investigated the information needed to make informed decisions, and has established a coherent engineering approach for the work ahead.

The teaching team will examine the reasoning and evidence you choose to present, identify potential weaknesses or overlooked considerations, challenge assumptions, and discuss possible alternatives.

Formative engineering consultation — not an approval gate

Your team remains responsible for every decision, including whether and how to act on expert feedback.

## Review Objectives

This first review focuses on five complementary dimensions of your engineering work.

| Dimension | Central question |
|----|----|
| Problem Investigation | What problem are we addressing, and what evidence supports our understanding? |
| Information Sources & Engineering Justification | What information supports our decisions, and why should we trust it? |
| Development Lifecycle & Engineering Process | How have we decided to conduct the engineering work, and why is this approach appropriate? |
| Development Environment & Team Organization | How have we organized the team and established the means to collaborate, develop, and control the work? |
| Project Planning & Feasibility | What do we intend to accomplish, with which resources, according to what schedule, and how will we recognize success? |

These dimensions are interconnected. Your understanding of the problem influences the lifecycle you select, the activities you plan, the expertise you need, the risks you accept, and the evidence you must collect.

**The purpose is not to produce five unrelated documents, but to demonstrate the coherence of your initial engineering strategy.**

## What the Expert Review Will Examine

### 3.1. Problem Investigation — Understanding Before Solving

Before defining a solution, your team must investigate the situation in which the problem occurs.

Your investigation should extend beyond the immediately visible symptoms. Consider the larger system, its actors, processes, dependencies, constraints, and mechanisms that may produce or sustain the problem.

You should be prepared to explain:

- What situation or phenomenon led your team to identify the problem?
- Who or what is affected, and in which real operational context?
- What evidence demonstrates that the problem actually exists?
- What are the potential causes, and how have you investigated them?
- How does the problem relate to the larger system and its value chain?
- Where might a software-based intervention create a meaningful change?
- What assumptions remain unresolved, and how do you intend to investigate them?

Distinguish observations, interpretations, hypotheses, and decisions

Observing that users experience long processing times does not automatically establish that the software architecture is responsible. Your investigation must identify possible mechanisms and gather evidence to evaluate them.

An incomplete investigation is expected at this stage. What matters is that your team can identify what is currently supported by evidence, what remains uncertain, and how it intends to reduce that uncertainty.

### 3.2. Information Sources — Investigating and Justifying Engineering Knowledge

Software engineering decisions should not rely solely on personal preferences, familiarity with a technology, or unexamined assumptions.

Your team is expected to identify, retrieve, evaluate, and use information relevant to both the problem and the engineering approach.

Depending on your project, information may come from scientific publications, professional standards, technical documentation, stakeholders, operational observations, existing systems, measurements, experiments, or other defensible sources.

Your review should address:

- **Information needs:** What did you need to understand before making your initial decisions?
- **Source identification:** Where did you search, and how did you identify relevant information?
- **Source credibility:** What makes the selected sources trustworthy, current, and appropriate for the question?
- **Critical comparison:** Do different sources support the same conclusions? Where do they disagree?
- **Engineering application:** How did the information influence your interpretation of the problem, your choice of methods, or your technical decisions?
- **Remaining gaps:** What important information is still missing or insufficiently supported?

Do not limit your report to a bibliography or a collection of links.

A source becomes useful engineering evidence when you can explain what it establishes, the conditions under which its findings apply, and how those findings influence your project.

Example — Justifying a lifecycle

Selecting an iterative development lifecycle because it is popular is not a sufficient justification. A stronger argument connects the characteristics of your problem—such as uncertainty, changing stakeholder needs, or the need for repeated experimentation—to the advantages, limitations, and requirements of the selected approach.

You should also be prepared to explain alternatives you considered and why they were not selected.

### 3.3. Development Lifecycle & Engineering Process — Designing How You Will Work

SPLASH does not prescribe a software development lifecycle, methodology, or fixed sequence of engineering activities.

Your team is responsible for choosing, establishing, and justifying an approach appropriate to the nature of the problem, the project constraints, and the available resources.

Your review should examine:

- **Lifecycle selection and justification.** Explain which lifecycle or combination of approaches you intend to use, what alternatives you considered, and why the selected approach fits your project. Describe how its activities relate to uncertainties, dependencies, stakeholder interactions, technical challenges, and expected outcomes.
- **Engineering activities and workflow.** Explain how you intend to organize investigation, requirements engineering, design, implementation, integration, verification, validation, deployment, and other relevant activities. Their sequence, overlap, frequency, and form depend on the lifecycle you establish.
- **Decision-making and traceability.** Explain how important decisions will be made, justified, documented, reviewed, and revised. How will the team preserve the reasoning behind choices when circumstances change?
- **Monitoring and adaptation.** Describe the mechanisms you intend to use to determine whether your process is effective. What observations, criteria, or measures will indicate that the approach needs to change?
- **Connection between process and expected quality.** Explain how the chosen process is intended to support software quality, the reliability of engineering decisions, and the validity of your conclusions about the problem and its resolution.

Merely naming a methodology is insufficient.

Example — “We use Scrum”

Stating “We use Scrum” does not explain what the team actually does. Describe the practices implemented, how they are organized, what purposes they serve, and why they are appropriate.

Your approach may evolve throughout SPLASH. The important requirement is that the initial choice is deliberate, informed, and capable of being examined and adapted.

### 3.4. Development Environment & Team Organization — Making the Process Operational

A development process is not established simply because it has been described in a document. Your team must put in place the organizational and technical mechanisms necessary to carry it out.

The review should consider how your team has organized its work, responsibilities, collaboration, tools, and engineering environment.

- **Team organization.** Explain how responsibilities are distributed, how expertise is used, how tasks are coordinated, and how collective decisions are made. Identify the role of the team leader and the mechanisms used to manage dependencies between members.
- **Development and collaboration tools.** Present the tools established or selected for relevant activities, such as version control, task management, documentation, communication, development, testing, integration, and coordination.
- **Working practices.** Describe how the team intends to manage changes, review contributions, share knowledge, maintain consistency, and detect problems during development.
- **Operational readiness.** Identify what has already been established, what remains to be configured, and whether missing tools, access rights, knowledge, or infrastructure could prevent planned activities.

Tool selection should be justified by the needs of the project and the process, rather than by habit or popularity.

Example — A repository is not a strategy

Creating a Git repository demonstrates that a tool has been provisioned. It does not by itself demonstrate that a version-control strategy, collaboration model, or review process has been established.

Your team should explain how the selected tools and practices support the engineering activities you intend to perform.

### 3.5. Project Planning & Feasibility — Establishing a Defensible Baseline

The first Expert Review should help your team establish an initial reference against which future progress can be examined.

This reference is not a promise that everything will proceed exactly as planned. It is an explicit representation of your present expectations, constraints, commitments, and uncertainties.

Your planning should address the following dimensions:

- **Objectives and scope.** Define what the team intends to achieve, what is included in the current scope, what is deliberately excluded, and what conditions or observations might justify a change.
- **Milestones and schedule.** Establish your own internal milestones and expected outcomes. Identify relevant activities, dependencies, estimates, and responsibilities. Explain how this schedule follows from the lifecycle and engineering strategy you have selected.
- **Resources and costs.** Identify the human, technical, material, informational, and financial resources needed. Estimate their availability and consumption, including the value of team members’ time and resources provided by other organizations.
- **Initial risks.** Identify significant sources of uncertainty or possible failure, their potential consequences, and the measures you intend to take to investigate, reduce, monitor, or respond to them.
- **Quality and control mechanisms.** Identify the qualities that matter for the project, how you intend to evaluate them, and which mechanisms will help you detect problems in the product or engineering process.
- **Expected outcomes and success criteria.** Explain what observable results would demonstrate that your intervention addresses the defined problem. Identify how those results could be measured or otherwise evaluated and what evidence must be collected.

At this stage, estimates may be uncertain and some criteria may require additional investigation. Your responsibility is to make these limitations explicit rather than conceal them behind unjustified precision.

Baseline for Expert Review 02

The initial plan becomes the reference for Expert Review 02, where the team will compare actual observations with expectations, analyze deviations, and decide whether corrective actions are needed.

## The Progress Report 01 — Establishing the Project Baseline

The Team Progress Report is the central document supporting the Expert Review.

Its purpose is to make your project’s current state, engineering reasoning, decisions, and uncertainties understandable to someone who has not participated in your daily activities.

It is not a promotional document, a collection of completed tasks, or a justification written after decisions have already been made.

**It is a project-management and engineering instrument that your team should continue to maintain throughout SPLASH.**

### Suggested Report Structure

The following structure is proposed to help organize your analysis. You may adapt, reorganize, or extend it according to your project, lifecycle, and engineering strategy.

| Section | Suggested content |
|----|----|
| 1\. Executive Summary | Current understanding of the problem, proposed intervention, project status, principal uncertainties and immediate priorities |
| 2\. Problem Investigation | Problem definition, system context, stakeholders, evidence, assumptions, causal investigation and intended intervention |
| 3\. Information & Evidence | Information sources, investigation approach, critical analysis, findings and their influence on engineering decisions |
| 4\. Engineering Strategy | Selected lifecycle, alternatives, justifications, engineering activities, workflow and decision-making process |
| 5\. Team & Development Environment | Roles, responsibilities, working practices, tools, collaboration and coordination mechanisms |
| 6\. Planning & Resources | Initial objectives, scope, internal milestones, schedule, dependencies, resource estimates and costs |
| 7\. Quality, Risks & Controls | Initial quality criteria, verification and validation strategy, identified risks, mitigation and monitoring mechanisms |
| 8\. Current State & Next Steps | Work completed so far, unresolved questions, remaining setup activities and immediate priorities |
| 9\. Supporting Artifacts | References and links to documents, repositories, models, observations and other evidence supporting the report |

You are not expected to have completed every engineering activity at this stage. Your report should accurately describe what has been investigated, decided, established, initiated, or left unresolved.

If an important aspect has not yet been addressed, explain its current status, the reasons, and the intended approach.

### What Makes a Useful Progress Report?

Consider the difference between the following statements.

Weak reporting

“We selected Agile for our project because it is flexible. We created a GitHub repository and assigned tasks to the team members. The project is progressing according to plan.” **Why it is weak:** This reports claims without explaining their justification, operational meaning, or supporting evidence.

Stronger reporting

“Our initial stakeholder discussions revealed uncertainty about two operational requirements. We therefore selected a development approach based on short iterations, allowing these requirements to be investigated through successive demonstrations. We plan to review stakeholder feedback at the end of each iteration and use it to revise the requirements and implementation priorities. The first iteration is scheduled to establish the operational workflow and test our assumptions about data availability.” **Why it is stronger:** It connects the problem, uncertainty, process, and planned engineering activities.

A useful report allows a reader to trace the relationship between **evidence, interpretation, engineering decisions, planned actions, and expected consequences**.

Use tables, diagrams, models, measurements, and direct references to project artifacts whenever they help communicate that reasoning more clearly than lengthy prose.

### Suggestions for evidence-based progress reporting

- Be factual, specific, and transparent about both successes and difficulties. Generic claims such as “everything is on track” are not useful without evidence.
- Explain causes and consequences, not merely activities. A completed meeting or a list of commits is meaningful only when connected to engineering decisions or outcomes.
- Use the format that best exposes the reasoning: concise text, tables, diagrams, direct links, and measurements.
- Describe what actually happened. Do not retrospectively rewrite the initial plan to make it appear that there was no deviation.
- Use the review to ask difficult questions, not to showcase an idealized project narrative.

## Supporting Artifacts — Choosing What Should Be Reviewed

The Progress Report provides an overview of your engineering work. Supporting artifacts allow the teaching team to examine particular decisions, analyses, or results in greater depth.

**Your team is responsible for determining which artifacts are relevant and which aspects would benefit from expert scrutiny.**

Examples include:

| Artifact | Possible subject of expert scrutiny |
|----|----|
| Project Proposal | Problem framing, feasibility, intended impact and overall strategy |
| Stakeholder or System Analysis | Identification of actors, dependencies, processes and problem mechanisms |
| Investigation Records | Evidence supporting the existence, causes and interpretation of the problem |
| Software Requirements Specification | Requirement origins, clarity, consistency, completeness and traceability |
| Development Plan | Lifecycle, engineering activities, responsibilities and planned controls |
| Project Schedule | Milestones, dependencies, resource allocation and estimation assumptions |
| Architecture or Design Documents | Initial design alternatives, constraints and engineering trade-offs |
| Quality or Test Plan | Quality objectives, validation criteria and planned verification activities |
| Risk Register or Risk Plan | Identified uncertainties, consequences, mitigation and monitoring |
| Development Repository | Version-control practices, development organization and evidence of implementation work |
| Experiments or Prototypes | Feasibility investigation, assumptions tested and findings obtained |

This is a collection of examples, **not a mandatory checklist of documents**.

You should present artifacts that genuinely exist and serve a meaningful role in your engineering approach. You are not required to produce a particular specification or plan solely because its name appears in this list.

However, choosing not to produce a conventional document does not remove the engineering responsibility associated with it.

Example — Requirements without a separate SRS

If your team does not maintain a separate Software Requirements Specification, you should still be able to explain how requirements are identified, analyzed, documented, communicated, reviewed, and traced throughout development.

The review may examine both the artifacts you provide and the reasoning behind your documentation strategy.

### Preparing Artifacts for Expert Review

For each artifact selected, identify its purpose, current status, and the aspects on which you would like feedback.

Make the relevant material accessible through a direct file, attachment, repository reference, or link. When possible, identify specific sections, models, decisions, or questions rather than requiring the reviewer to discover them without guidance.

An unfinished artifact may be suitable for review. In fact, examining it before important decisions become expensive to change is often especially valuable.

## How to Request an Expert Review

Your team may obtain expert feedback through one of two channels.

### Option A — Brightspace Submission (Recommended)

Submit your current Team Progress Report together with the supporting artifacts your team has selected for review.

Include a short explanation identifying the questions, decisions, uncertainties, or technical elements on which you would like feedback.

This approach provides the teaching team with written material that can be examined and commented on.

### Option B — Meeting with the Teaching Team

Request a meeting with the professor or teaching assistants to discuss your project and selected engineering artifacts.

Prepare the current Progress Report and the relevant documents, models, repositories, or other evidence before the meeting.

Your team should be ready to present its reasoning, answer questions, explain uncertainties, and discuss alternatives. A meeting may involve inspecting technical material or discussing particular decisions rather than delivering a formal presentation.

### Requesting Additional Expertise

The three scheduled reviews establish a minimum pedagogical structure. You may request further expert consultations whenever you encounter a problem, uncertainty, decision, or engineering challenge that would benefit from external expertise.

Do not wait for a scheduled review to seek help with an important issue.

## Expert Feedback & Follow-up

The teaching team acts as an expert resource and critical interlocutor. Its purpose is to help your team examine assumptions, identify overlooked factors, question methods, interpret evidence, and explore alternative approaches.

Expert feedback should not be interpreted as a formal approval of a design, methodology, requirement, or engineering decision.

Your team must retain responsibility for evaluating recommendations and determining the appropriate response.

After receiving feedback, you should:

1.  Identify the principal observations, questions, or concerns raised during the review.
2.  Examine their relevance to your project and the evidence on which they are based.
3.  Determine whether they require additional investigation, corrective action, or a revision of existing decisions.
4.  Record and justify significant decisions made in response to the feedback.
5.  Incorporate relevant changes into your project activities, documentation, or monitoring mechanisms.

You are not required to adopt every recommendation. You should, however, be capable of explaining how you evaluated the feedback and why you decided to accept, adapt, or reject particular suggestions.

The consequences of those decisions become part of the project’s history and may be revisited during subsequent expert reviews.

## Individual Reflection & Evidence of Competence

Alongside the Team Progress Report, each student produces an Individual Reflective Report, as specified in the SPLASH project instructions.

These documents serve different purposes.

The **Team Progress Report** makes the collective project trajectory observable: what the team investigates, decides, organizes, produces, and monitors.

The **Individual Reflective Report** makes each student’s engineering reasoning and learning observable: the assumptions they formed, alternatives they considered, decisions they contributed to, evidence they used, challenges they encountered, and how their understanding evolved.

Individual reflection should not simply repeat the team report or list personal contributions.

For this first milestone, students may reflect on how they participated in understanding the problem, evaluating information, selecting engineering approaches, organizing the team, or establishing the project plan.

The work and evidence presented through SPLASH contribute to demonstrating the relevant course Learning Outcomes and engineering competencies.

## Assessment & Formative Purpose

**Weight: 0%.** This expert review does not contribute a direct percentage to the final project grade. Its purpose is to provide formative feedback and support the development and demonstration of engineering competencies.

Evidence made observable through the review may contribute to the **Competency Floor** described in the SPLASH project overview.

The teaching team will focus on the quality of your engineering reasoning, the relevance and credibility of your evidence, the coherence of your decisions, and your ability to identify uncertainties and justify your approach.

The objective is not to reward the number of documents produced or the amount of software implemented at this stage.

What a strong first review demonstrates

Your team knows what it is investigating, why it is acting as it does, how it intends to conduct the work, and what evidence will allow it to evaluate its decisions.

## Practical Advice — Preparing for Your First Review

Treat the review as a professional engineering discussion rather than an examination in which you must defend every initial decision.

Present the actual state of your work, including difficulties, missing information, disagreements, or assumptions that have not yet been tested.

Avoid reporting activities without explaining their purpose and consequences. A task completed is not necessarily an engineering problem resolved.

Be precise about what is known, what is inferred, what has been decided, and what remains to be investigated. Use supporting evidence rather than general expressions such as *“our research shows”* or *“we believe this is the best solution”* without further justification.

When presenting a method, a process, or a technology, explain how it is used in your project and why it is appropriate. Do not assume that naming a recognized methodology demonstrates its correct application.

Finally, use this first review to establish a realistic and inspectable baseline. The next review will examine how your project evolves in relation to that baseline.
