DATASET=scidocs
MODEL=seetopic

python format.py --dataset $DATASET --model $MODEL
python evaluation.py --dataset $DATASET --model $MODEL