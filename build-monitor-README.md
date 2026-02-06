# Build Monitor Action

GitHub Action to monitor build time, send health status, and report success/failure like a sidecar.

## Usage

Use as a sidecar to monitor your build process:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Start Build Monitor
      uses: ghkdqhrbals/build-monitor@main
      with:
        action: start
        project_name: 'my-project'
        webhook_url: ${{ secrets.WEBHOOK_URL }}
    - name: Build
      run: npm run build
    - name: Test
      run: npm test
    - name: End Build Monitor
      uses: ghkdqhrbals/build-monitor@main
      with:
        action: end
        project_name: 'my-project'
        webhook_url: ${{ secrets.WEBHOOK_URL }}
```

## Inputs

- `action`: 'start' or 'end' (required)
- `webhook_url`: Webhook URL to send health status (optional)
- `health_check_url`: URL to perform health check (optional)
- `project_name`: Project name for reporting (optional, default: 'unknown')

## Outputs

- `build_time`: Build duration in seconds (end action only)
- `build_status`: 'success' or 'failure' (end action only)
- `health_status`: 'healthy', 'unhealthy', or 'unknown' (end action only)

## Features

- Measures build time from start to end
- Sends JSON payload to webhook with build details
- Reports success/failure based on job status
- Can be used across multiple jobs/steps