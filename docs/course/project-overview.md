## What SPLASH Is

**SPLASH — Self-Paced Learning in Applied Software for Humanity — is a self-directed, experiential learning environment for the practice of user-centered and system-oriented software engineering.** You carry out a complete engineering project on a real problem, without a predefined solution, prescribed lifecycle, fixed methodology, or sequence of technical tasks.

Your responsibility is to investigate a situation, determine where software can create a meaningful change, formulate an engineering response, and establish through evidence whether that intervention produced the intended effect. SPLASH therefore develops and assesses your ability to act under engineering uncertainty Engineering uncertainty A situation in which important information, constraints, causal relations, stakeholder expectations, technical feasibility, or outcomes are not fully known in advance. In SPLASH, uncertainty is something you investigate and manage, not something the instructor removes for you. rather than your ability to follow a recipe.

The SPLASH Principle

Your goal is not to prove that you can build software. Your goal is to demonstrate that you can **reason and act as a software engineer when neither the problem, the solution, nor the path between them has been predetermined.**

What You Are Expected to Do

SPLASH gives you substantial freedom over the subject, scope, process, and technical form of your project, but that freedom does not mean that the expected engineering work is undefined. By the end of the experience, your team must be able to show that it has carried out the following responsibilities as a coherent engineering process.

Build a software product

Define, implement, integrate, and operate a working software intervention whose scope is appropriate to the problem you chose.

Define how you will investigate and engineer

Construct and justify a **scientific method of investigation** and an **engineering approach** suited to the uncertainty, constraints, stakeholders, and evidence available in your context.

Control resources and costs

Identify the resources your project consumes, evaluate their cost and availability, monitor how they are used, and justify that expenditure against the value your solution is expected to create.

Solve a real problem

Document the problem, trace its source through the larger system, define the part you can realistically address, and demonstrate that your intervention changes the problem within that declared scope.

Demonstrate impact

Define what impact means for your project, establish observable criteria and a baseline, collect evidence, and show what changed in the real target context because of your intervention.

Assure quality

Define the qualities that matter for your product and process, establish defensible validation criteria, gather evidence against them, and continuously judge whether the project meets the level of quality you claim.

These Responsibilities Are Interdependent

They are not six independent deliverables to complete one after another. Your investigation shapes the problem you frame; the problem constrains the software you build; resource limits influence your engineering choices; quality criteria shape how you evaluate the result; and the operation of the solution allows you to judge its impact. SPLASH assesses how coherently you manage these relationships across the project.

## Start from the Problem, Not the Product

SPLASH is not an exercise in finding a justification for an application you already want to build. Statements such as *“we will build a recommendation system,” “we will create a platform,”* or *“we will train an AI model”* describe possible solutions. They do not establish what problem exists, why it exists, or whether that solution addresses its source. Before committing to a product, you must establish what is happening, who and what participate in the situation, where the relevant constraints or failures occur, and why a computational intervention is an appropriate response.

How do you define a problem properly?

The problem must concern **real users or stakeholders in a real context**, and your team must document that it actually exists. Plausibility is not enough.

A well-defined problem should make clear:

- **what is happening**;
- **who or what is affected**;
- **where the problem occurs in the larger system**;
- **what conditions, constraints, or mechanisms sustain it**; and
- **how you know the problem is real**.

Depending on the project, appropriate evidence may come from observations, interviews, operational data, existing processes, incidents, measurements, market evidence, scientific literature, institutional documentation, or other defensible sources.

## Software Inside a Larger System

In SPLASH, contemporary software is not treated as an isolated application. It operates within larger systems System-oriented view The software is analysed as one component among people, organizations, devices, policies, workflows, data sources, infrastructure, external services, and other software systems. The relevant unit of analysis is therefore larger than the codebase itself. involving people, organizations, physical infrastructure, regulation, economic processes, data flows, external services, and heterogeneous technical systems.

A web interface, mobile application, machine-learning model, API, library, embedded component, or decision-support tool may therefore be only one element of the intervention required to address a problem. Your first task is not to decide what application to build. It is to understand the system in which the problem exists.

**1. Observe the system** Identify actors, processes, dependencies, constraints, information flows, and observable effects.

**2. Locate the mechanism** Determine where the problem is produced or sustained rather than stopping at the visible symptom.

**3. Design the intervention** Define where computation can alter that mechanism and what evidence would show that it worked.

## Follow the Problem Through the System

A frequent engineering mistake is to assume that the person ultimately affected by a problem must also be the direct user or client of the software solution. SPLASH requires you to question that assumption.

The observable difficulty experienced by an end user may originate elsewhere: in an organizational process, an information flow, an interoperability failure, a resource-allocation mechanism, a decision process, an upstream supplier, an institutional constraint, or another technical subsystem. You are expected to trace the problem through its value chain Value chain The sequence of actors, activities, resources, information, and transformations through which value is created, transferred, or blocked. In SPLASH, following the value chain helps locate the point where a software intervention can have the greatest justified effect. and causal structure until you identify an intervention point where computing can realistically act on the mechanism sustaining the problem.

Four Roles That May Be Different

The user experiencing the problem, the stakeholder owning the problem, the actor capable of changing the situation, and the direct user of your software may be four different entities.

## Computing as an Engineering Instrument

In SPLASH, computing is understood in its broader historical and engineering sense: the **processing of computation and information to support problem solving and decision making through mathematics, modelling, and automation.**

Computing is therefore not reduced to building interfaces, managing databases, or automating existing tasks. It provides engineers with ways to represent aspects of the world, formalize relationships and constraints, process information, evaluate alternatives, simulate behaviours, support decisions, and automate actions where appropriate.

Observe Model Represent Compute Intervene Measure effect

Your responsibility is to determine **what should be modelled, what information is relevant, what can be computed, what should be automated, and how those computational mechanisms can contribute to resolving the problem within the larger system.**

Programming may be necessary to implement that intervention, but programming is not the central learning objective of SPLASH. The software is the computational intervention through which your engineering reasoning acts on the system.

## Your Mission

The Objective

Develop a software-based intervention for **real users or stakeholders** addressing a **real, documented problem**. Define the intended impact, establish observable success criteria, and collect evidence throughout the project. By the final defense, demonstrate that the problem, **as operationally defined within your declared scope**, has **disappeared or been reduced to the success threshold you established in the real target context, without relying on hypothetical future conditions, unavailable data, missing integrations, or dependencies that are not yet in place**—and present a credible strategy for scaling that effect.

Your subject is open, but your project must satisfy the following requirements:

- Address a **real, documented problem**.
- Target **real users, stakeholders, or operational actors** in a real context.
- Define the intended **impact** and how it will be observed.
- Use **software as the main engineered intervention**, understood as one component of a larger system.
- Define an appropriate software scope, from a full-stack product to a library, service, model, API, embedded component, or other software subsystem.
- Operate under **limited time and resource constraints**.
- Apply **software engineering principles and practices throughout the project lifecycle**.

Before You Commit to an Idea

Most problems you are likely to identify have already been addressed in some form. Turning an existing algorithm, model, or technique into an accessible product is therefore not, by itself, necessarily a sufficiently substantial engineering problem to solve. Accessibility can be a legitimate problem, but simply packaging an existing solution often leaves deeper technical, organizational, economic, regulatory, or operational difficulties unexplored.

Before committing to an idea, ask yourself: **why has this not already been done by professional engineers?** The answer may reveal the real engineering problem.

Likewise, the fact that large companies have access to far greater resources is **not a valid reason to conclude that your team cannot address the problem**. Resource limitations are part of the engineering context and must be managed explicitly. Similarly, delegating a difficult part of the problem to another organization simply because your team does not yet know how to solve it does not remove that difficulty from the engineering problem.

## Define and Measure Impact

Define Success Before You Claim It

You cannot define success retrospectively from whatever your system happens to produce. Your impact criteria must be explicit enough that the observed results can challenge your expectations rather than merely confirm them.

SPLASH does not prescribe what kind of impact matters. Impact may be economic, operational, environmental, societal, social, organizational, scientific, accessibility-related, safety-related, educational, or take another form justified by the problem.

Your team must define:

- **who or what** is expected to be affected;
- **what observable change** would constitute an improvement;
- **how that change** can be measured or otherwise observed;
- **what baseline or comparison** is appropriate;
- **what criterion or threshold** would justify claiming that the problem has been resolved within your declared scope.

## Engineering Under Resource Constraints

Engineering is performed under constraints. Time, labour, data, stakeholder access, computing capacity, infrastructure, licenses, money, attention, and organizational availability are finite resources. Even when team members are not paid by the project, their time still has an economic value.

You **must identify** the resources your project consumes, quantify their cost and availability, and monitor their use throughout the project. These resources must be treated as engineering constraints. You **must justify** engineering choices against the value they are expected to create and revise those choices when their cost, complexity, risk, or delay is no longer justified by that value.

Example — “Free” Resources Still Have a Cost

Jean and Jacques are working on an unpaid student project. Jean spends **8 hours** on the project and uses a **Visual Studio license provided by the university**.

Neither Jean’s time nor the software license is truly free. The cost is simply borne by someone else — for example the student, the university, or another organization. SPLASH therefore requires you to **identify and quantify these resources**, even when your team does not pay for them directly.

The objective is not necessarily to reimburse or monetize every resource, but to understand the real resources consumed by the project and who bears their cost.

More Is Not Automatically Better

A technically more sophisticated solution can still be an inferior engineering decision if its additional cost, resource consumption, complexity, or operational burden is not justified by a corresponding improvement in impact.

## Your Working Release

Your team defines what constitutes its working release Working release A release that is operationally complete within the scope your team claims and can be exercised under the real conditions required to support those claims. Its scope may be deliberately narrow; what matters is that the demonstrated behaviour is real rather than hypothetical. . SPLASH does not prescribe its size or architectural form. It may be a complete full-stack application, a service, an algorithmic component, an API, a library, an embedded subsystem, an analytical pipeline, or another software component appropriate to the intervention you designed.

What matters is not breadth but **operational completeness within the scope you claim**. If the scope is too large to demonstrate honestly with the resources available, reduce the scope rather than replacing evidence with promises.

A Working Release Is Not a Prototype or a Promise

Statements such as “the banking workflow will work once we have access to the real payment system” or “the model should work once real training data becomes available” describe unresolved dependencies, not a demonstrated working release. A prototype can be useful during the project, but your final claims must rely on operation with the real data, integrations, dependencies, and conditions required to support them.

**Reduce the scope if necessary, but demonstrate what you claim.**

## Two Outcomes Exist in SPLASH

Engineering outcome

Change the real situation

Your team places a functioning software intervention into a real context and determines whether it produces the effect you defined.

Learning outcome

Demonstrate engineering competence

Each student demonstrates engineering competence through the course Learning Outcomes, which become observable through reasoning, decisions, actions, reflection, adaptation, and professional practice.

These outcomes are related, but they are not equivalent. A successful product does not automatically demonstrate competent engineering: it may succeed through luck, inappropriate shortcuts, external assistance, or decisions that cannot be justified. Conversely, a project may encounter serious limitations while still producing strong evidence of engineering competence if those limitations are investigated, understood, managed, and incorporated into subsequent decisions.

Production Is Not the Priority

SPLASH is not organized around being right or wrong, and its purpose is not simply to obtain a finished product. The project exists because authentic engineering activity creates situations in which competencies can be acquired, exercised, challenged, and demonstrated.

**Your software is the vehicle of the learning experience, not its sole purpose.** The purpose of the learning experience is to develop an understanding of how engineering processes, decisions, constraints, uncertainty, and resource choices influence the quality and consequences of a real large-scale project.

## Your Team

Form Your SPLASH Team

To join a SPLASH team, go to [**Brightspace \> Community \> Groups \> SPLASH**](https://brightspace.uwindsor.ca/d2l/groups-sections/227327/groups/management/category/6068) and select an available SPLASH group. The list of students enrolled in SPLASH is also available on SharePoint and can be used to identify potential teammates.

[👥 View the SPLASH participant list on SharePoint](https://uwin365.sharepoint.com/sites/Section_COMP8117-1-R-2026F/Lists/COMP8117_Students_List_202603F/AllItems.aspx)

- Your team is composed of 4 members.
- You respect mixity and parity where possible (men/women, juniors/seniors).
- You designate one team leader.

Although team composition is flexible, it must be justified by the needs of the project. Your choices should reflect the expertise, roles, workload, coordination demands, and constraints required to carry out the work effectively.

The team defines its roles, internal governance, working agreements, technical responsibilities, decision process, timeline, lifecycle, documentation strategy, and coordination mechanisms. These choices are not administrative details: they are part of the engineering system you create to make the project possible.

## Demonstrating Competencies

### You Are the Judge

SPLASH deliberately places part of the responsibility for judgment on you. You are expected to evaluate engineering processes, artifacts, claims, and competency demonstrations **critically and scientifically**. Judgment must be grounded in evidence, explicit criteria, and defensible reasoning—not preference, intuition, confidence, or opinion.

For the dimensions of the project you evaluate, your team must develop its own rubrics Student-Defined Rubrics A rubric makes your quality model explicit: what dimensions matter, what evidence is relevant, and what distinguishes weak, acceptable, and strong performance. A rubric is not merely a scoring table. It is an argument about what quality means in the context of your project. and validation criteria Validation Criteria Observable conditions used to decide whether a requirement, hypothesis, process, release, impact claim, or competency claim is sufficiently supported. Criteria should be defined before the result is known whenever possible, so that success is not redefined retrospectively. . You must explain why those criteria are appropriate, what conception of quality they embody, what evidence can test them, and what limitations or trade-offs they introduce.

Judge from Evidence, Not Opinion

A statement such as *“we think this is good”* is not an engineering evaluation. A defensible judgment identifies the claim being evaluated, the criteria used, the evidence collected, the method used to interpret that evidence, and the reasoning that connects the evidence to the conclusion.

Your rubrics and validation criteria must then be **confronted with the rubrics provided by the teaching team**. The purpose is not to copy the teaching-team rubric or treat it as an answer key. Compare the two quality models, identify agreements and disagreements, examine what each one emphasizes or omits, and justify whether your own criteria should be retained, revised, or rejected. This comparison is itself evidence of your capacity for critical engineering judgment.

### Demonstrating Competence Through Evidence

SPLASH is evidence-based. The SPLASH Skills Matrix identifies the competencies assessed through the project and the Learning Outcomes through which those competencies become observable. Your responsibility is to ensure that these Learning Outcomes become visible in the work you produce throughout the project.

A **competency** combines **knowledge, action, and environment**: the knowledge that can be mobilized, the actions performed using that knowledge, and the environment in which those actions must be carried out. A **Learning Outcome (LO)** is a measurable statement describing an observable manifestation of that competency at a given level.

Evidence of competence Evidence of competence An observable artifact, action, result, decision, interaction, measurement, or explanation that supports a claim about what you can do. The existence of an artifact is not sufficient by itself; you must explain what competency it demonstrates and why. may include technical artifacts, models, experiments, decision records, stakeholder interactions, measurements, analyses, demonstrations, documentation, project records, or other defensible traces of engineering work.

Evidence Must Connect Action to Learning

Do not collect artifacts merely because they exist. For each competency claim, identify the Learning Outcome through which that competency becomes observable, the artifact or activity in which it appears, and the reasoning that connects what is observed to the competency claim.

Competencies and Learning Outcomes

How to Read the Matrix

The matrix is not a checklist of documents and it is not a complete grading rubric.

| Competency assessed in SPLASH | A.1  ASE.A.1 Apply various software development models such as waterfall model, iterative model and agile development. | B.1  ASE.B.1 Access, retrieve and analyze the latest technical information on software development, testing and verification from a variety of sources. | C.1  ASE.C.1 Apply object-oriented design and analysis techniques for software development. | D.1  ASE.D.1 Interpret informal user specifications to create accurate project requirements and deliverables. | F.1  ASE.F.1 Clearly and effectively communicate software functionalities through technical reports and oral presentations. | G.1  ASE.G.1 Work in a team environment and co-ordinate implementation of different project components with others. | I.1  ASE.I.1 Identify recent developments in software engineering and communicate how they affect current practice. |
|----|----|----|----|----|----|----|----|
| Apply a scientific method | × | × | × |  |  |  |  |
| Reason across disciplines |  | × |  | × |  | × | × |
| Arbitrate under constraints | × |  | × |  |  | × |  |
| Evaluate technical consequences |  |  | × |  |  |  |  |
| Produce added value |  |  |  | × |  |  |  |
| Design human-centred systems |  |  | × | × |  |  |  |
| Advise in service of other fields |  |  |  |  | × |  |  |
| Organize large-scale teams |  |  |  |  |  | × |  |
| Justify through literature |  | × |  |  |  |  | × |
| Judge literature critically |  | × |  |  |  |  | × |
| Adapt knowledge to new contexts | × |  |  |  |  |  | × |
| Learn autonomously |  | × |  |  |  |  | × |
| Demonstrate professionalism |  |  |  |  | × | × |  |
| Distinguish engineering from development | × | × |  | × |  |  | × |
| Model formally |  |  | × | × |  |  |  |

**×** = associated Learning Outcome  ·  Hover a LO code to view its full statement.

You do not need to create a separate artifact for every Learning Outcome. The same artifact, decision, method, milestone, or demonstration may make several Learning Outcomes observable. Across the project, the Learning Outcomes associated with the assessed competencies must become visible in your work.

## Autonomy Is Part of the Assessment

You receive

- The overall SPLASH objective and constraints.
- The course Learning Outcomes and SPLASH Skills Matrix.
- Three suggested expert-review dates.
- Access to teaching-team expertise, questions, and resources.
- Feedback on the work and reasoning you choose to present.

You decide

- The problem-framing and investigation strategy.
- The lifecycle, methodology, milestones, and project-management approach.
- The software scope, architecture, technologies, and engineering practices.
- The team organization and schedule.
- The evidence, metrics, and criteria used to demonstrate your claims and competencies.

Autonomy Does Not Mean Working Without Supervision

Autonomy does not mean the absence of monitoring, guidance, or discussion. The teaching team will not continuously chase your team for updates or tell you when to seek help. **It is your responsibility to approach the teaching team, discuss your decisions, expose uncertainties, and request feedback when it is useful.**

Being autonomous also does **not** mean that you are expected to work alone or avoid supervision. Knowing when to seek expertise, challenge your reasoning, or discuss a difficult decision is itself part of professional engineering practice.

SPLASH deliberately does not prescribe **how you organize and conduct the engineering work**. This is not an absence of expectations. **Choosing, justifying, adapting, and evaluating your approach is itself part of the engineering work you must demonstrate.**

Your team must therefore be capable of explaining what it did, why the chosen approach was appropriate, what alternatives were considered, **what information informed its decisions**, what assumptions and risks were accepted, and how the approach evolved when the environment contradicted those assumptions.

## The Teaching Team Does Not Own Your Decisions

The teaching team acts as an **expert resource, challenger, and provider of learning opportunities**. It can answer general questions about course content, assist with technical issues, provide resources such as computers, devices, software, and space, challenge assumptions, expose contradictions, identify overlooked perspectives, discuss alternatives, and help you interpret evidence.

Guidance Is Not Validation

The role of the teaching team is not to approve your methodology, certify your architecture, validate your requirements, choose your technologies, or determine whether a decision is “correct.” Its role is to open questions and debates; responsibility for the decision remains with your team.

**Receiving no objection from an instructor is not evidence that a decision is sound.**

## Milestones Are Expert Reviews, Not Approval Gates

SPLASH provides **three scheduled milestones**. Their purpose is not to authorize your next phase or tell you whether the project is “good.” They create three structured opportunities to expose your current reasoning and project state to **expert scrutiny** while there is still time to act on what you learn.

1.  Present the current state of the problem, project, and evidence.
2.  Show which Learning Outcomes are observable in your current work and which competencies they make visible.
3.  Confront your decisions, assumptions, and interpretations with expert questions.
4.  Identify blind spots, unresolved assumptions, and weaknesses in the evidence.
5.  Decide whether and how your trajectory should change.

The three scheduled milestones are a **minimum pedagogical structure**, not your project lifecycle. Your team defines its own internal milestones and may request additional expert reviews whenever they are useful.

## What You Submit at Each Milestone

Each milestone requires two complementary forms of documentation: a **team progress report** and an **individual reflective report**.

Team evidence

📄 Progress Report — What is happening to the project?

The progress report maintains a trace of the project as an evolving engineered system. It records how the project has evolved relative to previous expectations: problem understanding, scope, stakeholders, assumptions, requirements, architecture, resources, schedule, risks, experiments, evidence, costs, and observed outcomes.

**Its purpose is not to advertise progress. It makes project evolution inspectable and traceable.**

Individual evidence

🧠 Reflective Report — How am I reasoning as an engineer?

The reflective report makes your reasoning inspectable. You explain what you believed, what evidence supported that belief, what alternatives you considered, why you selected a course of action, what you expected to happen, what actually happened, and how the result changes your understanding or next decision.

**It is not a diary or a contribution summary; it makes your engineering judgment and learning observable.**

Documentation guidance and templates are provided in the instructions for each milestone, in the course material, and in the additional course resources. **Use them as memory aids and structural prompts to identify what should be considered, documented, and made explicit. Adapt them to your project and engineering approach, and do not treat them as prescriptions.**

## Final Defense

In week 12, your team presents a **final defense** with the working release and the engineering documentation produced throughout the project. The defense includes a **demonstration of the working release** and an evidence-based engineering argument connecting the problem, intervention, engineering process, observed effect, and impact.

**Be careful: this is not a product pitch.** Although you must be able to advocate for your product and demonstrate its business impact, you **must not** develop or present a business model.

You demonstrate that:

1.  **The problem is real.** Demonstrate that the problem is **real, bounded, and documented** using evidence from the actual target context.
2.  **The intervention is appropriate and feasible.** Show that the intervention point and software scope follow from your analysis of the larger system rather than from a predetermined product idea, and that the computational intervention can operate under the intended conditions.
3.  **The product works.** Demonstrate the working release in operation, with the relevant data, integrations, users, dependencies, and operating conditions required to support the claims you make about it.
4.  **The engineering method protects quality while managing resources.** Show that your engineering choices were **deliberate, informed, traceable, and adapted as evidence changed**, and explain how your process, controls, trade-offs, resources, uncertainty, and constraints influenced product quality and project outcomes.
5.  **The solution removes the problem.** Provide observed evidence that the defined problem **disappeared, or was reduced to the success threshold you established, within the operational scope of the project**, rather than relying on hypothetical future performance.
6.  **The impact is real and scalable.** Demonstrate that the observed effect constitutes meaningful impact according to the criteria you defined, and present a **credible strategy to scale** that effect, including the additional technical, organizational, human, data, regulatory, or financial conditions that would have to be addressed.
7.  **The entire reasoning is evidence-based.** Show that your problem framing, assumptions, system analysis, engineering choices, validation criteria, quality judgments, interpretations, and conclusions are grounded in evidence rather than opinion.

## Project Evaluation

**Project evaluation takes place at the end of the semester.** The intermediate milestones are formative expert reviews; their assessment is used only to determine the **Competency Floor**. They do not determine the final project grade.

Your evaluation rests on the evidence and metrics you provide. SPLASH does not award marks simply for effort, volume of code, number of features, or adherence to a preferred methodology. The relevant question is what your evidence demonstrates about the quality of the intervention and engineering process, and **what your individual work makes observable about your learning and competencies**.

| Component | Weight | Format | Assessed on |
|----|----|----|----|
| Product quality | 15% | Group | OriginalityOriginalityOriginality does not require inventing something that has never existed before. It refers to the extent to which the solution, its framing, or its engineering choices emerge from the team’s own analysis, reasoning, adaptation, and synthesis rather than from merely reproducing an existing solution., operational completeness, fitness for the target context, documented impact, and the extent to which the intervention resolves the defined problem within its declared scope. |
| Methodology quality | 15% | Group | Rigour, coherence, adaptability, traceability, and justified use of software engineering principles and resources across the lifecycle. |
| Reflection | 10% | Individual | Quality of the reasoning made visible through reflective reports, including assumptions, evidence, alternatives, expected effects, observed effects, and learning. |

Competency Floor

Your demonstrated level of competency is determined through the relevant Learning Outcomes made observable in your work. The **Competency Floor** guarantees a minimum grade corresponding to the competencies you have demonstrated, independently of whether every project ambition is ultimately achieved.

## What You Take Away from the Course

SPLASH is intended to leave you with more than a grade.

A portfolio-ready engineering project

You finish with a real software engineering project grounded in an actual problem and supported by evidence of its operation, impact, engineering decisions, and constraints—not only screenshots or source code. **You can present this experience in your CV, portfolio, and job interviews as a concrete example of engineering work carried out in a real context.**

Engineering methods learned through experience

You practice selecting, adapting, evaluating, and revising engineering approaches under uncertainty, incomplete information, heterogeneous stakeholders, resource constraints, and real consequences.

Experience creating measurable impact

You learn to connect software engineering decisions to observable changes in a real context, and to judge whether those changes are sufficient to claim that the intervention has actually addressed the problem.

The central outcome is not that you have followed one particular “advanced” methodology. It is that you have learned how to **construct and revise an engineering approach in response to reality**, and that you can make the corresponding competencies observable through your work.

## Calendar

About Deadlines

Milestone deadlines are indicative, and no late penalty applies. However, delaying a milestone also delays your expert review and reduces the time available to investigate feedback, revise your reasoning, collect new evidence, and change course before the final defense.

The SPLASH project runs for **10 production weeks**. **Week 1 begins on September 17, and Week 10 ends on November 25.** Reading Week counts as a production week even though no deliverable is expected during that period.

| Milestone | Indicative Deadline |
|----|----|
| Expert Review 1 | ~~October 7 — End of Week 3~~ **October 9** |
| Expert Review 2 | October 28 — End of Week 6 |
| Expert Review 3 | November 18 — End of Week 9 |
| Final Defense (Academic Week 12) | December 2–9 |

## AI Use and Collaboration

Disclose, Verify, Remain Accountable

Generative AI use and collaboration are permitted within the limits established by the course rules. In particular, **collaboration between teams and the use of generative AI must be disclosed**, including the tool used, its purpose, and the measures taken to verify its outputs. Your submissions must remain original, and responsibility for every engineering claim, decision, artifact, and result remains with you.
