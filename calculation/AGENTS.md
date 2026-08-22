# AGENTS.md

## Scope

These rules apply to `calculation/`. Inherit the root `AGENTS.md`.

A Calculation is a reusable method that transforms data into information. It is not an interpretation, ideology, topic index, or project narrative.

## Authority

- Do not create or materially change a Calculation object without explicit instruction or approval.
- Existing Calculation objects may be read and evaluated when relevant.
- Run an existing procedure only when it is relevant to the user's request and its inputs and side effects are understood.

## Required Documentation

The primary object is a Markdown method document. It must make the following intelligible, using headings appropriate to the method:

- purpose and information produced;
- input data and provenance;
- assumptions and scope conditions;
- method, formula, or model specification;
- procedure or code needed for reproduction;
- output definition;
- validation or diagnostic checks; and
- limitations and known failure modes.

Scripts may accompany the method when needed and explicitly authorized. Do not turn this folder into a complete computational workspace: avoid raw-data duplication, temporary files, caches, and generated intermediates unless the user specifically requests them.

## Integrity

- Never modify raw data in `source/dataset`.
- Record transformations rather than obscuring them.
- Distinguish a calculated result from its substantive interpretation; interpretation belongs primarily in Argument.
- Do not claim validation that was not run.
- Expose sensitivity to scale, spatial unit, period, parameter choice, and missing data when material.

## Naming

Name the object after the reusable calculation or method, such as `Accessibility Calculation` or `Employment Center Identification`. Prefer project-agnostic names when the procedure is reusable.
