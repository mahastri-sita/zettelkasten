// graphify OpenCode plugin
// Injects a knowledge graph reminder before shell tool calls when the graph exists.
//
// IMPORTANT: keep the reminder string free of backticks and $(...) constructs.
// The hook prepends `echo "<reminder>" ; <cmd>` to the user's shell command;
// backticks inside the double-quoted echo trigger bash command substitution,
// which both corrupts tool output and silently executes the very graphify
// command we are only suggesting. Plain words render fine in opencode's TUI.
import { existsSync } from "node:fs";
import { join } from "node:path";

const REMINDER =
  "[graphify] knowledge graph at graphify-out/. For focused questions, run graphify query with your question (scoped subgraph, usually much smaller than GRAPH_REPORT.md) instead of grepping raw files. Read GRAPH_REPORT.md only for broad architecture context.";

export const GraphifyPlugin = async ({ directory }) => {
  let reminded = false;

  return {
    "tool.execute.before": async (input, output) => {
      if (reminded || (input.tool !== "bash" && input.tool !== "shell")) return;
      if (!existsSync(join(directory, "graphify-out", "graph.json"))) return;
      if (!output.args || typeof output.args !== "object") return;
      if (typeof output.args.command !== "string" || !output.args.command) return;

      // ';' not '&&' - Windows PowerShell 5.1 rejects '&&' as a statement
      // separator, breaking the first bash command of the session (#1646).
      output.args.command = `echo "${REMINDER}" ; ${output.args.command}`;
      reminded = true;
    },
  };
};
