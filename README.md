# Train-yolo
# 요약
  현행 민원 접수 서비스는 시민이 불량 시설 보수 요청 민원 등의 신고를 하면 이를 사람이 보고 판단하기 때문에 신고가 접수되고 처리되는 과정에서 지연과, 인력 소모가 발생하였다.  
  
  사람 대신 객체 탐지 모델을 배치하여 사람 대신 불량 시설물을 탐지하고 이후 처리도 자동화한다면 이러한 문제를 해결할 수 있을 것이다.  
  
  따라서 본 연구에서는 YOLO 모델을 학습시켜 국내 보행 시설의 불량을 감지할 수 있게 만들고, 해당 모델을 배치한 애플리케이션을 구현하였다.  

  모델 학습 진행 : https://github.com/DS-Capstone-Design-2024-Fall/Train-yolo/tree/main/test  
  애플리케이션 : https://github.com/DS-Capstone-Design-2024-Fall/Application/blob/master/README.md  

# 진행 과정
https://smart-iodine-e75.notion.site/YOLO-10c146b8dcc080e7bf32d874cc04bad0

# 최종 보고서
https://docs.google.com/document/d/1oWqzZ8Lzyj9g7yxoUFqUnwwkBu3X2BCG5d6s0eM3ewA/edit?tab=t.0

# 파일 설명
Train-yolo/  
├── preprocessing/          # 데이터 전처리를 위한 디렉토리  
├── test/                   # 모델 테스트 관련 디렉토리  
│     ├── results/            # 테스트 결과를 저장하는 디렉토리  
├── train/                  # 모델 학습 관련 디렉토리  
│     ├── results/            # 학습 결과를 저장하는 디렉토리  
├── .gitignore              # Git 무시 파일 설정  
├── README.md               # 프로젝트 설명 문서  
├── crack-pretraining.yaml  # 균열 탐지 사전 학습 설정 파일  
├── image_labeling.py       # 이미지 라벨링 관련 스크립트  
└── street-facilities.yaml  # 도로 시설물 설정 파일  

**crack-pretraining.yaml**  
Pre training 에 필요한, 모델 입력 데이터셋에 대한 메타데이터 정보  

**street-facilities.yaml**  
모델 학습에 필요한, 모델 입력 데이터셋에 대한 메타데이터 정보  

**Preprocessing 폴더**  
데이터 전처리에 관한 코드 모음  

**Test 폴더**  
1. 모델 test 실행 python 파일 및 쉘 스크립트 (경희대학교 Seraph GPU 에서 실행하기 위한 용도) 파일  
2. 테스트 결과 : 하위 디렉토리 results  

**Train 폴더**  
1. 모델 train 실행 관련 python 파일 및 쉘 스크립트  
2. 모델 튜닝 관련 python 파일 및 쉘 스크립트  
3. Pre-training 관련 python 파일 및 쉘 스크립트 (여러 실험 중 하나였으나 의미있는 결과는 X)  
4. 학습 결과 : 하위 디렉토리 results.  
     사용 데이터셋 : https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=513 . AI-HUB 보행 안전을 위한 도로 시설물 데이터  
     전처리, 증강 등을 적용해서 dataset 마다 버전을 나누었다.
     results/v8m-result-4 의 경우 yolov8m 모델, 적용된 데이터셋 버전은 4 이라는 뜻이다.  
      
# 데모 애플리케이션
학습된 모델을 탑재한 (yolov8m) Flutter Aplicatoin  
https://github.com/DS-Capstone-Design-2024-Fall/Application  

![image](https://github.com/user-attachments/assets/d27ba2eb-e924-4a72-a177-74a87965ca3d)

# 결론 및 추후 과제
- 결론
     최종 보고서 내용의 실험 1, 2, 3 공통적으로 학습 중에 증강이 적용되었지만,  
  학습 전 데이터에 증강을 적용하기 전인 실험 1과 적용한 후인 실험 2, 3의 경우 예측 성능에 꽤 큰 차이가 존재한다.  
  실험 1의 학습중 Validation set 에 대한 결과(최종보고서 그림 14)에서 mAP50 은 대략 0.30, mAP50-95 는 대략 0.15의 수치였으나,  
  실험 2의 test set 에 대한 결과(최종보고서 그림19)에서는 각각 0.70, 0.50 정도로 크게 향상되었다.  

  다양한 형태 및 색상을 가지는 객체일수록 데이터 증강이 모델 예측 성능 개선에 크게 영향을 주었다.  
  클래스별로 성능 차이가 심하게 나는 문제는 오버샘플링을 통해 어느정도 완화할 수 있음을 확인하였다.

  ![image](https://github.com/user-attachments/assets/4f944244-2882-49be-8519-c8c934ce12d1)
  test/results/v11m-result-5-db-plus1000 결과 요약.  
  (train/results/v11m-result-5-db-plus1000/weights/best.pt)로 테스트하였다.
  

  ![3_12_1_1_2_2_20210815_0000207580-2](https://github.com/user-attachments/assets/37cbf0cf-3df3-4985-b4b3-1f980e0e80f6)  
  예측 및 정답 비교 (dataset_v3)  
  빨간 색 박스가 정답, 파란 색 박스가 예측에 해당한다.  

  
- 추후 과제 : 학습 데이터셋은 AI-HUB 의 데이터였으나, 실제로 촬영한 데이터를 섞어서 학습과 테스트에 적용


# 사용 데이터셋 설명

- street-facilities-raw  
Ai-hub에서 받은 대용량 데이터 원본 중 사용할 데이터만 모음

- street-facilities-selected (baseline)  
**street-facilities-raw**에서 2238 X 4032 이미지만 선택하여 360x640 으로 축소. 
너비 360 은 원본비율을 유지한 채 축소하는 과정에서 소수점을 올림처리해서 나온 정수

- <version 1.> 패딩 적용
street-facilities : 전처리 완료

- <version 2. (street-facilities-2)> 패딩 x
 baseline 1-a 에서 dataset 분할하여 저장

- <version 2. : only0>
싱글클래스. 실험 결과 성능에는 별 차이없음. 
결과 분석 편의상 계속 기존 방식대로 클래스 3가지로 수행.

- <version 3.>
 baseline에서 회전으로 증강 후 dataset 분할하여 저장

- <version 4.>
 baseline에서 확률적으로 원본 유지, 90도 회전, 플립, 랜덤크롭 후(각각 1/4확률) dataset 분할하여 저장

- <version 5.>  
 baseline에서 확률적으로 원본유지, 90/180/270도 회전 후(각각 1/4 확률) dataset 분할하여 저장  

- <version 5 - db>  
 방식은 동일하되 version 5.보다 데이터양이 2배 많게 조정  
