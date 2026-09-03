# One-time cPanel setup (about 10 minutes)

## A. Connect the repo
1. cPanel → **Git™ Version Control** → *Create*.
2. Toggle **Clone a Repository** ON.
   - Clone URL: `https://github.com/<your-user>/alrahalauto-site.git`
     (private repo: use `https://<token>@github.com/<user>/alrahalauto-site.git` — token needs *Contents: read* only; this token lives only on the server)
   - Repository Path: `repositories/alrahalauto-site`
   - Repository Name: `alrahalauto-site`
3. Click **Create**, then **Manage → Pull or Deploy → Deploy HEAD Commit**. This runs `.cpanel.yml`, backs up the current site to `~/backups/`, and publishes `dist/`.

## B. Make it automatic (auto-pull every 5 minutes)
cPanel → **Cron Jobs** → add, every 5 minutes (`*/5 * * * *`):

    cd $HOME/repositories/alrahalauto-site && git fetch -q origin && [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ] && git pull -q origin main && uapi VersionControlDeployment create repository_root=$HOME/repositories/alrahalauto-site >/dev/null 2>&1

From then on: every push Claude makes to `main` is live within 5 minutes.

## C. Rollback
- Fast: cPanel → Git Version Control → Manage → *Pull or Deploy* on an earlier commit, **or** ask Claude to `git revert` (auto-deploys).
- Emergency: cPanel Terminal → `rsync -a --delete ~/backups/site-<timestamp>/ ~/public_html/`

## Notes
- Photos live only on the server in `public_html/assets/img/` and are never deleted by a deploy (the rsync excludes that folder and only adds new images from the repo).
- `.htaccess`, `sitemap.xml`, `robots.txt`, `404.html` are all regenerated from the repo on each deploy.
