# 캠핑 계산기

이 프로젝트는 한 페이지 내에서 가정별 캠핑 사용액을 입력하고 분담금액과 차액을 계산하는 웹 앱입니다.

## 파일

- `index.html`: 입력 및 결과 표시가 모두 포함된 웹 페이지
- `camping_calculator.py`: 기존 Python 계산기 (웹과 별도)

## 배포 방법

### 1. GitHub Pages로 배포하기

1. GitHub에서 새 저장소를 생성합니다.
2. 로컬에서 다음 명령을 실행합니다:

```powershell
cd "c:\Users\wooks\Documents\클로드코드 projects\캠핑계산기"
git add .
git commit -m "Initial deploy setup"
git remote add origin https://github.com/<사용자이름>/<저장소이름>.git
git branch -M main
git push -u origin main
```

3. GitHub 저장소의 `Settings` > `Pages`에서 배포 브랜치를 `main`으로 선택하고 `/ (root)`를 설정합니다.
4. 잠시 후 `https://<사용자이름>.github.io/<저장소이름>/` 주소로 웹 페이지에 접속할 수 있습니다.

### 2. 로컬에서 바로 보기

- `index.html` 파일을 브라우저에서 열면 바로 사용할 수 있습니다.

## 배포 후 확인

- 웹 페이지가 공개된 후에는 `index.html`에서 디자인과 기능을 바로 확인할 수 있습니다.
- 필요하면 GitHub Pages 외에 Netlify나 Vercel로도 배포할 수 있습니다.
