# Release state

For maintainers and coding agents. Update this file **after** a tagged release is on GitHub and that version is on npm.

| Field | Value |
| --- | --- |
| Last shipped version | 1.0.0 |
| Last tag | `v1.0.0` |
| Tagged from `main` at | `0e2be2d` |
| GitHub Release | https://github.com/ysskrishna/ysskrishna-mcp/releases/tag/v1.0.0 |
| npm | https://www.npmjs.com/package/@ysskrishna/ysskrishna-mcp/v/1.0.0 |

`v1.0.0` is a lightweight tag. Its GitHub Release body came from the `1.0.0` section of `CHANGELOG.md`. There is no custom social preview image. GitHub topics were empty at that release.

**Next release:** `python3 scripts/bump_version.py X.Y.Z`, add the changelog section, run `bash validate-skills.sh` and `node --check index.js` on `main`, then push an annotated tag `vX.Y.Z`. See [AGENTS.md](../../AGENTS.md#releases).
