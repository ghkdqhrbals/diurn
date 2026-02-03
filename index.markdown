---
layout: home
---

# Welcome to Diurn

This is a Jekyll site that displays daily Google Analytics statistics.

## GA Stats

### Total
- **Active Users**: {{ site.data.ga_stats.total.active_users }}
- **Screen Page Views**: {{ site.data.ga_stats.total.screen_page_views }}
- **Total Users**: {{ site.data.ga_stats.total.total_users }}

### Last 30 Days
- **Active Users**: {{ site.data.ga_stats.30days.active_users }}
- **Screen Page Views**: {{ site.data.ga_stats.30days.screen_page_views }}
- **Total Users**: {{ site.data.ga_stats.30days.total_users }}

### Yesterday
- **Active Users**: {{ site.data.ga_stats.yesterday.active_users }}
- **Screen Page Views**: {{ site.data.ga_stats.yesterday.screen_page_views }}
- **Total Users**: {{ site.data.ga_stats.yesterday.total_users }}
