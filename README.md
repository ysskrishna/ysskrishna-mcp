# ysskrishna MCP

[![Tests](https://github.com/ysskrishna/ysskrishna-mcp/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/ysskrishna/ysskrishna-mcp/actions/workflows/validate-skills.yml) [![License: MIT](https://img.shields.io/github/license/ysskrishna/ysskrishna-mcp)](https://github.com/ysskrishna/ysskrishna-mcp/blob/main/LICENSE) [![GitHub release](https://img.shields.io/github/v/release/ysskrishna/ysskrishna-mcp?label=release)](https://github.com/ysskrishna/ysskrishna-mcp/releases) [![npm version](https://img.shields.io/npm/v/@ysskrishna/ysskrishna-mcp)](https://www.npmjs.com/package/@ysskrishna/ysskrishna-mcp) [![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)

[![skills.sh](https://skills.sh/b/ysskrishna/ysskrishna-mcp)](https://skills.sh/ysskrishna/ysskrishna-mcp)

This repository ships one Agent Skill, [`connect-ysskrishna-mcp`](skills/connect-ysskrishna-mcp/SKILL.md), which helps an agent connect a client to the public read-only MCP server at `https://www.ysskrishna.space/mcp`. No API key is required. Do not send sensitive data to the remote server. Installing the skill does not add the MCP server.

On 2026-11-16 a POST initialize to that URL returned HTTP 200 with server name ysskrishna; a Codex tool call was not run and a Cursor UI session was not opened.

## Installation

Native installs for specific agents:

<a id="claude-code"></a>

<details>
<summary><b>Claude Code</b> — plugin marketplace install for the <code>ysskrishna-mcp</code> bundle.</summary>

```text
/plugin marketplace add ysskrishna/ysskrishna-mcp
/plugin install ysskrishna-mcp@ysskrishna-mcp
```

```bash
claude plugin marketplace add ysskrishna/ysskrishna-mcp
claude plugin install ysskrishna-mcp@ysskrishna-mcp
```

Connect the MCP server (after the skill is installed):

```bash
claude mcp list
claude mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp
```

Use the applicable documented `--scope` value for project or local scope. Check `/mcp` in a session for connection and tools.

More in [docs/claude-code-setup.md](docs/claude-code-setup.md).

</details>

<a id="codex-cli-and-app"></a>

<details>
<summary><b>Codex CLI and App</b> — Codex plugin marketplace install; needs Codex CLI v0.122 or later.</summary>

```bash
codex plugin marketplace add ysskrishna/ysskrishna-mcp
codex plugin add ysskrishna-mcp@ysskrishna-mcp
```

Start a new session afterwards. Update with `codex plugin marketplace upgrade ysskrishna-mcp`. Remove with `codex plugin remove ysskrishna-mcp@ysskrishna-mcp`.

Connect the MCP server (after the skill is installed):

```bash
codex mcp list
codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp
```

The installed Codex CLI accepts `codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp`; a throwaway `CODEX_HOME` add/list/get on 2026-11-16 stored transport `streamable_http` and left the real config unchanged.

More in [docs/codex-setup.md](docs/codex-setup.md).

</details>

<a id="gemini-cli"></a>

<details>
<summary><b>Gemini CLI</b> — extension or <code>gemini skills install</code> from this repo.</summary>

```bash
gemini extensions install https://github.com/ysskrishna/ysskrishna-mcp
```

```bash
gemini skills install https://github.com/ysskrishna/ysskrishna-mcp.git --path skills
```

Connect the MCP server (after the skill is installed):

```bash
gemini mcp list
gemini mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp
```

Use `--scope project` when requested. Check `/mcp` for tools.

More in [docs/gemini-cli-setup.md](docs/gemini-cli-setup.md).

</details>

<a id="cursor"></a>

<details>
<summary><b>Cursor</b> — GitHub plugin or <code>npx skills</code> into Cursor's skills folders.</summary>

In Cursor, open **Customize, Plugins, Add, From GitHub Repository** and enter `github.com/ysskrishna/ysskrishna-mcp`. In Agent chat you can also run `/add-plugin`.

```bash
npx skills add ysskrishna/ysskrishna-mcp --agent cursor
```

Connect the MCP server (after the skill is installed): add the endpoint as a remote HTTP server in Cursor's MCP settings for the requested scope.

Cursor's docs use `mcpServers.<name>.url` in `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global). This was not added to a live Cursor config.

More in [docs/cursor-setup.md](docs/cursor-setup.md).

</details>

<a id="vscode"></a>

<details>
<summary><b>VS Code</b> — no VS Code–specific skill install command in the reference guides used for this repo.</summary>

Install the skill with a compatible installer, for example:

```bash
npx skills add ysskrishna/ysskrishna-mcp
```

Pick VS Code or the agent host in the installer when prompted.

Connect the MCP server (after the skill is installed): use the MCP server settings UI or **MCP: Add Server**, select HTTP, enter the endpoint `https://www.ysskrishna.space/mcp` and the name `ysskrishna`, and choose the requested configuration destination. Start the server and inspect its tools.

More in [docs/vscode-setup.md](docs/vscode-setup.md).

</details>

<a id="antigravity"></a>

<details>
<summary><b>Antigravity</b> — <code>agy plugin install</code> from GitHub.</summary>

```bash
agy plugin install https://github.com/ysskrishna/ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/antigravity-setup.md](docs/antigravity-setup.md).

</details>

<a id="github-copilot-cli"></a>

<details>
<summary><b>GitHub Copilot CLI</b> — Copilot plugin marketplace install.</summary>

```bash
copilot plugin marketplace add ysskrishna/ysskrishna-mcp
copilot plugin install ysskrishna-mcp@ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/copilot-cli-setup.md](docs/copilot-cli-setup.md).

</details>

<a id="factory-droid"></a>

<details>
<summary><b>Factory Droid</b> — Droid plugin marketplace install.</summary>

```bash
droid plugin marketplace add ysskrishna/ysskrishna-mcp
droid plugin install ysskrishna-mcp@ysskrishna-mcp --scope user
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/droid-setup.md](docs/droid-setup.md).

</details>

<a id="qwen-code"></a>

<details>
<summary><b>Qwen Code</b> — Qwen extension install for the bundle plugin.</summary>

```bash
qwen extensions install ysskrishna/ysskrishna-mcp:ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/qwen-code-setup.md](docs/qwen-code-setup.md).

</details>

<a id="grok-build"></a>

<details>
<summary><b>Grok Build</b> — direct <code>grok plugin install</code> with trust.</summary>

```bash
grok plugin install ysskrishna/ysskrishna-mcp --trust
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/grok-setup.md](docs/grok-setup.md).

</details>

<a id="opencode"></a>

<details>
<summary><b>OpenCode</b> — npm plugin or <code>opencode.json</code> entry.</summary>

```bash
opencode plugin @ysskrishna/ysskrishna-mcp --global
```

OpenCode 1.x, in `opencode.json`:

```json
{
  "plugin": ["@ysskrishna/ysskrishna-mcp"]
}
```

```json
{
  "plugin": ["ysskrishna-mcp@git+https://github.com/ysskrishna/ysskrishna-mcp.git"]
}
```

OpenCode 2.0.4 or later uses the key `plugins` instead of `plugin`.

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/opencode-setup.md](docs/opencode-setup.md).

</details>

<a id="pi"></a>

<details>
<summary><b>Pi</b> — <code>pi install</code> from npm or GitHub.</summary>

```bash
pi install npm:@ysskrishna/ysskrishna-mcp
```

```bash
pi install git:github.com/ysskrishna/ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/pi-setup.md](docs/pi-setup.md).

</details>

<a id="kimi-code"></a>

<details>
<summary><b>Kimi Code</b> — install from the in-app <code>/plugins</code> command.</summary>

```text
/plugins install https://github.com/ysskrishna/ysskrishna-mcp
```

Choose **Trust and install**, then run `/reload`.

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/kimi-setup.md](docs/kimi-setup.md).

</details>

<a id="hermes-agent"></a>

<details>
<summary><b>Hermes Agent</b> — skills tap (recommended).</summary>

```bash
hermes skills tap add ysskrishna/ysskrishna-mcp
hermes skills install ysskrishna/ysskrishna-mcp/connect-ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/hermes-setup.md](docs/hermes-setup.md).

</details>

<a id="devin-cli"></a>

<details>
<summary><b>Devin CLI</b> — <code>devin plugins install</code> (requires Devin login).</summary>

```bash
devin plugins install ysskrishna/ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/devin-setup.md](docs/devin-setup.md).

</details>

<a id="muse"></a>

<details>
<summary><b>Muse</b> — experimental plugins from a local clone.</summary>

```bash
git clone https://github.com/ysskrishna/ysskrishna-mcp.git
MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins install ./ysskrishna-mcp --scope user
MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins approve ysskrishna-mcp
```

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

More in [docs/muse-setup.md](docs/muse-setup.md).

</details>

<a id="skillssh-npx-skills"></a>

<details>
<summary><b>skills.sh (npx skills)</b> — copies skills into each agent's folder.</summary>

[skills.sh](https://skills.sh) supports many agents. Install this repo's skill:

```bash
npx skills add ysskrishna/ysskrishna-mcp
```

```bash
npx skills add ysskrishna/ysskrishna-mcp --list
```

More in [docs/other-agents.md](docs/other-agents.md#skillssh).

</details>

<a id="github-cli-gh-skill"></a>

<details>
<summary><b>GitHub CLI (gh skill)</b> — needs GitHub CLI v2.90.0 or later.</summary>

```bash
gh skill install ysskrishna/ysskrishna-mcp
```

```bash
gh skill install ysskrishna/ysskrishna-mcp connect-ysskrishna-mcp
```

More in [docs/other-agents.md](docs/other-agents.md#github-cli).

</details>

## Usage

Ask your agent to use the `connect-ysskrishna-mcp` skill. It identifies your client and scope, checks existing MCP entries, adds `https://www.ysskrishna.space/mcp` when needed, and verifies the connection where the client supports it.

## Remove

Remove the `ysskrishna` MCP connection with that client's command or MCP settings UI (for example `claude mcp remove ysskrishna -s user`, `codex mcp remove ysskrishna`, or `gemini mcp remove --scope user ysskrishna`). Confirm the entry uses `https://www.ysskrishna.space/mcp` before you remove it.

Remove the skill with the same installer you used to add it. **`gh skill`** has install, list, preview, publish, search, and update only — no remove. Delete the skill directory the installer created (see `gh skill install --help` for where it lands). For **skills.sh**, use `npx skills remove connect-ysskrishna-mcp` (or `npx skills remove --help` for scope and agent flags).

## Built and maintained by

ysskrishna MCP is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Changelog

See [CHANGELOG](CHANGELOG.md) for release history.

## Support

If you find this project helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/ysskrishna-mcp/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://www.npmjs.com/package/@ysskrishna/ysskrishna-mcp">npm package</a> •
  <a href="https://github.com/ysskrishna/ysskrishna-mcp/issues">Report Issues</a>
</p>