# Train-yolo
# Project Summary
  현행 민원 접수 서비스는 시민이 불량 시설 보수 요청 민원 등의 신고를 하면 이를 사람이 보고 판단하기 때문에 신고가 접수되고 처리되는 과정에서 지연과, 인력 소모가 발생하였다. 
  사람 대신 객체 탐지 모델을 배치하여 사람 대신 불량 시설물을 탐지하고 이후 처리도 자동화한다면 이러한 문제를 해결할 수 있을 것이다. 
  따라서 본 연구에서는 YOLO 모델을 학습시켜 국내 보행 시설의 불량을 감지할 수 있게 만들고, 해당 모델을 배치한 애플리케이션을 구현하였다.

  모델 학습 진행 : https://github.com/DS-Capstone-Design-2024-Fall/Train-yolo/tree/main/test  
  애플리케이션 : https://github.com/DS-Capstone-Design-2024-Fall/Application/blob/master/README.md  

# Code instruction
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

crack-pretraining.yaml  
Pre training 에 필요한, 모델 입력 데이터셋에 대한 메타데이터 정보  

street-facilities.yaml  
모델 학습에 필요한, 모델 입력 데이터셋에 대한 메타데이터 정보  

Preprocessing 폴더  
데이터 전처리에 관한 코드 모음  

Test 폴더
1. 모델 test 실행 python 파일 및 쉘 스크립트 (경희대학교 Seraph GPU 에서 실행하기 위한 용도) 파일  
2. 테스트 결과 : 하위 디렉토리 results  

Train 폴더
1. 모델 train 실행 관련 python 파일 및 쉘 스크립트  
2. 모델 튜닝 관련 python 파일 및 쉘 스크립트  
3. Pre-training 관련 python 파일 및 쉘 스크립트 (여러 실험 중 하나였으나 의미있는 결과는 X)  
4. 학습 결과 : 하위 디렉토리 results  

# Demo
학습된 모델을 탑재한 (yolov8m) Flutter Aplicatoin  
https://github.com/DS-Capstone-Design-2024-Fall/Application  

![image](https://github.com/user-attachments/assets/d27ba2eb-e924-4a72-a177-74a87965ca3d)

# Conclusion and Future Work
- Concolusion
     최종 보고서 내용의 실험 1, 2, 3 공통적으로 학습 중에 증강이 적용되었지만,  
  학습 전 데이터에 증강을 적용하기 전인 실험 1과 적용한 후인 실험 2, 3의 경우 예측 성능에 꽤 큰 차이가 존재한다.  
  실험 1의 학습중 Validation set 에 대한 결과(최종보고서 그림 14)에서 mAP50 은 대략 0.30, mAP50-95 는 대략 0.15의 수치였으나,  
  실험 2의 test set 에 대한 결과(최종보고서 그림19)에서는 각각 0.70, 0.50 정도로 크게 향상되었다.  

  다양한 형태 및 색상을 가지는 객체일수록 데이터 증강이 모델 예측 성능 개선에 크게 영향을 주었다.  
  클래스별로 성능 차이가 심하게 나는 문제는 오버샘플링을 통해 어느정도 완화할 수 있음을 확인하였다.  
  
-Future work : 학습 데이터셋은 AI-HUB 의 데이터였으나, 실제로 촬영한 데이터를 섞어서 학습과 테스트에 적용  
 
