make_data : 레이더영상 => 숫자데이터
make_model : 숫자데이터 => 모델저장or트레이닝 => 정확도 계산
GUI : make_data + make_model + 데이터에 따라 excel파일 두개로 나누기(make_data하고 make_model하려면 엑셀을 수동으로 두파일로 쪼개야함)

개발환경 : windows10/pycharm
GUI를 실행하신후에 data가 excel파일에 생성이 되면 excel파일에 들어가 a열a행을 수정해야합니다.(동일한 숫자로 다시 써주면 됨/안그러면 오류가 생기는데 원인을 모름)
그후에 버튼대로 실행하시면 됩니다.

cf) 레이더 영상 데이터는 용량이 커서 보기로 한달정도의 데이터만 첨부합니다. 알집파일을 풀고 python 실행파일과 같은 경로에 두시면 됩니다.