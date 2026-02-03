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

# 헬퍼 함수: 기간 데이터 가져오기 (단일 요청)
def get_stats_for_ranges(ranges):
    request = RunReportRequest(
        property=f'properties/{property_id}',
        date_ranges=ranges,
        # dimensions=[Dimension(name='date')],  # 제거하여 range별 합산
        metrics=[
            Metric(name='activeUsers'),
            Metric(name='screenPageViews'),
            Metric(name='totalUsers'),
        ],
    )
    response = client.run_report(request)
    stats = []
    for row in response.rows:
        stats.append({
            'active_users': int(row.metric_values[0].value),
            'screen_page_views': int(row.metric_values[1].value),
            'total_users': int(row.metric_values[2].value),
        })
    return stats

# 데이터 가져오기 (한 요청에 여러 ranges)
ranges = [
    DateRange(start_date='2020-01-01', end_date=yesterday_str),  # total
    DateRange(start_date=thirty_days_ago_str, end_date=yesterday_str),  # 30days
    DateRange(start_date=yesterday_str, end_date=yesterday_str),  # yesterday
]
stats_list = get_stats_for_ranges(ranges)

print(f"Stats list length: {len(stats_list)}")
for i, stat in enumerate(stats_list):
    print(f"Range {i}: {stat}")

data = {
    'total': stats_list[0] if len(stats_list) > 0 else {'active_users': 0, 'screen_page_views': 0, 'total_users': 0},
    '30days': stats_list[1] if len(stats_list) > 1 else {'active_users': 0, 'screen_page_views': 0, 'total_users': 0},
    'yesterday': stats_list[2] if len(stats_list) > 2 else {'active_users': 0, 'screen_page_views': 0, 'total_users': 0},
}

# _data 폴더 생성
os.makedirs('_data', exist_ok=True)

# JSON 파일 저장
with open('_data/ga_stats.json', 'w') as f:
    json.dump(data, f, indent=2)