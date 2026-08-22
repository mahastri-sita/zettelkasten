# AGENTS.md

## Scope

This vault is a personal research operating system for urban planning and urban science. It is a research workspace, not a software repository. Do not run build, lint, typecheck, or test commands unless a specific calculation artifact explicitly requires them.

The system is framework-first, human-led, AI-active, evidence-checked, synthesis-preserving, and contradiction-aware. The user retains final intellectual authority.

## Language

- Research notes default to Bahasa Indonesia.
- Academic paper drafts default to English.
- Preserve the language of existing files unless the user asks for a change.

## Scoped Instructions

Before working in a folder, read the `AGENTS.md` files from the vault root through the target folder if they are not already in context. Apply rules in this order:

1. The user's current explicit instruction.
2. The most specific applicable folder instruction.
3. Parent-folder instructions.
4. Root defaults in this file.

Evidence integrity is non-negotiable: never fabricate evidence, provenance, quotations, locators, calculations, or source access. Always make material uncertainty visible.

If classification or authority is ambiguous, do not guess aggressively. Ask one concise question.

## Epistemic Architecture

```text
MY IDEA / BIG QUESTION
          |
          v
       ARGUMENT
          ^
          |
SOURCE + CALCULATION
          |
          v
 ARGUMENT TESTING
          |
          +----> SYNTHESIS PRODUCT
          |
          +----> OUTPUT ----> candidate synthesis

TOPIC NOTES index all layers.
CONTRADICTION JOURNEY records confirmed intellectual change.
```

Folder roles:

- `argument/argument`: personal thinking in motion and the main research kitchen.
- `argument/synthesis-product`: mature, defensible, reusable personal synthesis.
- `argument/contradiction-journey`: confirmed changes in intellectual position.
- `calculation`: reusable methods that transform data into information.
- `output`: drafts and final expressions of research work.
- `source`: external evidence, statements, observations, and datasets.
- `topic-notes`: AI-maintained semantic indexes and routers.

Do not add folders, taxonomies, lifecycle systems, status systems, tags, or metadata beyond rules explicitly defined in the applicable `AGENTS.md` files.

## Authority Matrix

AI may create and maintain files autonomously in:

- `source`
- `topic-notes`

AI requires an explicit instruction or approval before creating files in:

- `argument/argument`
- `argument/synthesis-product`
- `argument/contradiction-journey`
- `calculation`
- `output`

For existing files in `argument/argument`, `argument/synthesis-product`, and `output`, an explicit editing intent such as "edit", "revise", "update", or "write into this file" authorizes conservative editing. A request to analyze, research, critique, compare, or check does not authorize editing those files.

For `argument/contradiction-journey`, propose a change and obtain approval before writing it. For `argument/synthesis-product`, AI may nominate a candidate, but the user decides whether it is promoted and created.

## Research Behavior

- Begin from the user's question or framework rather than forcing a literature-first workflow.
- Test frameworks against evidence, counterevidence, alternative mechanisms, assumptions, and scope conditions.
- Distinguish source evidence, calculation results, user positions, AI inference, and speculation.
- Surface evidence that weakens the user's position. Do not silently reconcile contradictions or rewrite the user's worldview.
- Trace important substantive claims to relevant Source or Calculation objects.
- Split a note only when the separated intellectual object has independent reuse value, not merely because a file is long.

## Targeted Context Retrieval

For a substantive task centered on an Argument, use this order:

1. Read the active Argument.
2. Read relevant portions of `argument/contradiction-journey/contradiction-journey.md` if it exists.
3. Follow direct links and relevant Topic Notes.
4. Read the Source and Calculation objects that support or challenge the claims.
5. Broaden the search only if material gaps remain.

Do not read the entire vault when targeted retrieval is sufficient. The Contradiction Journey is optional for small technical or administrative tasks.

## Linking

- Create wikilinks only for strong, semantically useful connections.
- Prefer a smaller number of meaningful links over a dense graph.
- Do not link every noun.
- In Topic Notes, annotate links with the reason for the relationship.
- Strip Obsidian wikilinks and tags before passing note content into skills or external agent workflows that do not understand Obsidian syntax.

## Completion

After a substantive research task, check whether an existing Topic Note needs maintenance or whether a new router is genuinely warranted. This is a relevance check, not a mandatory global update ritual.

Conclude substantive work with any important provenance limits, unresolved contradictions, unsupported inferences, or data limitations made visible.

## Anti-Patterns

- File proliferation without clear epistemic value.
- Atomic-note fragmentation by default.
- Direct promotion from Source to Synthesis Product.
- Unauthorized rewriting of personal intellectual work.
- Treating AI summaries as user-authored positions.
- Treating official or published material as automatically correct.
- Fabricating missing metadata or hiding limited source access.
- Autonomous creation of new taxonomy or workflow layers.
