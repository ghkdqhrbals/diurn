import os
import json
from datetime import datetime, timedelta
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

# 환경 변수에서 키와 프로퍼티 ID 가져오기
key_json = os.environ['GA_KEY']
property_id = os.environ['GA_PROPERTY_ID']

# 환경 변수에서 날짜 가져오기 (기본값 yesterday)
start_date = os.environ.get('START_DATE', 'yesterday')
end_date = os.environ.get('END_DATE', 'yesterday')

# 서비스 계정 인증
credentials = service_account.Credentials.from_service_account_info(json.loads(key_json))
client = BetaAnalyticsDataClient(credentials=credentials)

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

response = client.run_report(request)

# 데이터 추출 (첫 번째 행 가정)
if response.rows:
    row = response.rows[0]
    date_str = row.dimension_values[0].value
    date_obj = datetime.strptime(date_str, '%Y%m%d')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    data = {
        'date': formatted_date,
        'activeUsers': int(row.metric_values[0].value),
        'screenPageViews': int(row.metric_values[1].value),
        'totalUsers': int(row.metric_values[2].value),
    }
else:
    data = {
        'date': yesterday,
        'activeUsers': 0,
        'screenPageViews': 0,
        'totalUsers': 0,
    }

# _data 폴더 생성
os.makedirs('_data', exist_ok=True)

# JSON 파일 저장
with open('_data/ga_stats.json', 'w') as f:
    json.dump(data, f, indent=2)