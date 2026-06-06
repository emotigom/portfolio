# Codex Prompt: Next.js App Router 포트폴리오로 변환

아래 정적 포트폴리오 사이트를 Next.js App Router + TypeScript + Tailwind CSS 구조로 변환해줘.

## 목표

- 현재 `index.html`, `styles.css`, `script.js`의 디자인과 문구를 최대한 유지한다.
- Next.js 15 App Router 기준으로 작성한다.
- `app/page.tsx`, `app/layout.tsx`, `app/globals.css` 중심으로 구성한다.
- 테마 전환은 클라이언트 컴포넌트로 분리한다.
- 반응형 레이아웃, 접근성, SEO 메타데이터를 유지한다.
- 외부 이미지 없이 CSS만으로 완성한다.

## 요구사항

1. Hero / Intro / Projects / Strengths / Stack / Timeline / Contact 섹션을 유지한다.
2. 프로젝트 카드 데이터는 배열로 분리해 map 렌더링한다.
3. Contact의 GitHub 주소는 placeholder 주석을 남긴다.
4. `npm run lint`와 `npm run typecheck`가 통과하도록 작성한다.
5. 색상은 Tailwind config 없이 CSS 변수 또는 globals.css 기반으로 처리한다.
6. 모바일에서 nav는 숨기고, 카드들은 1열로 쌓이게 한다.

## 산출물

- 변경 파일 목록
- 핵심 구현 설명
- 실행한 검증 명령
