# GA Stats Fetcher

GitHub Action to fetch Google Analytics 4 daily stats and save to JSON.

## Usage

Add this action to your workflow:

```yaml
- uses: ghkdqhrbals/ga-stats-fetcher@main
  with:
    ga_key: ${{ secrets.GA_KEY }}
    ga_property_id: '123456789'
```

This will generate `_data/ga_stats.json` with stats for total, last 30 days, and yesterday.

## JavaScript Widget

Embed the GA stats widget in your HTML:

```html
<div id="ga-stats"></div>
<script src="https://your-username.github.io/your-repo/assets/ga_stats.js"></script>
```

This will display the GA stats in the div. Adjust the script src to your GitHub Pages URL.

## Jekyll Integration

In your Jekyll site, you can access the data in Liquid templates:

```liquid
<!-- Total stats -->
Total Active Users: {{ site.data.ga_stats.total.active_users }}
Total Screen Page Views: {{ site.data.ga_stats.total.screen_page_views }}
Total Users: {{ site.data.ga_stats.total.total_users }}

<!-- Last 30 days -->
30 Days Active Users: {{ site.data.ga_stats["30days"].active_users }}
30 Days Screen Page Views: {{ site.data.ga_stats["30days"].screen_page_views }}
30 Days Total Users: {{ site.data.ga_stats["30days"].total_users }}

<!-- Yesterday -->
Yesterday Active Users: {{ site.data.ga_stats.yesterday.active_users }}
Yesterday Screen Page Views: {{ site.data.ga_stats.yesterday.screen_page_views }}
Yesterday Total Users: {{ site.data.ga_stats.yesterday.total_users }}
```

Or use the JavaScript widget for dynamic loading.

## Inputs

- `ga_key`: GA service account key JSON string (required)
- `ga_property_id`: GA4 property ID (required)
- `start_date`: Start date (optional, default: 'yesterday')
- `end_date`: End date (optional, default: 'yesterday')

## Outputs

Saves `_data/ga_stats.json` with the stats.

## Setup

1. Create a GA4 property and service account with read access.
2. Download the service account key JSON.
3. Add `GA_KEY` secret in your repo with the JSON content.
4. Set `ga_property_id` to your GA4 property ID.

## Testing

A separate test workflow (`.github/workflows/test-ga.yml`) runs on pushes to `ga_stats.py` or `action.yml`, or manually via workflow dispatch. It tests the action locally and verifies the output JSON is generated.