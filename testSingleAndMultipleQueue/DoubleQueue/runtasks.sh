CNT=64

for (( c=1; c<=$CNT; c++))
do
    python add_tasks_1_2.py&
done

for (( c=1; c<=$CNT; c++))
do
    python add_tasks_3_4.py&
done
