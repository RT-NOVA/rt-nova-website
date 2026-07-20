# SEO and search metadata

Search and social-sharing metadata are already wired into the site. Routine updates should edit the current data and partials; do not rerun the original installer script.

## Primary files

- `data/site_seo.yaml` — organization name, official description, service area, social accounts, default image, keywords, and important pages.
- `layouts/partials/seo/meta.html` — canonical, description, Open Graph, Twitter, and indexing metadata.
- `layouts/partials/seo/schema.html` — JSON-LD for the organization, website, pages, breadcrumbs, and news articles.
- `layouts/partials/head/seo.html` — head integration.
- `layouts/sitemap.xml` — custom sitemap output.
- `static/robots.txt` — crawler rules and sitemap location.
- `static/llms.txt` and `static/llms-full.txt` — concise machine-readable program summaries.

## Updating organization facts

Edit `data/site_seo.yaml` when the official description, service area, social account, logo, default sharing image, or important page list changes.

Use production URLs and accurate program facts. Keep page-specific descriptions in each content file's front matter when a generic site description is not sufficient.

## Validation

After an SEO update:

1. Run the normal Hugo production build.
2. Inspect the rendered page source for the canonical URL, description, Open Graph image, and `application/ld+json` blocks.
3. Confirm `/robots.txt`, `/sitemap.xml`, `/llms.txt`, and `/llms-full.txt` build successfully.
4. Check that important pages in `data/site_seo.yaml` still exist.
5. After deployment, use Google Search Console to inspect priority pages and resubmit the sitemap when appropriate.

`robots.txt` and `llms.txt` communicate crawl and entity information; they do not guarantee rankings. Accurate content, working internal links, current pages, and external references to the official domain remain the most important signals.
