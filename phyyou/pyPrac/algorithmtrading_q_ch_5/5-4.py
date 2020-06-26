# ## 문제 5-4

#  * 체질량 지수(BMI; Body Mass Index)는 인간의 비만도를 나타내는 지수로서 체중과 키의 관계로 아래의 수식을 통해 계산합니다. 
# 여기서 중요한 점은 체중의 단위는 킬로그램(kg)이고 신장의 단위는 미터(m)라는 점입니다.
#  * BMI=체중(kg) / 신장(m)^2

#  * 일반적으로 BMI 값에 따라 다음과 같이 체형을 분류하고 있습니다.
#  	* BMI < 18.5, 마른체형
#  	* 18.5 <= BMI < 25.0, 표준
#  	* 25.0 <= BMI < 30.0, 비만
#  	* BMI >= 30.0, 고도 비만

#  * 함수의 인자로 체중(kg)과 신장(cm)을 받은 후 BMI 값에 따라 ‘마른체형’, ‘표준’, ‘비만’, ‘고도 비만’ 중 하나를 출력하는 함수를 작성하세요.

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

weight = int(input('weight : '))
height = int(input('height : '))
height_type = input('height_type(ex: cm, m, mm) : ')

cal_ed_BMI = BMI_Cal(weight, height, height_type)

print(BMI_Classify(cal_ed_BMI))