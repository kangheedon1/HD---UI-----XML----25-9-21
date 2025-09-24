# HD BAS 29.3.1 Generator
HD-기능-UI-로작-실행로직-XML -모음-25-9-21-통합

## 개요
Building Automation System (BAS) 29.3.1 표준을 준수하는 XML 설정 파일을 생성하는 통합 도구입니다.

## 기능
- 🏢 BAS 29.3.1 표준 XML 생성
- 🎨 사용자 친화적인 웹 UI 인터페이스
- ⚙️ 장치 및 자동화 규칙 설정
- 📱 반응형 디자인 (모바일 지원)
- 🔧 사전 정의된 템플릿 제공
- ✅ XML 스키마 유효성 검사
- 💾 XML 파일 다운로드

## 구성 요소

### 1. bas_generator.py
- BAS 29.3.1 XML 생성 엔진
- 템플릿 기반 설정 생성
- Python 라이브러리로 사용 가능

### 2. bas-schema.xsd
- BAS 29.3.1 XML 스키마 정의
- 유효성 검사 기준
- 표준 준수 보장

### 3. index.html
- 웹 기반 사용자 인터페이스
- 대화형 설정 도구
- 실시간 XML 생성 및 미리보기

### 4. server.py
- HTTP 서버 (개발용)
- UI와 백엔드 연결
- RESTful API 제공

## 사용 방법

### 명령줄에서 사용
```bash
python3 bas_generator.py
```

### 웹 인터페이스 사용
```bash
python3 server.py
```
브라우저에서 http://localhost:8000 접속

### 라이브러리로 사용
```python
from bas_generator import BAS291Generator

generator = BAS291Generator()
config = generator.load_template("basic")
xml_output = generator.generate_bas_config(config)
generator.save_config(config, "my_bas_config.xml")
```

## 지원 장치 유형
- HVAC (난방, 환기, 공조)
- Lighting (조명 제어)
- Security (보안 시스템)
- Occupancy (점유 감지)
- Energy (에너지 관리)
- Fire Safety (화재 안전)
- Access Control (출입 통제)
- Elevator (엘리베이터)
- Water Management (물 관리)

## 지원 프로토콜
- BACnet
- Modbus
- DALI
- KNX
- LonWorks
- MQTT
- HTTP
- TCP

## 템플릿
- **Basic**: 기본 BAS 설정 (HVAC + 에너지 절약 규칙)
- **Advanced**: 고급 BAS 설정 (HVAC + 조명 + 종합 자동화)

## XML 스키마 준수
생성되는 모든 XML은 BAS 29.3.1 표준을 준수하며, 다음을 포함합니다:
- 시스템 정보
- 장치 설정
- 자동화 규칙
- UI 구성
- 네임스페이스 및 스키마 검증

## 요구사항
- Python 3.6+
- 최신 웹 브라우저 (Chrome, Firefox, Safari, Edge)

## 파일 구조
```
HD---UI-----XML----25-9-21/
├── README.md              # 프로젝트 문서
├── bas_generator.py       # BAS 생성기 엔진
├── bas-schema.xsd         # XML 스키마 정의
├── index.html             # 웹 UI 인터페이스
├── server.py              # HTTP 서버
└── bas_config_29.3.1.xml  # 생성된 예제 XML
```

## 개발자 정보
- 버전: 29.3.1
- 언어 지원: 한국어, 영어, 일본어, 중국어
- 라이선스: MIT
