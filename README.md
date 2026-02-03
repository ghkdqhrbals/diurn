# GA Stats Fetcher

GitHub Action to fetch Google Analytics 4 daily stats and save to JSON.

## Usage

```yaml
- uses: your-username/ga-stats-fetcher@v1
  with:
    ga_key: ${{ secrets.GA_KEY }}
    ga_property_id: '123456789'
    start_date: '2023-01-01'
    end_date: '2023-01-01'
```

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
3. Use the JSON as `ga_key` input (store in secrets).