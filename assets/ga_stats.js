// GA Stats Widget
// Embed this script to display GA stats on your site
// Usage: <div id="ga-stats"></div><script src="path/to/ga_stats.js"></script>

(async function() {
  try {
    const response = await fetch('/assets/ga_stats.json'); // Adjust path if needed
    if (!response.ok) throw new Error('Failed to fetch GA stats');
    const data = await response.json();

    const html = `
      <div class="ga-stats">
        <h3>GA Statistics</h3>
        <div class="stat-section">
          <h4>Total</h4>
          <p>Active Users: ${data.total.active_users}</p>
          <p>Screen Page Views: ${data.total.screen_page_views}</p>
          <p>Total Users: ${data.total.total_users}</p>
        </div>
        <div class="stat-section">
          <h4>Last 30 Days</h4>
          <p>Active Users: ${data['30days'].active_users}</p>
          <p>Screen Page Views: ${data['30days'].screen_page_views}</p>
          <p>Total Users: ${data['30days'].total_users}</p>
        </div>
        <div class="stat-section">
          <h4>Yesterday</h4>
          <p>Active Users: ${data.yesterday.active_users}</p>
          <p>Screen Page Views: ${data.yesterday.screen_page_views}</p>
          <p>Total Users: ${data.yesterday.total_users}</p>
        </div>
      </div>
    `;

    document.getElementById('ga-stats').innerHTML = html;
  } catch (error) {
    console.error('Error loading GA stats:', error);
    document.getElementById('ga-stats').innerHTML = '<p>Failed to load GA stats.</p>';
  }
})();