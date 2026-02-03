import os
import json
from datetime import datetime, timedelta
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

# 환경 변수에서 키와 프로퍼티 ID 가져오기
key_json = os.environ['GA_KEY']
property_id = os.environ['GA_PROPERTY_ID']

# 서비스 계정 인증
credentials = service_account.Credentials.from_service_account_info(json.loads(key_json))
client = BetaAnalyticsDataClient(credentials=credentials)

# 날짜 계산
today = datetime.now().date()
yesterday_date = today - timedelta(days=1)
yesterday_str = yesterday_date.strftime('%Y-%m-%d')
thirty_days_ago = today - timedelta(days=30)
thirty_days_ago_str = thirty_days_ago.strftime('%Y-%m-%d')

# 헬퍼 함수: 기간 데이터 가져오기
def get_stats(start_date, end_date):
    request = RunReportRequest(
        property=f'properties/{property_id}',
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[Dimension(name='date')],
        metrics=[
            Metric(name='activeUsers'),
            Metric(name='screenPageViews'),
            Metric(name='totalUsers'),
        ],
    )
    response = client.run_report(request)
    if response.rows:
        total_active_users = sum(int(row.metric_values[0].value) for row in response.rows)
        total_screen_page_views = sum(int(row.metric_values[1].value) for row in response.rows)
        total_users = sum(int(row.metric_values[2].value) for row in response.rows)
        return {
            'active_users': total_active_users,
            'screen_page_views': total_screen_page_views,
            'total_users': total_users,
        }
    return {'active_users': 0, 'screen_page_views': 0, 'total_users': 0}

# 데이터 가져오기
total_stats = get_stats('2020-01-01', yesterday_str)  # 전체 기간
thirty_days_stats = get_stats(thirty_days_ago_str, yesterday_str)
yesterday_stats = get_stats(yesterday_str, yesterday_str)

data = {
    'total': total_stats,
    '30days': thirty_days_stats,
    'yesterday': yesterday_stats,
}

# _data 폴더 생성
os.makedirs('_data', exist_ok=True)

# JSON 파일 저장
with open('_data/ga_stats.json', 'w') as f:
    json.dump(data, f, indent=2)