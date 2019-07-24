# SMTP를 이용한 이메일(Gmail) 보내기
---
###  사용법
#### 1. Clone이나 다운로드

#### 2. config.py 수정하기
    Id = 'id here' # test@gmail.com 아이디 입력
    Pw ='token password here' 비밀번호 입력
    From = Id
    To = 'To' 보내는 사람 이메일 주소 입력
    file_name = "path here" 첨부할 파일이 있다면 경로 입력
    Sub = 'sub here ' 메일 제목 입력
    content = 'content here' 내용 입력하기

* __구글 토큰 비밀번호 참고__  https://support.google.com/mail/answer/7126229?hl=ko



#### 3. sendmail.py send mail function 설명
    send_mail(attach=True) 첨부 파일이 있을 경우 True 아니면 False 설정
