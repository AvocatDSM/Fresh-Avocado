# Margin(외부여백)
>정의 된 경계 외부에서 요소 주위에 공간을 만든다.  
- margin-top
- margin right
- margin-bottom
- margin left 
# padding(내부여백)
> 정의된 테두리 내에서 내용 주위에 공간을 생성한다.   
- padding-top
- padding-right
- padding-bottom
- padding-left
  
## Values
- auto  
  : browser이 margin을 계산한다.
- length  
  : px, pt, cm 등의 여백을 저장한다.
- %  
  : 포함하는 요소 너비의 여백을 %로 지정한다.
- inherit  
  : 부모 요소에서 여백을 상속하도록 지정한다.  
    
## 속성
- margin/padding: 25px 50px 75px 100px;
  - top = 25px
  - right = 50px;
  - botoom = 75px
  - left = 100px
- margin/padding: 25px 50px 75px;
  - top = 25px
  - right and left = 50px
  - bottom = 75px
- margin/padding: 25px 50px;
  - top and bottom = 25px
  - right and left = 50px
- margin/padding: 25px;
  - 모든 margin = 25px
  
## The auto Value
> container 내에서 가로로 가운데에 맞추도록 설정한다. 왼쪽과 오른쪽 여백 사이가 균등하게 분할된다.  