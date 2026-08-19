# Automated Maintenance

This repository uses a daily GitHub Actions job to produce `reports/latest.md`.

The job checks links already present in `README.md` through the GitHub API and searches a small set of writing-related queries for new candidates. It records repository metadata and evidence leads; it does not rewrite `README.md` and it does not decide that a candidate belongs in the index.

The workflow pushes the report to the automation-owned `automation/daily-update` branch and opens or updates one review pull request. Each run replaces that branch with a fresh report based on the latest `main`; do not place manual work on that branch. The `main` branch changes only after a maintainer reviews and merges that pull request.

## Quality boundary

- An inaccessible, archived, forked, or license-undeclared entry is flagged for review.
- Candidate discovery is a lead, not a recommendation.
- Candidate tiers only prioritize review using topic relevance, declared licensing, adoption, recent activity, and available description evidence.
- Descriptions, community adoption claims, licensing, and security implications require source review.
- The workflow only uses the GitHub API and standard-library Python; it does not install discovered Skills or execute repository scripts.

## GitHub setting

Repository Actions settings must allow workflows to create pull requests. The workflow requests only `contents: write` and `pull-requests: write`; it does not approve its own pull request.

The scheduled run is configured for 04:00 Asia/Shanghai using the UTC cron expression `0 20 * * *` (20:00 UTC on the previous calendar day). GitHub may delay scheduled jobs during high load, so this is a target time rather than a strict real-time guarantee.

Run it manually with **Actions → Daily repository update report → Run workflow**.
