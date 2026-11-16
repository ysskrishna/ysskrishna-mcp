# Release state

For maintainers and coding agents. Update this file **after** a tagged release is on GitHub and that version is on npm.

| Field | Value |
| --- | --- |
| Last shipped version | 1.0.1 |
| Last tag | `v1.0.1` |
| Tagged from `main` at | `b972faa` |
| GitHub Release | https://github.com/ysskrishna/ysskrishna-mcp/releases/tag/v1.0.1 |
| npm | https://www.npmjs.com/package/@ysskrishna/ysskrishna-mcp/v/1.0.1 |

`v1.0.1` is an annotated tag. The GitHub Release body is the tag message, which matches the `1.0.1` section of `CHANGELOG.md`. npm publish succeeded from that tag with provenance. There is no custom social preview image. GitHub About uses the site homepage and 20 topics, including `gemini-cli-extension`.

This file was updated after the tag. That commit is not part of `v1.0.1`.

**Next release:** `python3 scripts/bump_version.py X.Y.Z`, add the changelog section, run `bash validate-skills.sh` and `node --check index.js` on `main`, then push an annotated tag `vX.Y.Z`. See [AGENTS.md](../../AGENTS.md#releases).
