# Ahn Sangkyoon Portfolio Site

교육 기술, AI/데이터 분석, 웹 개발 프로젝트를 소개하는 정적 포트폴리오 사이트입니다.

## 구성

- `index.html` — 전체 페이지 구조
- `styles.css` — 반응형 스타일, 다크/라이트 테마
- `script.js` — 테마 전환, 연도 표시
- `README.md` — 사용 방법

## 바로 실행하기

파일을 압축 해제한 뒤 `index.html`을 브라우저에서 열면 됩니다.

VS Code를 사용한다면 Live Server 확장 프로그램으로 실행해도 좋습니다.

## 수정할 부분

1. `index.html`의 Contact 섹션에서 GitHub 주소를 실제 주소로 수정하세요.
2. 프로젝트 카드의 설명을 실제 공개 가능한 내용 기준으로 다듬으세요.
3. 배포 시에는 Vercel, Netlify, GitHub Pages 중 하나를 사용하면 됩니다.

## GitHub Pages 배포 예시

```bash
git init
git add .
git commit -m "Add portfolio site"
git branch -M main
git remote add origin https://github.com/YOUR_ID/YOUR_REPO.git
git push -u origin main
```

GitHub 저장소 Settings → Pages → Deploy from branch → main / root 선택.
