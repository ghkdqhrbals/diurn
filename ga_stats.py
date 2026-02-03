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

# GA4 보고서 요청
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

from google.protobuf.json_format import MessageToDict

response = client.run_report(request)

# 전체 response 출력 (디버깅용)
response_dict = MessageToDict(response._pb)
print(json.dumps(response_dict, indent=2))

# 데이터 추출
if response.rows:
    total_active_users = 0
    total_screen_page_views = 0
    total_users = 0
    dates = []
    for row in response.rows:
        date_str = row.dimension_values[0].value
        date_obj = datetime.strptime(date_str, '%Y%m%d')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        dates.append(formatted_date)
        total_active_users += int(row.metric_values[0].value)
        total_screen_page_views += int(row.metric_values[1].value)
        total_users += int(row.metric_values[2].value)
    data = {
        'start_date': start_date,
        'end_date': end_date,
        'dates': dates,
        'total_active_users': total_active_users,
        'total_screen_page_views': total_screen_page_views,
        'total_users': total_users,
    }
else:
    data = {
        'start_date': start_date,
        'end_date': end_date,
        'dates': [],
        'total_active_users': 0,
        'total_screen_page_views': 0,
        'total_users': 0,
    }

# _data 폴더 생성
os.makedirs('_data', exist_ok=True)

# JSON 파일 저장
with open('_data/ga_stats.json', 'w') as f:
    json.dump(data, f, indent=2)