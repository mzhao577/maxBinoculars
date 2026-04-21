
pyScript="binocularAnalysis.py"
model="large"
inDir="./input"
outDir="./output"
outFile="BinocularAnalysis_${model}.csv"


python  binocularAnalysis.py --input_dir $inDir --model ${model}  --output_dir $outDir  --output_file $outFile 

