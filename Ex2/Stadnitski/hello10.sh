for i in {0..9}
do
  num=$RANDOM
  ./hello $num
  ./hello $num > shOut/shOut$i.txt &
done
wait
