## Context & Purpose

Your team is now approaching the final stage of its SPLASH project. During the first Expert Review, you examined the foundations of your engineering approach. During the second, you analyzed actual development progress, identified deviations, evaluated the effectiveness of your processes, and established corrective actions.

The third Expert Review examines how your project has evolved since the previous milestone and whether your team is prepared to bring its engineering work to a defensible conclusion.

At this stage, the focus progressively shifts from establishing and adapting the development process toward consolidating the software intervention, evaluating its quality and impact, resolving significant uncertainties, and preparing for project closure.

This does not mean that development is expected to be complete. Important activities may remain, and your investigation may still reveal unexpected findings.

The objective is to establish a realistic understanding of your project's current state, determine what remains necessary to achieve its intended outcomes, and evaluate whether the remaining work can be completed within the available resources and constraints.

The teaching team will examine the evidence you provide, challenge your assessment of project readiness, identify overlooked dependencies or risks, and discuss possible strategies for completing the project.

Formative engineering consultation — not an approval gate

**This review is a formative engineering consultation, not an approval gate.** Your team remains responsible for deciding how to conclude its project, what claims it can legitimately make, and what evidence is necessary to support those claims.

## Review Objectives

The third review focuses on six complementary dimensions.

| Dimension | Central question |
|----|----|
| Progress Since Review 02 | What has changed since the previous milestone, and what evidence demonstrates that evolution? |
| Planning Drift & Corrective Action Effectiveness | How does actual progress compare with the revised baseline, and have previous adjustments produced their intended effects? |
| Engineering & Product Maturity | How mature, coherent, integrated, and operational is the software intervention? |
| Quality & Residual Risk | What has been verified, what remains uncertain, and which problems or risks could compromise completion? |
| Impact Evidence & Validation Readiness | What evidence demonstrates, or will be needed to demonstrate, that the intervention addresses the real problem? |
| Project Closure & Final Defense Preparation | What remains to be done, how will the team complete it, and what engineering argument will support the final defense? |

These dimensions are interconnected.

A technically complete implementation may still require integration, validation, or evidence of its actual effect. Similarly, a project may have achieved meaningful results while retaining unresolved quality problems or significant operational dependencies.

The purpose is not to create an optimistic account of the final stage, but to establish **what has been achieved, what can be demonstrated, what remains unresolved, and which decisions are necessary to bring the project to a coherent conclusion** .

## What the Expert Review Will Examine

### 3.1. Progress Since Review 02 — Evaluating the Latest Project Evolution

The previous Expert Review established a revised understanding of the project, including updated objectives, priorities, planning assumptions, corrective actions, and risk-management decisions.

Your team must now examine what actually happened after those decisions were made.

Your review should address:

- Which objectives established or revised during Review 02 have been achieved, partially achieved, postponed, changed, or abandoned?
- What significant engineering activities have been completed since the previous milestone?
- What software components, integrations, tests, experiments, documentation, or other artifacts have evolved?
- What evidence demonstrates the reported results?
- What unexpected findings, difficulties, or opportunities emerged?
- How has the team's understanding of the problem or proposed intervention changed?
- What remains incomplete, and what are the consequences for project completion?

Distinguish the state of the project from the activities undertaken to reach that state.

For example, completing the implementation of several components does not necessarily demonstrate that the intended system is operational. The components may remain unintegrated, insufficiently validated, or dependent on unavailable infrastructure.

Likewise, an investigation that leads the team to reject an initially planned feature may represent valuable progress if it prevents an ineffective intervention or improves the coherence of the final solution.

**Engineering progress should be interpreted through the results achieved, the uncertainties resolved, and the contribution made toward the project's intended outcomes.**

### 3.2. Planning Drift & Corrective Action Effectiveness — Evaluating the Revised Trajectory

During Review 02, your team examined deviations and established corrective actions or adaptations.

The third review must evaluate the consequences of those decisions.

Your analysis should address the following.

**Reference baseline**

Identify the revised objectives, milestones, schedule, scope, responsibilities, and resource assumptions established after the previous milestone.

**Observed deviations**

Compare the actual state of the project with those revised expectations. Identify differences concerning progress, effort, resources, costs, dependencies, technical results, or scope.

**Corrective action outcomes**

Examine the actions undertaken following Review 02. Which were implemented? What effects were expected? What effects were actually observed?

**Effectiveness and unintended consequences**

Determine whether the selected actions addressed the original difficulties, reduced uncertainty, improved quality, or created new constraints and risks.

**Remaining feasibility**

Assess whether the remaining objectives are achievable with the time, resources, expertise, and technical capabilities available.

**Final adjustments**

Identify any further changes required and justify their consequences for the project and its intended outcomes.

Do not assume that corrective actions were successful simply because they were implemented.

For example, reorganizing the team's workload may have reduced coordination delays while leaving an unresolved architectural dependency that still threatens integration.

Similarly, reducing the scope may improve feasibility while requiring a reassessment of whether the remaining intervention can still address the problem to the intended degree.

Engineering principle

**Schedule performance and engineering progress remain distinct.** The objective is to determine whether the revised trajectory has improved the project's ability to achieve meaningful, demonstrable results.

Weak analysis

> We implemented the corrections from the previous review and are now almost finished. Some tasks remain, but we expect to complete everything before the final presentation.

*This gives no evidence that the corrective actions worked, no assessment of the remaining work, and no justification for the confidence expressed.*

Stronger analysis

> Following Review 02, we introduced integration checks at the end of each iteration. Three previously recurring interface failures were detected earlier and resolved before the latest release. However, end-to-end validation remains incomplete because the external service is not consistently available. We have therefore revised our final activities to prioritize operational validation over two lower-priority enhancements and defined the minimum conditions required to support our final claims.

*This evaluates the effects of earlier decisions, identifies a remaining limitation, and connects the final adjustment to explicit project objectives.*

Your report should preserve the history of previous baselines and decisions. Do not retrospectively alter earlier expectations to conceal deviations or make corrective actions appear more successful than the evidence supports.

### 3.3. Engineering & Product Maturity — Evaluating the Intervention as a System

As the project approaches completion, your team must assess the maturity of its engineering work and the operational state of the software intervention.

This examination should consider not only individual components, but also their relationships, dependencies, integration, and behaviour within the larger system.

**Architecture and design coherence**

Explain how the current architecture supports the intended intervention. Identify significant design changes, unresolved inconsistencies, technical compromises, and remaining architectural limitations.

**Implementation and integration**

Describe which components are implemented, integrated, and operational. Identify dependencies between subsystems and any functionality that remains incomplete or unverified.

**Requirements and traceability**

Examine the relationship between the problem, stakeholder needs, defined requirements, engineering decisions, implementation, and available verification evidence.

**Technical debt and trade-offs**

Identify compromises made during development, their rationale, and their potential consequences for quality, maintainability, reliability, or future evolution.

**Operational conditions**

Determine whether the intervention can operate under the actual conditions relevant to the problem, including data, infrastructure, external services, stakeholder interactions, and other necessary dependencies.

**Engineering documentation**

Evaluate whether the project's documents, models, repositories, and decision records accurately represent the system and support its use, evaluation, and future development.

A collection of implemented features is not necessarily a functioning software intervention.

The relevant question is whether the system, within its declared scope, can operate coherently and perform the functions required to support the team's engineering claims.

In SPLASH, the final working release must be operationally complete within the scope claimed by the team.

A narrow but complete intervention can therefore be more defensible than a larger implementation whose essential dependencies or behaviours remain hypothetical.

### 3.4. Quality & Residual Risk — Establishing What Can Be Trusted

During Review 02, your team examined the implementation and effectiveness of its quality- and risk-management processes.

The third review concentrates on the results of those processes and the uncertainties that remain before project closure.

**Quality criteria and evidence**

Revisit the qualities and acceptance criteria established for your project. Explain what has been verified or validated, what evidence is available, and which criteria remain unmet or unexamined.

**Verification and validation results**

Present the outcomes of testing, reviews, inspections, experiments, stakeholder evaluations, or other relevant verification and validation activities.

**Defects and unresolved issues**

Identify significant defects, quality weaknesses, inconsistencies, and technical limitations. Evaluate their severity and consequences for the intended intervention.

**Residual risks**

Identify risks that remain relevant to the final project activities, including risks associated with deployment, integration, resource availability, stakeholder access, data, security, and operational dependencies.

**Risk and quality trade-offs**

Explain decisions to correct, mitigate, accept, defer, or eliminate particular problems through changes of scope or technical approach.

**Closure conditions**

Determine which quality and risk conditions must be satisfied before the team can reasonably claim that the intervention is ready for its intended use or final demonstration.

Be careful not to confuse the absence of detected defects with evidence of quality.

A test suite that reports no failures may still leave important behaviours, operational conditions, or stakeholder needs unexamined.

Similarly, closing an issue in a project-management tool does not establish that the underlying problem has been resolved unless appropriate evidence supports that conclusion.

Engineering principle

**Your assessment should distinguish what has been demonstrated, what remains uncertain, and what the team has consciously decided to accept within the declared scope.**

### 3.5. Impact Evidence & Validation Readiness — Demonstrating That the Intervention Matters

SPLASH requires more than the production of functioning software.

Your project must demonstrate that its intervention addresses a real, documented problem and produces an observable effect in the intended context.

The third Expert Review should examine your readiness to support that demonstration.

**Problem and success criteria**

Revisit the operational definition of the problem, the intended change, and the criteria or thresholds established for judging whether the intervention succeeds.

**Baseline and comparison**

Identify the observations or measurements that characterize the problem before the intervention and the comparisons required to evaluate its effect.

**Evidence collected**

Present results already obtained from experiments, operational use, stakeholder interactions, measurements, or other relevant observations.

**Validation strategy**

Explain how the team intends to demonstrate that the intervention affects the problem rather than merely producing functioning software.

**Remaining evidence gaps**

Identify missing observations, unavailable data, insufficient experiments, or unresolved dependencies that could limit the conclusions you will be able to defend.

**Impact and limitations**

Explain what your current evidence supports about the intervention's effectiveness and what remains necessary to demonstrate the intended impact.

For example, demonstrating that an automated processing system completes a task in two seconds is evidence of its operational performance.

Demonstrating that this performance removes or reduces the original problem requires connecting that result to the actual operational context, affected stakeholders, baseline conditions, and defined success criteria.

The final defense must distinguish between **the product working as designed** and **the intervention achieving its intended effect** .

Your team should identify what evidence is necessary for each claim and ensure that the remaining project activities prioritize collecting that evidence.

### 3.6. Project Closure & Final Defense Preparation — Planning a Defensible Conclusion

The third Expert Review should help your team determine how to complete the project, consolidate its results, and prepare for the Final Defense.

Project closure is not simply the end of development activities or the arrival of a deadline.

It involves establishing what has been accomplished, verifying the results, documenting significant decisions and limitations, resolving or managing outstanding issues, and preparing the evidence needed to support the project's conclusions.

Your review should examine:

**Remaining engineering activities**

Identify the work still required to complete, integrate, validate, document, and demonstrate the intervention.

**Prioritization and feasibility**

Distinguish essential activities from desirable improvements. Explain how priorities have been selected in relation to the remaining resources, risks, and project objectives.

**Final verification and validation**

Define which checks, experiments, evaluations, or stakeholder interactions must be completed before the Final Defense.

**Working release preparation**

Explain how the team will establish and demonstrate a stable, operationally complete release within the declared scope.

**Documentation and traceability**

Identify the records, specifications, models, test results, measurements, and decision histories required to make the engineering work understandable and inspectable.

**Unresolved issues and limitations**

Explain how remaining limitations will be addressed and how they affect the claims the team can legitimately make.

**Final Defense preparation**

Describe how the team intends to connect the problem, investigation, engineering decisions, software intervention, quality evidence, observed outcomes, and impact into a coherent engineering argument.

The Final Defense is not a product pitch.

The team must demonstrate not only what it has built, but also why the intervention is appropriate, how it was engineered, what evidence supports its quality, and whether it achieved the intended effect.

Engineering principle

**The objective of closure preparation is to ensure that the project's conclusions follow from the work actually performed and the evidence actually collected—not from promises about what the system might achieve later.**

## The Progress Report 03 — Assessing Project Closure Readiness

The Team Progress Report is a continuing engineering document. For this third milestone, your report should extend the analysis established during previous reviews and examine how the project has evolved toward its intended conclusion.

The primary objective is to determine whether the project is progressing toward an operationally complete, adequately validated, and evidence-supported intervention.

Your report should make the remaining engineering work visible, evaluate the effectiveness of previous decisions, and establish a defensible strategy for project completion.

It should also provide a foundation for the Final Defense by connecting engineering intentions, actual decisions, technical results, and observable outcomes.

### Suggested Report Structure

The following structure is proposed to organize your analysis. You may adapt it to your project, lifecycle, engineering approach, and documentation strategy.

| Section | Suggested content |
|----|----|
| 1\. Executive Summary | Current project status, principal achievements, significant limitations, closure readiness and final priorities |
| 2\. Progress Since Review 02 | Activities completed, outcomes achieved, project changes, technical results and supporting evidence |
| 3\. Planning Drift & Corrective Actions | Comparison with the revised baseline, effectiveness of previous corrective decisions, remaining deviations and final adjustments |
| 4\. Engineering & Product Maturity | Architecture, implementation, integration, requirements traceability, technical debt and operational readiness |
| 5\. Quality & Residual Risk | Verification and validation results, quality criteria, unresolved defects, residual risks and acceptance decisions |
| 6\. Impact Evidence | Problem baseline, success criteria, experiments, operational observations, preliminary results and remaining evidence gaps |
| 7\. Closure Strategy | Remaining activities, final milestones, resource allocation, priorities, dependencies and completion conditions |
| 8\. Final Defense Readiness | Working release, demonstration strategy, supporting engineering evidence, documentation and defensible conclusions |
| 9\. Lessons Learned & Supporting Artifacts | Significant findings, process evolution, engineering lessons and references to relevant documentation and evidence |

This structure is indicative rather than mandatory.

Your report should focus on the information necessary to understand the project's current condition and determine what must happen before it can be concluded.

Do not reproduce all previous reports. Refer to earlier decisions, baselines, or evidence when they are necessary to explain the current state.

### From Progress Monitoring to Closure Readiness

The third report should connect four complementary questions.

| Dimension     | Guiding question                     |
|---------------|--------------------------------------|
| **Evolution** | What changed since the last review?  |
| **Readiness** | What is operational and validated?   |
| **Evidence**  | What conclusions can we demonstrate? |
| **Closure**   | What remains necessary to conclude?  |

A project may be nearly complete in terms of implemented functionality while remaining far from completion in terms of validation, operational integration, or impact evidence.

Conversely, a project may have a deliberately limited software scope but be approaching a defensible conclusion because its intervention is operational, its engineering choices are traceable, and its effects have been observed.

Your report should make those distinctions explicit.

### What Makes a Useful Closure Readiness Assessment?

Weak reporting

> Our project is approximately 90% complete. Most features are implemented, and we are confident that everything will be ready for the final presentation. We only need to finish testing and documentation.

*This provides an unsupported completion estimate and treats testing and documentation as minor residual tasks without examining their scope, dependencies, or potential consequences.*

Stronger reporting

> All five components required for the declared release scope have been implemented, and four have passed their integration tests. The remaining component depends on an external service whose behaviour differs from our initial assumptions. The current release supports six of the eight operational scenarios defined in our validation plan. We have prioritized resolution of the integration dependency and the two outstanding scenarios over additional features. We will evaluate closure readiness against the established acceptance criteria rather than an estimated percentage of completion.

*This distinguishes implementation, integration, validation, remaining dependencies, and completion criteria. It supports a realistic decision about the final project trajectory.*

### Suggestions for Evidence-Based Closure Reporting

- Be factual, specific, and transparent about both accomplishments and unresolved difficulties. An optimistic statement about readiness is not a substitute for evidence.
- Compare actual results with the latest project baseline while preserving the history of previous plans and decisions.
- Evaluate whether earlier corrective actions produced the intended consequences, including any unexpected effects.
- Distinguish implemented functionality, integrated functionality, validated behaviour, operational readiness, and demonstrated impact.
- Identify the remaining work precisely. Explain its importance, dependencies, resource requirements, risks, and expected outcomes.
- Use appropriate representations such as readiness matrices, test summaries, milestone comparisons, architecture diagrams, risk registers, and direct links to evidence.
- Do not present future intentions as completed results. Make clear what has already been demonstrated and what remains to be established.
- Use the review to challenge the team's assumptions about readiness, not to construct an idealized narrative of successful completion.

## Supporting Artifacts — Evidence of Engineering Maturity and Readiness

The Progress Report provides an overall assessment of the project's trajectory and readiness for closure.

Supporting artifacts allow the teaching team to examine particular elements of the engineering work and evaluate whether the team's conclusions are supported by evidence.

Your team decides which artifacts are relevant and which aspects would benefit from expert scrutiny.

Examples include:

| Artifact | Possible subject of expert scrutiny |
|----|----|
| Updated Project Plan | Final milestones, remaining dependencies, priorities and resource allocation |
| Requirements Specification | Requirement coverage, changes, consistency and traceability to implemented functionality |
| Software Design or Architecture | Architectural coherence, integration, technical compromises and remaining limitations |
| Source Code Repository | Implementation status, integration history, release configuration and engineering practices |
| Integration Records | Interfaces, dependencies, integration results and unresolved interoperability problems |
| Quality Plan & Results | Quality criteria, assurance activities, verification evidence and outstanding quality concerns |
| Test Plan & Test Reports | Test execution, coverage, observed failures, validation results and remaining test activities |
| Risk Register or Risk Plan | Residual risks, mitigation effectiveness, materialized issues and closure risks |
| Operational Demonstration | Functioning software, real operating conditions, required services and dependencies |
| Experiments & Impact Measurements | Baseline comparisons, observed effects, validation findings and limitations |
| Technical Documentation | System description, operational instructions, decision history and evidence traceability |
| Final Defense Preparation | Demonstration strategy, key engineering claims, supporting evidence and identified gaps |

These examples do not constitute a mandatory list of deliverables.

Your team should provide artifacts that genuinely exist and support meaningful engineering activities or conclusions.

An incomplete artifact may still be appropriate for expert review when it exposes an important uncertainty or decision that requires examination.

### Preparing Artifacts for Expert Review

Identify the artifacts you want examined and explain why they are relevant to the project's completion.

For example, your team may request an architectural review because integration issues remain unresolved, an examination of its validation strategy because the intended impact is difficult to measure, or an assessment of its final plan because important dependencies threaten completion.

Provide direct access to the selected material and identify the specific questions or engineering concerns on which you would like feedback.

The objective is not to impress the reviewer with the quantity of documentation but to enable meaningful scrutiny of the project's actual state.

## How to Request an Expert Review

Your team may obtain expert feedback through two channels.

### Option A — Brightspace Submission (Recommended)

Submit the current version of your Team Progress Report together with the supporting artifacts selected for review.

Identify the aspects of the project on which you would like expertise, particularly unresolved engineering decisions, concerns about quality or operational readiness, difficulties in collecting impact evidence, or uncertainties about project closure.

Make relevant evidence and previous decisions accessible so that the teaching team can understand your current conclusions and their foundations.

### Option B — Meeting with the Teaching Team

Request a meeting with the professor or teaching assistants to discuss the current state of your project and the remaining engineering challenges.

Prepare the Progress Report and relevant documentation, technical artifacts, test results, demonstrations, or measurements.

Your team should be ready to explain its assessment of project readiness, justify its final priorities, demonstrate available results, and discuss unresolved limitations or risks.

The meeting may involve examining the working release, evaluating evidence, discussing the closure strategy, or questioning the coherence of the argument being prepared for the Final Defense.

### Requesting Additional Expertise

Your team may request further consultations whenever additional feedback would help resolve an important technical, methodological, or organizational issue.

The responsibility for identifying when expertise is needed remains with your team.

## Expert Feedback & Follow-up

The teaching team provides an external perspective on your project's readiness and engineering reasoning.

It may identify inconsistencies between your claims and supporting evidence, challenge optimistic estimates, highlight unexamined operational dependencies, or suggest alternative strategies for resolving remaining difficulties.

The teaching team does not certify that the project is complete, approve the working release, or assume responsibility for the final engineering decisions.

Following the review, your team should:

1.  Identify the principal observations, concerns, and questions raised.
2.  Evaluate their implications for quality, operational readiness, impact evidence, and project closure.
3.  Determine whether additional investigation, verification, validation, or development activities are required.
4.  Reassess the final priorities, available resources, and remaining risks.
5.  Decide which recommendations to implement, adapt, or reject, and justify those decisions.
6.  Update the relevant engineering artifacts, closure strategy, and Final Defense preparation.

Expert feedback may reveal that some planned activities are no longer necessary, while others require more attention than initially expected.

It may also challenge the scope of the conclusions the team intends to defend.

Engineering principle

**The purpose is not to obtain confirmation that the project is ready, but to improve the team's ability to determine and justify its actual readiness.**

## Individual Reflection & Evidence of Competence

Alongside the Team Progress Report, each student produces an Individual Reflective Report as specified in the SPLASH project instructions.

The two documents address complementary dimensions of the engineering experience.

The Team Progress Report describes the collective state and evolution of the project, the results of engineering activities, the remaining challenges, and the strategy for project completion.

The Individual Reflective Report makes each student's engineering reasoning, decisions, learning, and professional development observable.

For this third milestone, individual reflection may consider:

- How has my understanding of the problem and the engineering intervention evolved since the previous reviews?
- Which initial assumptions or decisions have been confirmed, modified, or rejected through evidence?
- How did I contribute to evaluating technical maturity, quality, risks, or operational readiness?
- What significant engineering trade-offs did I encounter, and how did I reason through them?
- What did I learn from the consequences of earlier corrective actions?
- How have my working practices, collaboration, and engineering judgment evolved?
- Which competencies can I now demonstrate through concrete actions, results, and evidence?
- What important limitations or questions remain in my own understanding?

Individual reflection should not be limited to describing completed tasks or expressing satisfaction with the final product.

For example, identifying why an architectural assumption failed, how that failure was investigated, and how the resulting knowledge influenced later decisions provides stronger evidence of engineering learning than simply reporting that a component was completed.

The purpose is to demonstrate **how experience and evidence have transformed your engineering reasoning** , not merely to summarize what you contributed.

## Assessment & Formative Purpose

This expert review does not contribute a direct percentage to the final project grade. Its purpose is to provide formative feedback and support the development and demonstration of engineering competencies.

Evidence made observable through the review may contribute to the Competency Floor described in the SPLASH project overview.

The teaching team will examine the quality of your project analysis, the relevance and credibility of your supporting evidence, your assessment of engineering maturity, and the coherence of your closure strategy.

The objective is not to reward the number of implemented features, the apparent percentage of completion, or the team's confidence that everything will be finished on time.

What a strong third review demonstrates

**A strong third review demonstrates that your team understands the actual state of its project, can distinguish achieved results from remaining uncertainties, and is capable of planning a defensible engineering conclusion supported by evidence.**

## Practical Advice — Preparing for Your Third Review

Treat this review as a professional examination of your project's readiness, not as a rehearsal for promoting your final product.

Be precise about what is complete, what has been verified, what remains uncertain, and what must still be accomplished.

Do not confuse implementation with operational readiness. A system can contain all its intended components while remaining unable to operate reliably under real conditions.

Likewise, do not confuse operational performance with impact. A technically functioning system must still be evaluated against the actual problem and the success criteria established for the intervention.

When identifying remaining work, explain why each activity matters and what conditions determine its completion. General statements such as *“we only need testing”* or *“the final integration should be straightforward”* are not useful without evidence and analysis.

Evaluate previous corrective actions through their actual consequences. An action that initially appeared appropriate may have produced unexpected difficulties or revealed additional uncertainties.

Be explicit about technical debt, limitations, unresolved quality concerns, and residual risks. These elements are part of the engineering reality and should influence the team's final decisions.

Use concise and appropriate representations to communicate readiness: traceability matrices, validation results, risk summaries, milestone comparisons, architecture diagrams, and clearly referenced evidence may be more informative than lengthy descriptions.

Finally, examine whether the project's declared scope remains coherent with the intervention that can actually be demonstrated. When resources are insufficient to support all intended features or activities, prioritize the engineering work necessary to achieve and substantiate the project's essential outcomes.

**The third review should help your team move from managing development toward establishing an evidence-based conclusion: what problem you addressed, what intervention you engineered, what results you observed, what limitations remain, and what those results allow you to claim.**
