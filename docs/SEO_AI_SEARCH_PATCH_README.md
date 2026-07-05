# RT-NOVA SEO / AI Search Patch

This patch adds files intended to help Google, Bing, ChatGPT search, and other answer engines understand that `https://rawlingstigersnova.com/` is the official Rawlings Tigers NOVA website.

## Files included

- `data/site_seo.yaml` — editable organization facts, official description, service-area terms, social links, and important pages.
- `static/robots.txt` — allows normal search engines plus OpenAI `OAI-SearchBot`, `ChatGPT-User`, and `GPTBot`.
- `static/llms.txt` — concise AI-readable site summary.
- `static/llms-full.txt` — longer AI-readable site/entity summary.
- `layouts/partials/seo/meta.html` — canonical URL, description, Open Graph, Twitter card, and indexing metadata.
- `layouts/partials/seo/schema.html` — JSON-LD structured data for SportsOrganization, WebSite, WebPage, BreadcrumbList, and NewsArticle on news pages.
- `layouts/partials/head/seo.html` and `layouts/partials/seo.html` — wrapper partials.
- `layouts/sitemap.xml` — custom XML sitemap with lastmod/changefreq/priority hints.
- `scripts/rt-nova-install-seo.sh` — helper script to wire the SEO partial into the Hugo `<head>`.

## Apply

From the repo root:

```bash
unzip -o ~/Desktop/rt-nova-seo-ai-search-patch.zip -d .
bash scripts/rt-nova-install-seo.sh
hugo server -D --disableFastRender
```

Then view the page source and confirm you see:

```html
<script type="application/ld+json">
```

Also confirm these URLs work locally or after deploy:

- `/robots.txt`
- `/sitemap.xml`
- `/llms.txt`
- `/llms-full.txt`

## After deploy

1. Verify `rawlingstigersnova.com` in Google Search Console.
2. Submit `https://rawlingstigersnova.com/sitemap.xml`.
3. Use URL Inspection and request indexing for the homepage, About, Teams, Tryouts, Coaches, Accolades, Schedules, and Social Hub pages.
4. Update Instagram, Facebook, tournament profiles, and any Rawlings Tigers national references to point to `https://rawlingstigersnova.com/`.

## Notes

- `llms.txt` is a proposed convention, not a guaranteed ranking signal.
- `robots.txt` does not force search engines to rank the site higher; it only communicates crawl permissions and sitemap location.
- The best way to suppress old TeamLinkt results is still to have TeamLinkt unpublish, delete, or noindex the old public pages.
