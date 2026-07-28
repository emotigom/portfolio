# Ahn Sangkyoon Portfolio

교육 현장의 문제를 수업 설계, 웹 제품, AI·데이터 프로젝트로 해결해 온 과정을 정리한 개인 포트폴리오입니다.

## 핵심 방향

- 학교·기관의 실제 사용 환경에서 출발하는 classroom-first 제품 개발
- 아이디어를 사용자 흐름, API, 데이터, 권한과 테스트로 구체화
- 구현뿐 아니라 배포, 운영 문서, 실패 복구와 피드백 반영까지 연결
- AI 결과를 그대로 사용하는 대신 사람이 선택·수정·검증하는 과정 강조

## 대표 내용

- **Gomdory / Gomboard**: Next.js, Supabase, Cloudflare 기반 교육용 보드 플랫폼
- **흉부 X-ray 폐렴 분류**: DenseNet·ConvNeXt 기반 의료 영상 분류 실험
- **AI Health Web Assignment**: FastAPI 환자·진료기록 API 및 Redis·Celery 비동기 아키텍처 설계
- **AI·웹 창작 16차시 프로그램**: 생성형 AI, HTML/CSS/JS, 음악·영상 AI와 작품 공유 수업

## 로컬 실행

별도 빌드 도구 없이 정적 파일로 구성되어 있습니다.

```bash
python -m http.server 8000
```

브라우저에서 `http://localhost:8000`을 열면 됩니다.

## 파일

- `index.html`: 포트폴리오 본문
- `styles.css`: 반응형 레이아웃과 다크·라이트 테마
- `script.js`: 테마 저장, 현재 연도, 스크롤 등장 효과
- `assets/profile-dog.png`: 기존 포트폴리오 마스코트 이미지

## Links

- GitHub: https://github.com/emotigom
- Email: ahnsangkyoon@gmail.com
