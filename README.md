# Ahn Sangkyoon Portfolio

교육 현장에서 발견한 문제를 실제 웹 서비스로 만들고, 인증·데이터 경계부터 클라우드 배포와 검증까지 연결해 온 Backend / Backend-heavy Full-stack 개발 포트폴리오입니다.

## Focus

- **Python Backend / Backend-first Full-stack**: FastAPI, REST API, PostgreSQL, React, TypeScript
- **Product & Field**: 초·중·고·특수학교 및 교육기관 50개+ 현장 경험을 제품 요구사항으로 연결
- **Production**: Supabase Auth/RLS, Cloudflare Workers/Pages/R2, Google Cloud Run, GitHub Actions
- **Quality & Operations**: Playwright, pytest, Vitest, Testcontainers, production smoke, rollback verification, runbook

## Selected Projects

### 1. Gomdory
교사 주도 수업, 학생 보드, Courseware와 학생 프로젝트를 하나의 브라우저 기반 흐름으로 연결한 교육 웹 서비스입니다.

- 장기간의 AI·SW 교육 현장에서 반복해서 만난 기기·네트워크·계정·수업 운영 제약을 제품 요구사항으로 구조화
- Next.js / TypeScript + OpenNext Cloudflare runtime
- Supabase Auth/RLS, PostgreSQL, Cloudflare R2
- teacher boards, classroom sessions, Courseware runtime, student projects
- 데이터 처리·보안·운영·복구 runbook을 코드와 함께 관리
- Live: https://gomdory.com/
- Source: https://github.com/emotigom/gom-clean

### 2. SK7 · 상균7데이즈
혈압 관찰값과 7일 생활습관 챌린지를 기록·조회·수정·회고하는 교육·연구 목적의 비진단형 웹 서비스입니다.

- React/TypeScript → FastAPI REST API → Supabase PostgreSQL
- Magic Link access token 검증, 호출자 토큰 전달, RLS 기반 사용자 데이터 소유권
- 30일 데이터 수명주기, 계정 삭제, JSON export
- Cloudflare Worker / Google Cloud Run 분리 배포
- GitHub Actions, Playwright, production smoke, rollback verification
- Evidence: Auth boundary / account removal PR / API release record
- Live: https://hyeol.app/
- Source: https://github.com/AI-HealthCare-05/AH_05_07

### 3. Nextbridge
교사 워크숍의 일정·협의실·현장 질문을 지원하고 행사 종료 상태까지 실제 운영한 웹앱입니다.

- Astro / TypeScript / Supabase Edge Functions
- RLS, 역할별 권한, Turnstile 서버 검증, 원자적 rate limiting
- GitHub Pages / Cloudflare 고정 QR 경로
- 실제 휴대전화 종단 검증과 ready → published → archived 운영
- Source: https://github.com/emotigom/nextbridge

## Engineering Lab

핵심 제품·운영 경험과 별도로, 새로운 기술이나 경계를 재현 가능한 방식으로 깊게 검증하는 실험 저장소입니다.

### Gomdory Play
학생의 제한된 JavaScript 입력을 AST allowlist로 검증해 3D 물리 미션에 연결하는 게임 코딩 교육 프로토타입입니다.

- React / TypeScript / React Three Fiber / Rapier / Acorn
- 학생 코드를 임의 실행하지 않고 허용된 syntax만 내부 명령으로 변환
- Vitest 기반 입력 해석·상태 전이 검증
- Source: https://github.com/emotigom/gomdory-play

### Backend Evidence Lab
production backend 개념을 problem → test → minimal implementation → verification → evidence 순서로 학습하고 검증하는 Spring Boot 실험 저장소입니다.

- Java 21 / Spring Boot / Spring JDBC / PostgreSQL / Flyway
- Testcontainers 기반 실제 PostgreSQL 통합 테스트
- idempotency uniqueness, concurrent race, PostgreSQL ON CONFLICT 기반 CREATED / REPLAYED / conflict semantics
- Source: https://github.com/emotigom/backend-evidence-lab

## Background

2020년부터 초·중·고·특수학교 및 교육기관 50개+ 현장에서 AI·SW 교육을 진행했습니다. 학생·교사와 직접 수업을 운영하며 기기, 브라우저, 학교 네트워크, 계정, 개인정보와 짧은 수업 전환 시간 같은 비개발 환경의 제약을 경험했고, 이를 Gomdory의 화면·세션·권한·데이터·실패 시나리오로 구체화하고 있습니다.

이전에는 KIST 시뮬레이션 연구, DB 관리, 홈페이지 개발·마케팅 운영 경험을 쌓았으며 현재의 데이터·제품 관점으로 연결하고 있습니다.

## Position

Python Backend를 중심으로 Backend-heavy Full-stack, AI/Application Web, Healthcare·EdTech 서비스 개발 역할에 관심이 있습니다.

## Links

- Portfolio: https://emotigom.github.io/portfolio/
- Resume: [Ahn Sangkyoon · Python Backend / Full-stack](./assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack.pdf)
- Gomdory: https://gomdory.com/
- SK7: https://hyeol.app/
- GitHub: https://github.com/emotigom
- Email: ahnsangkyoon@gmail.com

## License

- Site code and general layout: [MIT License](./LICENSE)
- Portfolio copy, project descriptions, metrics, contact information and brand assets: [All rights reserved](./CONTENT_NOTICE.md)
