cd scigen
perl make-latex.pl --author "11811901 fanshun"
cd tmp
cd scigen/tmp
for dir in $(ls)
do
    [ -d $dir ] && file0=$dir
done

cd $file0
file=$(find *.tex)
latex $file
bibtex $file
latex $file
latex $file
file2=$(find *.dvi)
dvipdf $file2
file3=$(find *.pdf)
mv $file3 ../../../$1
cd ../..
rm -rf tmp
