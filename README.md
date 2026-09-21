# Ahn Sangkyoon · Python Backend Portfolio

Python/FastAPI와 PostgreSQL을 중심으로 인증·데이터 경계, 웹 연동, 배포와 검증을 연결한 개발 포트폴리오입니다.

- **Portfolio:** https://emotigom.github.io/portfolio/
- **Resume:** [Python Backend / Backend-first Full-stack PDF](./assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack.pdf)
- **GitHub:** https://github.com/emotigom
- **Contact:** ahnsangkyoon@gmail.com

## Selected engineering work

### SK7 · 상균7데이즈
혈압 관찰과 7일 생활습관 기록·회고를 지원하는 비진단형 서비스입니다.

- **Identity & ownership:** FastAPI에서 Supabase 세션 신원을 확인하고 호출자 토큰을 PostgREST에 전달합니다. 클라이언트가 보낸 사용자 ID 대신 세션 신원을 사용합니다.
- **Data lifecycle:** 서버가 정한 30일 접근 만료와 물리적 정리 작업을 분리하고, RLS에 소유권과 만료 조건을 함께 적용했습니다.
- **Release safety:** 2026-09-07의 API 한정 배포·복구 기록을 연결합니다. 0% 트래픽 검증, 운영 전환, 이전 revision 복구, 새 revision 재적용과 각 smoke 결과를 기록한 과거 증거입니다.
- **Account lifecycle:** 호출자 한정 삭제 API와 오래된 완료 응답이 새 세션을 지우지 못하게 하는 브라우저 경합 테스트를 구분해서 보여줍니다.

[Service](https://hyeol.app/) · [Source](https://github.com/AI-HealthCare-05/AH_05_07)

### Nextbridge
교사 워크숍 현장지원·문의 운영 웹입니다. Edge Functions를 공개 API 경계로 두고 입력 검증, Turnstile, 속도 제한, 멱등성과 트랜잭션 처리를 연결했습니다. SK7의 호출자 JWT 전달 방식과 달리 서버 service-role 경계를 사용합니다.

[Source](https://github.com/emotigom/nextbridge)

### Gomdory Play
학생 입력을 Acorn AST 허용 목록으로 검사한 뒤 `ThrowCommand`로 변환하는 3D 코딩 학습 프로토타입입니다. `eval`/`Function`으로 일반 JavaScript를 실행하지 않습니다.

[Source](https://github.com/emotigom/gomdory-play)

### Stress Score Prediction
3,000행·16개 입력 특성의 회귀 실험입니다. OOF/secondary 검증과 독립 seed 테스트를 구분하고 Public MAE 0.1271을 기록했습니다. Baseline 0.1283 대비 약 0.9% 개선이며, Public 점수를 일반화 성능으로 주장하지 않습니다. 저장소는 비공개이고 이 포트폴리오에서는 코드 공개 검증을 제공하지 않습니다.

## Evidence scope

[Evidence map](./assets/evidence-map.json)에 코드·테스트·설계 문서·과거 운영 기록을 구분했습니다. 코드 링크는 검토한 전체 commit SHA에 고정합니다.

| Project | Reviewed source |
| --- | --- |
| SK7 | `ccc66c165eefbdaec77e5bb0cad57b989f38e92c` |
| Nextbridge | `a52f3c1a97c1b6dc4560c575acfbfee472bffd8a` |
| Gomdory Play | `73b62be750564f89b510bb48a83f4e3a4205ad4c` |

검토일: **2026-09-21**. 고정된 소스나 과거 운영 기록은 현재 서비스 상태를 자동으로 보증하지 않습니다. Mock 테스트는 실제 Supabase RLS나 실제 계정 삭제 검증과 구분합니다. 만료 검증은 2026-09-08 합성 혈압 관찰 행에 한정하며 자연 상태의 30일 관찰을 주장하지 않습니다.

모델은 별도 브라우저-local 경로를 사용합니다. 현재 모델 계약의 기간 한정 수치 미리보기를 영구적인 숫자 미표시 정책으로 설명하지 않습니다. 이력서와 웹은 비진단성 및 분석 입력·결과 미저장 원칙을 유지합니다.

## Site implementation

- Plain semantic HTML, CSS and optional JavaScript. Build step, package manager and runtime dependencies 없음.
- 기본 HTML은 JavaScript 없이도 읽을 수 있습니다. 테마 설정 저장이 차단되어도 페이지는 동작합니다.
- 모바일 메뉴와 account deep dive는 native `details`/`summary`를 사용합니다.
- Dark/light, reduced motion, 키보드 focus 및 모바일 재배치를 지원합니다.
- 승인된 안전한 실제 제품 캡처가 이번 작업에 없었으므로 `Product overview`는 기능 설명입니다. 제품 스크린샷으로 가장한 이미지나 가짜 화면은 넣지 않았습니다.
- 기존 Open Graph 이미지·favicon·권리 고지는 유지합니다. 기존 날짜별 이력서 파일은 삭제하지 않고 현재 CTA만 안정적인 PDF 파일명에 연결합니다.

## Local preview

이 디렉터리에서:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

브라우저에서 `http://127.0.0.1:8000/`을 엽니다. GitHub Pages에서는 기존 `/portfolio/` 경로를 그대로 사용합니다.

## Offline checks

Python 3.9+와 Node.js 18+가 필요합니다. npm 패키지를 설치하지 않습니다.

```bash
python3 scripts/check_site.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
node --check script.js
node --test tests/theme.test.cjs
```

`.github/workflows/portfolio-checks.yml`은 동일 검사를 실행합니다. 외부 링크 HTTP 상태, 실제 배포, 원 프로젝트의 테스트 또는 전체 WCAG 적합성을 보장하는 검사가 아닙니다. 소스 링크 대상은 연결된 GitHub 읽기 도구로 별도 확인했습니다.

## Updating the résumé

`assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack.pdf` 내용만 교체하면 됩니다. PDF와 편집용 DOCX의 내용·날짜를 맞추고 실제 2페이지 렌더링과 링크를 검토합니다. 편집용 DOCX는 이 공개 웹 디렉터리에 추가하지 않습니다.

## License

Site code and general layout: [MIT](./LICENSE). Personal copy, project descriptions, metrics and branding: [Content rights notice](./CONTENT_NOTICE.md).
