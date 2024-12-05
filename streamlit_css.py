def get_loading():
    return """
    <style>
        .loader {
        width: 15px;
        aspect-ratio: 1;
        border-radius: 50%;
        animation: l5 1s infinite linear alternate;
        }

        @keyframes l5 {
        0% {
            box-shadow: 20px 0 #000, -20px 0 #0002;
            background: #000;
        }
        33% {
            box-shadow: 20px 0 #000, -20px 0 #0002;
            background: #0002;
        }
        66% {
            box-shadow: 20px 0 #0002, -20px 0 #000;
            background: #0002;
        }
        100% {
            box-shadow: 20px 0 #0002, -20px 0 #000;
            background: #000;
        }
        }
        </style>
        """
def get_loading1() :
    return """
    <style>
        .loader {
        width: 120px;
        height: 20px;
        -webkit-mask: linear-gradient(90deg, #000 70%, #0000 0) 0 / 20%;
        background: linear-gradient(#000 0 0) 0 / 0% no-repeat #ddd;
        animation: l4 2s infinite steps(6);
        }

        @keyframes l4 {
        100% {
            background-size: 120%;
        }
        }
        </style>
"""

def get_slide() :
    return """
    <style>
        /* 슬라이더 컨테이너 */
        .slider {
            width: 308px; /* 확대된 슬라이더 가로 크기 */
            height: 450px; /* 확대된 슬라이더 세로 크기 */
            overflow: hidden; /* 넘치는 부분 숨김 */
            position: relative; /* 상대적 위치 설정 */
            margin: auto; /* 중앙 정렬 */
        }

        /* 슬라이드 이미지 컨테이너 */
        .slides {
            display: flex;
            width: calc(308px * 3); /* 이미지 개수만큼 폭 설정 */
            animation: slide 6s infinite; /* 6초 주기로 애니메이션 실행 */
        }

        /* 개별 슬라이드 */
        .slide {
            min-width: 308px; /* 확대된 슬라이드의 가로 크기 */
            height: 450px; /* 확대된 슬라이드의 세로 크기 */
        }

        /* 이미지 */
        .slide img {
            width: 308px; /* 이미지의 가로 크기 */
            height: 450px; /* 이미지의 세로 크기 */
            object-fit: cover; /* 비율 유지하며 크기 조정 */
        }

        /* 애니메이션 */
        @keyframes slide {
            0% { transform: translateX(0); }
            33% { transform: translateX(-308px); }
            66% { transform: translateX(-616px); }
            100% { transform: translateX(0); }
        }
        </style>
        """


def get_status():
    return """
    <style>
        /* 허재원 추가_1130 */
        .status-container {
            text-align: center;
            margin-top: 20px;
        }
        .chatbot-image {
            width: 350px;
            height: auto;
            margin-bottom: 10px;
        }
        .status-message {
            text-align: center;
            font-family: 'Pretendard', sans-serif;
            font-style: normal;
            font-weight: 500;
            font-size: 18px;
            line-height: 120%;
            /* identical to box height, or 29px */
            letter-spacing: -0.02em;
            margin-top: 10px;
        }
        .spinner {
            margin: 10px auto;
            width: 40px;
            height: 40px;
            position: relative;
            text-align: center;
        }
        .double-bounce1, .double-bounce2 {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background-color: #007bff;
            opacity: 0.6;
            position: absolute;
            top: 0;
            left: 0;
            animation: bounce 2s infinite ease-in-out;
        }
        .double-bounce2 {
            animation-delay: -1s;
        }
        @keyframes bounce {
            0%, 100% { transform: scale(0); }
            50% { transform: scale(1); }
        }
    </style>
"""
def get_css():
    return """
    <style>
        /* 사이드바 배경 흰색으로 설정 */
        [data-testid="stSidebar"] {
            background-color: white;
        }

        /* 오른쪽 메인 화면 배경 흰색으로 고정 */
        [data-testid="stAppViewContainer"] {
            background-color: white;
        }

        /* 상단 헤더 배경 흰색으로 고정 */
        header[data-testid="stHeader"] {
            background-color: white;
        }
        
        /* 사이드바 오른쪽에 회색 구분선과 그림자 추가 (필수)*/
        [data-testid="stSidebar"] {
            border-right: 1px solid #d3d3d3; /* 회색 구분선 */
            box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1); /* 오른쪽에 그림자 추가 */
        } 

        /* 사이드바 제목을 우측 화살표와 같은 행에 배치 */
        .sidebar-title {
            display: flex;
            align-items: center;
            font-size: 20px;
            font-weight: bold;
            color: black;
        }
        
        /* 텍스트 입력 상자의 테두리 색상 회색으로 설정 (필수)*/
        input[type="text"] {
            border: 1px solid #d3d3d3;
            padding: 10px;
            border-radius: 5px;
        }
        
        /* 선택된 텍스트 입력 필드의 테두리 강조 색상 (필수)*/
        input[type="text"]:focus {
            border-color: #a9a9a9;  /* 강조 회색 */
            box-shadow: none;
            outline: none;
        }

        /* 사이드바 스타일 수정 */
        .css-1y4p8pa {  /* Streamlit 사이드바 CSS 클래스 */
            padding-right: 1rem;
            padding-left: 1rem;
            overflow-y: auto;
        }

        /* 사이드바와 구분선 간격 확보 */
        .css-1y4p8pa .chatbox-container {
            margin-right: 10px; /* 구분선과 여유 간격 추가 */
        }
            
        /* 챗 섹션 배경을 완전히 흰색으로 설정 */
        .sidebar .css-1y4p8pa {
            background-color: #ffffff !important;
            padding: 10px;
            box-shadow: 2px 0px 5px rgba(0,0,0,0.1); /* 오른쪽에 가벼운 그림자 추가하여 구분 */
            border-right: 1px solid #ddd; /* 두 섹션을 분리하는 얇은 선 추가 */
        }

        /* 채팅창 스타일 */
        .chatbox {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            max-width: 700px;
            margin: auto;
        }

        /* 챗봇 말풍선 스타일 */
        .chatbot-bubble {
            background-color: #f0f0f0; /* 회색 배경색 */
            color: black; /* 글자색 검정 */
            padding: 10px;
            border-radius: 15px; /* 둥근 모서리 */
            margin: 5px 0;
            max-width: 80%; /* 말풍선이 차지하는 최대 너비 */
            display: inline-block;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* 가벼운 그림자 */
            animation: fadeIn 0.5s; /* 서서히 나타나는 애니메이션 */
        }

        /* 사용자 말풍선 스타일 */
        .user-bubble {
            background-color: #007bff; /* 파란색 배경 */
            color: white; /* 글자색 흰색 */
            padding: 10px;
            border-radius: 15px; /* 둥근 모서리 */
            margin: 5px 0;
            max-width: 80%;
            display: inline-block;
            text-align: right; /* 텍스트 오른쪽 정렬 */
            float: right; /* 말풍선을 오른쪽으로 정렬 */
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* 가벼운 그림자 */
            animation: fadeIn 0.5s; /* 서서히 나타나는 애니메이션 */
        }
            
        /* 오른쪽 콘텐츠 영역 스타일 */
        .content-area {
            padding: 20px;
            background-color: #ffffff;
            box-shadow: -2px 0px 5px rgba(0,0,0,0.1); /* 왼쪽에 가벼운 그림자 추가 */
        }
            
        /* 스크롤바 스타일 */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
            
        /* 챗봇 이미지 스타일 */
        .chatbot-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
            vertical-align: middle;
        }
        
        .chatbot-message, .user-message {
            display: flex;
            align-items: center;
        }
    
        /* 애니메이션 효과 */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* 입력창과 버튼 스타일 */
        .input-container {
            display: flex;
            margin-top: 20px;
        }

        .message-input {
            flex: 1;
            padding: 10px;
            border-radius: 20px;
            border: 1px solid #ddd;
            font-size: 16px;
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            margin-right: 10px;
            box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
        }

        .send-button {
            background-color: #007bff;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
            font-size: 16px;
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
        }

        /* 모바일 반응형 디자인 */
        @media (max-width: 768px) {
            .chatbox {
                max-width: 100%;
            }
            .message-input {
                font-size: 14px;
            }
            .send-button {
                font-size: 14px;
                padding: 8px 12px;
            }
        }

        /* 선택된 pills 색상을 파란색 테두리로 변경 - 적용안되는 중...ㅠ */ 
        .st-pills [data-selected="true"] {
            border-color: #007bff !important; /* 파란색 테두리 */
            color: #007bff !important; /* 파란색 텍스트 */
            font-weight: bold !important;
        }
            
        /* 비선택 pills 스타일 - 적용안되는 중...ㅠ */
        .st-pills [data-selected="false"] {
            color: #444 !important;
        }

        /* 결과 파트 전체 페이지의 상단 여백을 최소화하는 CSS 스타일 추가 */

        .main .block-container, .css-1lcbmhc.e1fqkh3o5 {
            padding-top: 0px;  /* 페이지 최상단 간격 제거 */
            
        }
        .header-container {
            text-align: center;
            margin-top: -80px;  /* 화면 상단에서 일정한 거리 유지 */
            margin-bottom: 20px;
        }
        .header-title {
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            font-style: normal;
            font-weight: 600;
            font-size: 24px;
            color: black;
            margin: 5px 0;
        }
        .header-subtitle {
            font-size: 16px;
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            color: #606060;
            font-style: normal;
            font-weight: 400;
            line-height: 120%;
            /* identical to box height, or 24px */
            letter-spacing: -0.02em;
            margin: 0;
        }
        .loading-container {
            text-align: center;
            margin-top: 50px;
        }
        .loading-container img {
            width: 150px;
            margin-top: 20px;
        }
        .loading-container p {
            font-size: 16px;
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            color: #333333;
            margin-top: 10px;
        }
    </style>
"""
def travel_css():
    return """
    <style>
        /* 사이드바 배경 흰색으로 설정 */
        [data-testid="stContainer"] {
            background-color: white;
        }
"""

def travel_card_style():
    return """
    <style>
    /* 여행 일정 카드 스타일 정의 */
    .subheader {
        font-size: 18px;
        font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
        color: black;
        margin-top: 0px;
        }
    .travel-card-container {
        display: flex;
        align-items: flex-start; /* 동그라미와 카드 상단 정렬 */
        margin-bottom: 15px;
    }
    .card-number {
        margin-right: 10px; /* 동그라미와 카드 사이 간격 */
    }
    .circle {
        width: 21px;
        height: 21px;
        border-radius: 50%; /* 원형 */
        background-color: #00199A; /* 파란색 배경 */
        color: white; /* 흰색 텍스트 */
        font-size: 11px;
        font-family: 'Pretendard', sans-serif;
        text-align: center;
        line-height: 21px;
    }
    .travel-card {
        flex: 1;
        border-radius: 8px;
        padding: 10px;
        background-color: #ffffff; /*f9f9f9*/
        box-shadow: 0px 4px 40px 4px rgba(0, 0, 0, 0.08);
        font-family: 'Pretendard', sans-serif;
        font-size: 14px;
    }
    .travel-card-header {
        display: flex;
        align-items: center; /* 이미지와 텍스트 수평 정렬 */
        gap: 10px; /* 이미지와 텍스트 간 간격 */
        margin-bottom: 8px; /* 헤더와 회색선 사이 간격 */
    }
    .travel-card-header img {
        width: 40px; /* 이미지 너비 */
        height: 40px; /* 이미지 높이 */
        object-fit: cover; /* 비율 유지 */
        border-radius: 8px; /* 이미지 모서리 둥글게 */
    }
    .travel-card-header h5 {
        margin: 0;
        font-size: 14px;
        font-family: 'Pretendard', sans-serif;
        color: black;
        display: inline;
    }
    .travel-card-header p.time {
        margin: 0;
        font-size: 12px;
        font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
        color: #888888;
        display: inline;
        margin: 0 0 5px 0;
    }
    .travel-card hr {
        margin: 8px 0;
        border: none;
        border-top: 1px solid #e4e4e4;
    }
    .travel-card p.description {
        font-size: 13px;
        font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
        color: black;
        margin: 0;
    }
    </style>
    """

# 숙소 추천 카드 스타일 정의
def accommodation_card_style():
    return """
    <style>
        .accommodation-card {
            border: none; /* 배경색 및 테두리 제거 */
            padding: 10px;
            margin: 5px auto;
            text-align: left; /* 텍스트 왼쪽 정렬 */
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* 카드 상단부터 정렬 */
            align-items: flex-start; /* 텍스트도 왼쪽 정렬 */
        }

        .accommodation-card img.accommodation-image {
            width: 100%; /* 이미지 너비를 카드 너비에 맞춤 */
            height: 85px; /* 고정된 높이 */
            object-fit: cover; /* 이미지가 비율을 유지하면서 카드 크기에 맞도록 자름 */
            margin-bottom: 5px; /* 이미지 아래 간격 추가 */
            border-radius: 8px; /* 이미지 모서리 둥글게 */
        }
        
        .accommodation-card h6 {
            font-size: 12px;
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            font-weight: bold;
            color: black;
            display: inline;
            margin: 0 0 5px 0;
        }
        .accommodation-card p {
            font-size: 12px;
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            color: black;
            display: inline;
            margin: 0 0 5px 0;
        }
    </style>
"""

# 여행 일정 제목 스타일 정의
def title_style():
    return """
    <style>
        .accommodation-title {
            font-size: 20px; /* 원하는 크기로 조정 */
            font-family: 'Pretendard', sans-serif; /* Pretendard 적용 */
            font-weight: bold;
            color: black;
            margin-bottom: 10px;
        }
    </style>
"""

