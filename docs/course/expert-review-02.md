## Context & Purpose

Your team has now been working on its SPLASH project for several weeks. During the first Expert Review, you examined the foundations of your engineering approach: problem investigation, information sources, development lifecycle, team organization, and initial planning.

You have since had the opportunity to put that approach into practice. Some activities may have proceeded as expected, while others may have encountered unexpected difficulties, revealed new information, or required changes to your initial assumptions.

The second Expert Review is an opportunity to examine how your project has actually evolved compared with what your team originally intended.

The objective is not simply to report completed tasks or demonstrate that work has been performed. It is to determine whether your engineering process is producing the expected results, understand deviations, evaluate the effectiveness of your control mechanisms, and identify appropriate corrective actions.

The teaching team will examine the evidence you provide, challenge your interpretations, and discuss alternative ways of addressing the difficulties and uncertainties you have encountered.

Formative engineering consultation — not an approval gate

**This review is a formative engineering consultation, not an approval gate.** Your team remains responsible for monitoring its project, interpreting the available evidence, and deciding whether and how to modify its engineering strategy.

## Review Objectives

This second review focuses on six complementary dimensions of your engineering work.

| Dimension | Central question |
|----|----|
| Development Progress | What has actually been achieved, and what evidence demonstrates it? |
| Planning Drift | How does the current project state compare with the previous baseline, and why have deviations occurred? |
| Corrective Actions | What decisions have been made to address deviations, and how are those decisions justified? |
| Quality Management | How is quality being controlled, verified, and evaluated throughout development? |
| Risk Management | How have risks evolved, and how effectively are they being identified, monitored, and managed? |
| Engineering Process Effectiveness | Does the selected lifecycle and engineering process work as intended, and what should be adapted? |

These dimensions are interconnected.

A delay in implementation may originate from underestimated complexity, unstable requirements, insufficient technical knowledge, ineffective coordination, or an intentional change in direction resulting from new evidence.

Similarly, an apparently successful implementation may conceal unresolved quality problems, uncontrolled risks, or an engineering process that is consuming more resources than anticipated.

**The purpose of the review is therefore not merely to identify deviations, but to understand what those deviations reveal about your engineering decisions, processes, and assumptions.**

## What the Expert Review Will Examine

### 3.1. Development Progress — Establishing What Has Actually Happened

Your team must be capable of explaining the actual state of its project using factual observations and verifiable evidence.

Progress should be examined in relation to the objectives, activities, and expected outcomes established during the previous milestone.

Your review should address:

- Which planned objectives or activities have been completed, partially completed, postponed, modified, or abandoned?
- What software components, models, experiments, integrations, documentation, or other engineering artifacts have been produced?
- What evidence demonstrates that the reported work has actually been performed?
- Which expected results have been achieved, and according to what criteria?
- What important difficulties or unexpected findings have emerged?
- What remains incomplete, and what prevents its completion?
- How have the contributions and coordination of team members influenced progress?

Avoid confusing activity with progress.

For example, spending several days implementing a feature does not necessarily mean that the project has advanced toward solving the identified problem.

The relevant question is what the activity produced, whether the result satisfies its intended purpose, and how it contributes to the project's objectives.

**Distinguish work performed, outputs produced, results verified, and objectives achieved.**

A feature may be implemented without being integrated. An integration may succeed without satisfying its requirements. A validated requirement may still contribute little to resolving the underlying problem.

Your progress analysis should make these distinctions explicit.

### 3.2. Planning Drift — Comparing Expectations with Reality

Your initial planning established expectations about objectives, activities, milestones, resources, costs, and the sequence of engineering work.

The second Expert Review requires you to confront those expectations with the observed project trajectory.

Your analysis should establish:

**The reference baseline**

Identify the planning assumptions and commitments against which progress is being compared. These may originate from your initial Project Proposal, development plan, schedule, backlog, or other planning artifacts.

**Observed deviations**

Identify differences between planned and actual progress. These may concern delivery dates, activity duration, effort, resource consumption, scope, dependencies, quality, or expected results.

**Deviation magnitude**

Whenever possible, quantify the differences using appropriate indicators, such as planned versus actual effort, milestone completion, work remaining, resource consumption, or the evolution of project scope.

**Causal analysis**

Investigate why deviations occurred. Consider technical, organizational, informational, human, environmental, and methodological factors.

**Consequences**

Explain how these deviations affect the remainder of the project, the feasibility of objectives, the resources available, and the quality or impact of the expected intervention.

Understanding deviations — not every deviation is a failure

**A deviation is not automatically a failure.**

A project may intentionally diverge from its initial schedule because new evidence reveals that an assumption was incorrect, a different intervention would be more effective, or an activity requires more investigation than anticipated.

**Schedule performance and engineering progress are not equivalent.** A project may fall behind its initial schedule while making significant engineering progress—for example, by identifying the actual mechanism behind the problem, discovering that a proposed solution would be ineffective, resolving a critical uncertainty, or identifying a more appropriate intervention.

Such discoveries may justify revising the scope, technical approach, development activities, or project schedule. The resulting deviation may therefore represent an improvement in the project's understanding, relevance, or expected quality rather than a deterioration of its engineering trajectory.

What matters is not whether the project follows its original plan without deviation, but whether the team can **identify the differences, explain their causes and consequences, and justify the decisions made in response** .

Weak analysis

> We are one week behind schedule because development took longer than expected. We will work harder to catch up.

This identifies a delay but provides no analysis of its causes, consequences, or the feasibility of the proposed response.

Stronger analysis

> Integration was originally estimated at four days but required seven. Investigation showed that the external API did not guarantee the data consistency assumed during planning. We introduced an additional validation mechanism and postponed a lower-priority feature. The revised schedule allocates two days for integration testing and preserves the next operational milestone.

This identifies the deviation, explains its cause, connects it to an engineering decision, and makes the revised trajectory inspectable.

Your team should compare actual progress with the appropriate baseline rather than retrospectively rewriting the initial plan to make the project appear on schedule.

### 3.3. Corrective Actions — Learning to Adapt Deliberately

Monitoring only becomes useful when observations influence engineering decisions.

When your team identifies a significant deviation, weakness, or change in circumstances, it must determine whether corrective action is necessary and what response is appropriate.

Your review should examine:

- What deviations or problems require action, and why?
- Which alternatives have been considered?
- What evidence supports the selected response?
- What consequences or trade-offs are associated with that response?
- Which activities, responsibilities, resources, or priorities must change?
- How will the team determine whether the corrective action is effective?
- What new risks or dependencies might the action introduce?

Corrective action may involve modifying the schedule, revising priorities, reallocating responsibilities, changing technical approaches, improving communication, investigating uncertainties, strengthening validation, or reducing the scope of an intervention.

However, corrective action should not be confused with simply moving deadlines or adding more work.

For example, when a feature takes longer than expected, assigning additional developers may not improve progress if the underlying difficulty concerns missing information or an unresolved design decision.

The appropriate response depends on the diagnosed cause.

**A corrective action is an engineering decision. It should therefore be justified, traceable, and evaluated through its observed consequences.**

Baseline for Expert Review 03

The revised strategy and planning established during this review will serve as the reference for Expert Review 03.

### 3.4. Quality Management — Controlling What You Produce

Software quality does not emerge automatically from completing implementation tasks.

Your team is responsible for identifying the qualities that matter for its intervention, defining criteria to evaluate them, and implementing mechanisms to monitor and control quality throughout development.

The second Expert Review examines how those mechanisms have been applied in practice.

**Quality objectives and criteria**

Explain which quality attributes are important for your project and why. These may concern functionality, reliability, security, performance, maintainability, usability, interoperability, accessibility, or other characteristics justified by the problem and operational context.

**Quality assurance activities**

Describe the processes and practices established to prevent defects and maintain the quality of engineering work. These may include reviews, development standards, design evaluations, automated checks, integration practices, or other relevant mechanisms.

**Verification and validation**

Explain how you determine whether the software conforms to its specifications and whether it addresses the actual needs and problem for which it is developed.

**Quality evidence**

Present available evidence, such as test results, review findings, defect records, measurements, experiments, stakeholder observations, or other forms of evaluation.

**Quality problems and corrective actions**

Identify significant defects, weaknesses, or uncertainties. Explain how they were detected, what caused them, and how the team responded.

**Quality plan effectiveness**

Evaluate whether the selected practices and criteria are appropriate and whether they need to be revised.

Do not simply report that testing is planned or that a quality plan exists.

The review should examine what quality-related activities have actually been performed, what they revealed, and how their results influenced development decisions.

Example — Quality evidence has limits

For instance, reporting that all implemented unit tests pass is meaningful evidence about the tested behaviours. It does not establish that the software satisfies stakeholder needs, integrates correctly with external systems, or produces the intended impact.

Your team must interpret each quality indicator within the scope of what it actually measures.

### 3.5. Risk Management — Managing Uncertainty Throughout Development

Risks evolve as the project progresses.

Some initial risks may have disappeared, others may have materialized, and new risks may have emerged from technical decisions, discoveries, dependencies, resource limitations, or changes in the operational environment.

Your team should be able to demonstrate that risk management is an active engineering process rather than a document produced once at the beginning of the project.

The review should examine:

**Risk evolution**

Compare the risks identified at the previous milestone with the current situation. Which remain relevant, which have changed, and which new risks have emerged?

**Risk assessment**

Explain how the team evaluates the likelihood, potential consequences, and significance of identified risks.

**Risk response**

Describe the measures selected to prevent, reduce, monitor, transfer, accept, or otherwise manage risks, as appropriate to your project.

**Observed effectiveness**

Examine whether risk-management actions have worked as intended. Were emerging problems detected early enough? Were the consequences limited? Did the selected measures introduce additional costs or constraints?

**Residual and emerging risks**

Identify risks that remain unresolved and explain how they may affect future engineering activities and project feasibility.

**Connections with planning and quality**

Explain how risks influence priorities, technical decisions, resource allocation, testing activities, and scheduling.

Consider the distinction between a risk and an issue.

A risk concerns an uncertain event or condition that may affect the project. An issue is a problem that has already occurred and requires management.

Example — Risk versus issue

For example, uncertainty about obtaining access to a required dataset is a risk. Discovering that the dataset is unavailable is an issue that may trigger corrective actions and the reassessment of other risks.

A useful risk-management process must be capable of handling both.

### 3.6. Engineering Process Effectiveness — Evaluating How the Team Works

During the first review, your team justified its selected lifecycle, engineering practices, development environment, and organizational approach.

You now have operational experience with those choices.

The second Expert Review examines whether they are functioning as intended.

Your analysis should consider:

**Lifecycle implementation**

Has the team actually followed the lifecycle it selected? If not, what changed, why, and with what consequences?

**Engineering practices**

Which activities and practices have proved effective? Which have created difficulties, unnecessary work, or coordination problems?

**Team organization**

How have roles, responsibilities, workload distribution, communication, and decision-making evolved?

**Development tools**

Do the selected tools support the intended processes? Have they introduced limitations or required adaptations?

**Resource efficiency**

How are time, effort, expertise, infrastructure, and other resources being consumed compared with expectations?

**Learning and improvement**

What has the team learned about its own approach, and which changes are necessary to improve subsequent work?

Do not evaluate a process merely by whether it resembles a recognized methodology.

Example — Methodology labels are not evidence

For example, holding daily meetings does not demonstrate that Scrum is effective, and completing iterations does not automatically establish that iterative development is appropriate.

Evaluate the observable effects of your practices: the problems they help detect, the coordination they enable, the uncertainty they reduce, and the consequences they produce for your project.

Evaluate process effectiveness

**The objective is to determine whether your engineering process remains appropriate for the problem, rather than preserving the original process simply because it was initially selected.**

## The Progress Report 02 — Analyzing the Project Trajectory

The Team Progress Report is a continuing engineering document. For this second milestone, your report should extend the information established during Expert Review 01 and analyze how the project has evolved since that reference point.

Its purpose is to help your team understand the relationship between its initial expectations, the work actually performed, the results obtained, and the decisions required to continue.

The report should make the evolution of the project inspectable and traceable.

### Suggested Report Structure

The following structure is proposed to organize your analysis. Adapt it to your project's lifecycle, circumstances, and documentation strategy.

| Section | Suggested content |
|----|----|
| 1\. Executive Summary | Overall project status, principal deviations, significant findings, corrective decisions and immediate priorities |
| 2\. Development Progress | Objectives achieved or missed, activities performed, engineering artifacts, technical results and supporting evidence |
| 3\. Planning Drift Analysis | Comparison with the previous baseline, deviation magnitude, causal analysis and consequences |
| 4\. Corrective Actions & Revised Strategy | Alternatives considered, corrective decisions, justifications, revised priorities and updated schedule |
| 5\. Quality Management | Quality criteria, assurance activities, verification and validation results, detected weaknesses and quality-plan adjustments |
| 6\. Risk Management | Evolution of identified risks, emerging risks, mitigation activities, materialized issues and residual exposure |
| 7\. Engineering Process & Team | Lifecycle effectiveness, organization, coordination, resource consumption, tools, and improvements |
| 8\. Lessons Learned & Next Steps | Major successes, challenges, findings, unresolved questions and priorities before the next milestone |
| 9\. Supporting Artifacts | References to documentation, repositories, measurements, testing evidence, planning records and other relevant materials |

This structure is indicative rather than mandatory.

Your report should accurately represent the project's evolution and allow a reviewer to follow the reasoning that connects observations, decisions, and their consequences.

### The Plan–Progress–Problems Perspective

A useful way to structure your report is to distinguish three complementary questions.

| Plan                | Progress                | Problems                       |
|---------------------|-------------------------|--------------------------------|
| What did we expect? | What actually happened? | What explains the differences? |

**Evidence → Analysis → Decisions → Revised Plan**

Use quantitative indicators where meaningful, but do not manufacture metrics merely to give an impression of precision. Qualitative evidence may also be appropriate when its origin, relevance, and interpretation are explicit.

The report should help you identify which assumptions remain defensible and which must be revised.

### What Makes a Useful Progress Report?

Weak reporting

> We completed most of our tasks, but some features are late. We had communication problems, so we will organize more meetings. Testing is ongoing and risks are under control.

This provides general claims without verifiable evidence, causal explanation, or a way to evaluate the proposed corrective actions.

Stronger reporting

> By the end of the second iteration, four of the six planned integration scenarios had been verified. Two remained blocked by inconsistent test data from an external service. Our initial planning did not account for this dependency. We introduced a controlled test dataset, assigned responsibility for integration validation, and moved one non-critical interface improvement to the next iteration. The revised plan includes explicit integration-readiness criteria.

This connects expectations, observations, causes, corrective decisions, and future verification criteria.

## Supporting Artifacts — Evidence of Engineering Progress

The Progress Report provides the overall analysis. Supporting artifacts allow the teaching team to examine particular elements of the project's implementation, monitoring, and adaptation.

Your team decides which artifacts are relevant for the expertise requested.

Examples include:

| Artifact | Possible subject of expert scrutiny |
|----|----|
| Updated Project Plan | Changes in objectives, priorities, milestones and resources |
| Schedule or Task Tracking | Planned versus actual progress, dependencies and effort |
| Software Requirements Specification | Requirement changes, traceability, inconsistencies and unresolved needs |
| Software Design or Architecture | Technical decisions, implementation feasibility, trade-offs and architectural evolution |
| Source Code Repository | Development progress, version-control practices, integration history and reviews |
| Quality Plan | Quality objectives, control mechanisms and assurance practices |
| Test Plan & Results | Test strategy, coverage, execution results, defects and interpretation |
| Risk Register or Risk Plan | Risk evolution, mitigation, emerging threats and residual risks |
| Resource or Cost Tracking | Planned versus actual consumption, allocation and constraints |
| Decision Records or Meeting Minutes | Decision-making, coordination, alternatives and justification |
| Experiments or Technical Demonstrations | Results, technical feasibility, validated assumptions and unresolved limitations |

These are examples, not mandatory deliverables.

Include artifacts that have genuinely been produced through the team's engineering activities. You are not expected to manufacture documentation solely for the review.

However, if your team has chosen not to produce a particular conventional artifact, you should still be capable of explaining how the associated engineering responsibilities are fulfilled.

### Preparing Artifacts for Review

Identify the artifacts you want examined and indicate which aspects would benefit from expert feedback.

For instance, you may request an examination of your updated development plan because of persistent scheduling deviations, of your risk-management approach because an important dependency has materialized, or of your testing strategy because quality results do not match expectations.

Make the relevant documents, repositories, diagrams, measurements, or demonstrations accessible and clearly reference them from the Progress Report.

## How to Request an Expert Review

Your team may obtain expert feedback through two channels.

### Option A — Brightspace Submission (Recommended)

Submit the current version of your Team Progress Report together with the supporting artifacts selected for review.

Identify the questions, deviations, decisions, or technical concerns you would like the teaching team to examine.

Include references to the previous baseline and relevant evidence where necessary to make the project's evolution understandable.

### Option B — Meeting with the Teaching Team

Request a meeting with the professor or teaching assistants to examine your project's progress and engineering decisions.

Prepare the current Progress Report and the supporting material relevant to the discussion.

Your team should be ready to explain what has changed since the previous milestone, present evidence, discuss the causes of significant deviations, and justify proposed corrective actions.

A meeting may focus on project management, engineering processes, software artifacts, quality, risks, or any other issue requiring expertise.

### Requesting Additional Expertise

You may request additional expert consultations when uncertainties, technical difficulties, or important decisions would benefit from external scrutiny.

Seeking feedback is part of autonomous engineering practice. Your team remains responsible for recognizing when expertise is needed and for deciding how to use it.

## Expert Feedback & Follow-up

The teaching team provides external expertise, critical questions, and alternative perspectives. It does not assume responsibility for managing the project or deciding which corrective actions your team must implement.

During the second review, feedback may concern the interpretation of deviations, the adequacy of corrective measures, the effectiveness of quality controls, the management of risks, or the suitability of the development process.

After receiving feedback, your team should:

1.  Identify the observations and concerns raised during the review.
2.  Determine which assumptions, decisions, or analyses require further investigation.
3.  Evaluate possible responses and their consequences.
4.  Decide which corrections or changes should be implemented.
5.  Update the relevant plans, engineering artifacts, and monitoring mechanisms.
6.  Preserve the reasoning behind significant decisions so that their effects can be examined later.

Recommendations should be evaluated critically rather than followed automatically.

You should be able to explain why the team accepted, adapted, or rejected important suggestions and what evidence informed those decisions.

The revised planning and corrective actions established after this review will provide the reference for Expert Review 03.

## Individual Reflection & Evidence of Competence

Alongside the Team Progress Report, each student produces an Individual Reflective Report as specified in the SPLASH project instructions.

The two documents serve complementary purposes.

The Team Progress Report examines the collective project trajectory, the effectiveness of the engineering process, and the decisions made to manage development.

The Individual Reflective Report examines each student's reasoning, contribution to decisions, assumptions, observations, challenges, and learning.

For this second milestone, individual reflection may address questions such as:

- What expectations did I hold about the activities or decisions in which I participated?
- What actually happened, and what evidence challenged my expectations?
- How did I contribute to identifying or analyzing a deviation?
- Which alternatives did I consider when responding to a difficulty?
- How did I evaluate the consequences of my decisions?
- What did I learn about the engineering process, collaboration, technical constraints, or my own reasoning?
- How will that learning influence my subsequent actions?

The Individual Reflective Report should not be a personal activity log or a repetition of the Team Progress Report.

Its purpose is to make engineering judgment, critical thinking, professional autonomy, and learning observable through concrete experiences and evidence.

## Assessment & Formative Purpose

This expert review does not contribute a direct percentage to the final project grade. Its purpose is to provide formative feedback and support the development and demonstration of engineering competencies.

Evidence made observable through the review may contribute to the **Competency Floor** described in the SPLASH project overview.

The teaching team will examine the quality of your progress analysis, the evidence supporting your conclusions, your ability to identify and explain deviations, and the coherence of your engineering decisions.

The objective is not to reward the amount of code produced, the number of tasks completed, or the team's ability to appear on schedule.

What a strong second review demonstrates

**A strong second review demonstrates that your team understands how its project has evolved, can explain the causes and consequences of deviations, and is capable of adapting its engineering approach through informed decisions.**

## Practical Advice — Preparing for Your Second Review

Treat this review as an opportunity to examine the real consequences of your engineering approach, including its limitations and unexpected effects.

Be transparent about delays, technical difficulties, unsuccessful decisions, coordination problems, or unmet expectations. Concealing these elements prevents the team from identifying opportunities for improvement.

Avoid general claims such as *“we are on track,” “testing is going well,”* or *“we have managed the risks.”* Explain what these statements mean, which observations support them, and what criteria you use to judge the situation.

Distinguish symptoms from causes. A missed deadline may be the visible consequence of an earlier estimation problem, an unresolved dependency, or an ineffective decision-making process.

Use appropriate representations to communicate progress and deviations. A comparison table, annotated timeline, issue history, risk matrix, or test-results summary may make a complex situation easier to understand than several pages of general commentary.

Do not interpret every deviation negatively. Changes may reflect better knowledge, more appropriate decisions, or a justified evolution of your project. Explain their significance instead of classifying them automatically as successes or failures.

Finally, remember that an engineering process is valuable because of what it helps you achieve and control—not because it follows a fashionable methodology.

**Use this review to convert your experience into knowledge, your observations into decisions, and your corrective actions into a defensible trajectory for the remainder of SPLASH.**
