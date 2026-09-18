# Ahn Sangkyoon Portfolio

Python/FastAPI와 React/TypeScript를 기반으로 웹 서비스를 구현하고, 인증·데이터 경계부터 클라우드 배포와 QA까지 연결해 온 개발 포트폴리오입니다.

## Focus

- **Python Backend / Full-stack**: FastAPI, REST API, PostgreSQL, React, TypeScript
- **Production**: Supabase Auth/RLS, Cloudflare Workers/R2, Google Cloud Run, GitHub Actions
- **Quality**: Playwright, pytest, Vitest, production smoke / rollback verification
- **AI & Data**: scikit-learn, pandas, NumPy, tabular regression, OOF validation

## Selected Projects

### 1. SK7 · 상균7데이즈
AI 헬스케어 KDT 캡스톤으로 개발한 비진단형 혈압·생활습관 관찰/회고 웹 서비스입니다.

- React/TypeScript → FastAPI REST API → Supabase PostgreSQL
- Magic Link, JWT, RLS 기반 사용자 데이터 소유권
- 30일 데이터 수명주기, 계정 삭제, JSON export
- Cloudflare Worker / Google Cloud Run 분리 배포
- GitHub Actions, Playwright, production smoke, rollback verification
- Live: https://hyeol.app/
- Source: https://github.com/AI-HealthCare-05/AH_05_07

### 2. Nextbridge
교사 워크숍의 일정·협의실·현장 질문을 지원한 실제 운영 웹앱입니다.

- Astro / TypeScript / Supabase Edge Functions
- RLS, 역할별 권한, Turnstile 서버 검증, 속도 제한
- GitHub Pages / Cloudflare QR 경로
- 실제 휴대전화 종단 검증과 행사 종료 archive
- Source: https://github.com/emotigom/nextbridge

### 3. Stress Score Prediction
3,000행·16개 특성의 회귀 문제에서 모델 실험과 검증 계약을 관리한 ML 프로젝트입니다.

- Python / scikit-learn / ExtraTrees / 거리 기반 모델
- OOF, secondary validation, independent seed test
- Public MAE 0.1271 (baseline 0.1283 대비 약 0.9% 개선)
- 실제 제출 Notebook과 미채택 가설 기록
- Repository: private

### 4. Gomdory Play
학생 코드 입력을 3D 물리 상호작용으로 연결한 게임 코딩 교육 프로토타입입니다.

- React / TypeScript / React Three Fiber / Rapier / Acorn
- 제한된 JavaScript 입력 파싱 및 검증
- power, variable, expression, angle 단계형 미션
- Vitest 기반 로직 검증
- Source: https://github.com/emotigom/gomdory-play

## Background

초·중·고 및 교육기관의 50개+ 현장에서 SW·AI 교육을 진행했습니다. 장기간의 현장 경험을 바탕으로 비개발 사용자의 요구를 화면·API·데이터·권한·실패 시나리오로 구조화하는 데 강점이 있습니다.

## Links

- Resume: [Ahn Sangkyoon · Python Backend / Full-stack](./assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack_20260918.pdf)
- GitHub: https://github.com/emotigom
- Email: ahnsangkyoon@gmail.com
- SK7: https://hyeol.app/

## License

- Site code and general layout: [MIT License](./LICENSE)
- Portfolio copy, project descriptions, metrics, contact information and brand assets: [All rights reserved](./CONTENT_NOTICE.md)
