# Gomdori repository rename — deployment-safe cutover

Status: **Four repository renames verified by stable IDs on 2026-10-31.** Continue checking live GitHub Pages and legacy QR route behavior separately.

Tracking: [portfolio issue #13](https://github.com/emotigom/portfolio/issues/13).


## Verified post-rename milestones (2026-10-31)

- The four new repository URLs resolve under `emotigom` with the same stable repository IDs listed above.
- [Event Support PR #66](https://github.com/emotigom/gomdori-event-support/pull/66) merged: Astro CI and Pages builds derive the project base from the current repo name; required PR CI succeeded. Confirm live route/QR separately.
- [Pipeline PR #6](https://github.com/emotigom/gomdori-lesson-pipeline/pull/6) merged: trusted Factory checkout, state schemas, generators and pinned-SHA validation updated together, and required CI succeeded.
- The Portfolio source URLs and three evidence-map source URLs are updated to the new repository path; original evidence keys, immutable commit SHAs and the verified blob SHAs stay unchanged.
- No external Cloudflare Worker, DNS redirect, Supabase project identity, crypto namespace, or printed QR destination has been changed by the rename follow-up.

## Stable repository identities and intended new names

| GitHub repository ID | Last connector-visible name | Intended name |
| --- | --- | --- |
| `1334987272` | `emotigom/nextbridge-lesson-factory` | `emotigom/gomdori-lesson-factory` |
| `1334903079` | `emotigom/nextbridge-lesson-pipeline` | `emotigom/gomdori-lesson-pipeline` |
| `1329557538` | `emotigom/nextbridge-classroom-kit` | `emotigom/gomdori-classroom-kit` |
| `1331513856` | `emotigom/nextbridge` | `emotigom/gomdori-event-support` |

Recheck repository **IDs** as well as names before applying edits. A 404 can also result from missing connector access. Do not create replacement repositories solely to make a renamed URL appear.

## What a repository rename does **not** migrate

GitHub redirects normal repository browser and Git operations after a rename. **GitHub Pages project-site addresses are excluded.** GitHub also does not redirect calls to a GitHub Action hosted in the renamed repository. Refer to [GitHub's repository rename guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository).

Do not delete historical Git commits, rewrite old evidence SHAs, revoke previously distributed licenses, remove participant access without a plan, or replace cloud service IDs by string substitution.

## Follow-up code edits, in safe order

### 1. Lesson Factory, then Pipeline

- Factory: preserve the deployed Cloudflare Worker identity `nextbridge-lesson-factory` in `wrangler.jsonc` until a separate Cloudflare Worker migration is approved and tested. Changing the GitHub repo name **does not** rename the Cloudflare Worker. Review the `/api/health` service identifier separately.
- Pipeline: replace the trusted Factory repository name **consistently** in `tools/pipelinectl.py`, `tools/handoff_lineage.py`, `tools/new_lesson.py`, `tools/handoff_sync.py`, `config/defaults.json`, both contracts where appropriate, current and fixture states, and `.github/workflows/qa.yml` plus `design-gate.yml`. Changing only README will fail the pipeline's exact-repository security check.
- Preserve pinned `factoryCommitSha` values. Existing commit identities survive repository rename.
- Update README, operations/security docs and future generated metadata. A historical decision record can retain dated names with a small explanation.
- Run `python3 -m unittest discover -s tests -v` and the exact Factory integration workflows before merging.

### 2. Classroom Kit GitHub Pages

- Current Pages workflow deploys `index.html`, `programs/`, and `go/` into the project site's artifact.
- New project path is expected to be `https://emotigom.github.io/gomdori-classroom-kit/`; this is **not live-confirmed**.
- Audit any hard-coded links in `go/workshop/index.html`, metadata and guide pages. Keep the original printed QR link working via independently verified redirect or compatible legacy hosting.
- Re-run `npm run check`, Pages deployment, direct mobile QR tests and an external URL check. Do **not** assume the old `github.io/nextbridge-classroom-kit/` URL redirects.

### 3. Event Support Pages — high risk

- The existing `astro.config.mjs`, `.github/workflows/pages.yml`, `.github/workflows/ci.yml`, README and `scripts/check-build.mjs` assume the original `/nextbridge` base path.
- After repository identity resolves, update the **default** Astro base and both workflows to `/gomdori-event-support` in a single tested PR. Modify the root-relative asset validator in `scripts/check-build.mjs` to derive the expected prefix rather than baking in `nextbridge`.
- Keep the existing `/nextbridge` URL accessible through a deliberately hosted redirect/alias where possible; project Pages paths do not redirect automatically.
- Check the Kakao/Naver navigation `appname`, app manifests, service-worker scope and caches, mobile deep links, SEO metadata, and Cloudflare `https://go.gomdory.com/2026-sk` destination.
- Verify Supabase allowed origins / CORS and sign-in redirects as applicable. **Do not** rename actual Supabase project IDs, deployed function hosts or the private token cryptographic namespace (`nextbridge-private-token:`) as part of repository rename.
- Run `npm ci && npm run verify`, verify GitHub Pages deployment and test archived status lookup without changing the archived event or reopening submissions.

### 4. Portfolio / evidence

- After the new URLs resolve with the original IDs, update the portfolio's current `Source:` link and any present-facing repository links.
- Keep SHA-pinned historical evidence links and `assets/evidence-map.json` revision hashes intact unless source reachability and blob identity are verified; record old path as historic if necessary.
- Run portfolio CI checks before merging.

## Verification gates and rollback

1. Authenticate to the intended `emotigom` account. Confirm all four new URLs **and stable repo IDs**. Inspect the repository's **Settings → General → Repository name** if the connector remains inconsistent.
2. Confirm Pages source configuration after each rename. Check the deployment workflow and direct HTTP response for the new and old project-site URL separately.
3. Update code on feature branches and merge only after required checks. Do not bypass the `verify` gate.
4. Check printed QR destinations on a phone, paths without a trailing slash, deep-linked archived lookup pages, 404 handling, and cached PWA behavior.
5. For local clones, run `git remote set-url origin https://github.com/emotigom/<new-name>.git` only after the new URL resolves.
6. If a website fails, roll back the Pages deployment or route to the last known working origin. A GitHub repo rename rollback alone does not recover old GitHub Pages paths; keep a compatible legacy route.

## Historical audit before the final rename confirmation (2026-10-31)

The connected GitHub API listed all four old repository names and returned 404 for all proposed new names. A lookup by stable repository IDs also returned the old names. No renames, external DNS changes, Cloudflare Worker migrations, Supabase writes or destructive changes were made by this audit.

That discrepancy was resolved by the user completing the GitHub UI rename confirmation. The original repository IDs now resolve at the Gomdori slugs. Continue to preserve Git evidence and the original printed QR routes.
