# Diurn

Jekyll 기반 사이트로, GitHub Actions를 사용하여 매일 Google Analytics 통계를 가져와 JSON으로 저장합니다.

## 설정

1. Google Analytics 4 프로퍼티를 생성하고, 서비스 계정을 만드세요.
2. 서비스 계정 키(JSON)를 다운로드하세요.
3. GitHub 리포지토리의 Settings > Secrets and variables > Actions에서 다음 Secrets를 추가하세요:
   - `GA_KEY`: 서비스 계정 JSON 키의 전체 내용
   - `GA_PROPERTY_ID`: GA4 프로퍼티 ID (예: 123456789)
4. 서비스 계정에 GA4 프로퍼티에 대한 읽기 권한을 부여하세요.

## 워크플로우

- 매일 자정(UTC)에 자동으로 실행됩니다.
- 수동으로도 실행 가능합니다 (Actions 탭에서).

## 데이터 사용

`_data/ga_stats.json`에 저장된 데이터를 Jekyll에서 사용할 수 있습니다.

예시:
```liquid
Active Users: {{ site.data.ga_stats.activeUsers }}
Screen Page Views: {{ site.data.ga_stats.screenPageViews }}
Total Users: {{ site.data.ga_stats.totalUsers }}
```

## 로컬 실행

```bash
bundle exec jekyll serve
```