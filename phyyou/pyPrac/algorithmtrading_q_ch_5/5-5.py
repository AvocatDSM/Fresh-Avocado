# ## 문제 5-5

#  * 사용자로부터 키(cm)와 몸무게(kg)를 입력받은 후 BMI 값과 BMI 값에 따른 체형 정보를 화면에 출력하는 프로그램을 작성해 보세요. 
#  파이썬에서 사용자 입력을 받을 때는 input 함수를 사용하며, 작성된 프로그램은 계속해서 사용자로부터 키와 몸무게를 입력받은 후 
#  BMI 및 체형 정보를 출력해야 합니다(무한 루프 구조).

def BMI_Cal(Mass, BodyHeight, Type_BodyHeight):
    if Type_BodyHeight == 'cm':
        BodyHeight /= 100.0
    elif Type_BodyHeight == 'm':
        BodyHeight = float(BodyHeight)
    elif Type_BodyHeight == 'mm':
        BodyHeight /= 1000.0
    BMI = Mass / (BodyHeight * BodyHeight)
    
    return BMI

def BMI_Classify(BMI):
    if BMI >= 30.0:
        return '고도 비만'
    elif BMI >= 25.0 and BMI < 30.0:
        return '비만'
    elif BMI >= 18.5 and BMI < 25.0:
        return '표준'
    elif BMI < 18.5 and BMI > 0.0:
        return '마른체형'
    else:
        return '계산할 수 없음'

while 1:
    weight = int(input('weight : '))
    height = int(input('height : '))
    height_type = input('height_type(ex: cm, m, mm) : ')
    cal_ed_BMI = BMI_Cal(weight, height, height_type)
    print(BMI_Classify(cal_ed_BMI))