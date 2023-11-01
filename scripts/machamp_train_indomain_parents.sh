cd machamp

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.1.cardiffnlp-twitter-roberta-base --parameters_config ../configs/params.cardiffnlp-twitter-roberta-base.json --seed 1

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.2.cardiffnlp-twitter-roberta-base --parameters_config ../configs/params.cardiffnlp-twitter-roberta-base.json --seed 2

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.3.cardiffnlp-twitter-roberta-base --parameters_config ../configs/params.cardiffnlp-twitter-roberta-base.json --seed 3

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.1.bert-base-cased --parameters_config ../configs/params.bert-base-cased.json --seed 1

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.2.bert-base-cased --parameters_config ../configs/params.bert-base-cased.json --seed 2

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.3.bert-base-cased --parameters_config ../configs/params.bert-base-cased.json --seed 3

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.1.roberta-base --parameters_config ../configs/params.roberta-base.json --seed 1

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.2.roberta-base --parameters_config ../configs/params.roberta-base.json --seed 2

!python3 train.py --dataset_config ../configs/parents.json --name parents.machamp.3.roberta-base --parameters_config ../configs/params.roberta-base.json --seed 3


cd ..
