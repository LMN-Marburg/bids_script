#/bin/sh
#Pfad zu den BOLD Bildern als 1ter Parameter angeben
#Funktioniert nur wenn noch kein zusammengefasstes Bild existiert
#Nur in fsl5env nutzbar

#Schritt 1 Name aus den vorhanden Dateien extrahieren
#echo Name extrahieren ...
cd $1
#VAR=$(/bin/ls -tr *.nii | tail -1)
#DATA=${VAR%_*}
#echo Name extrahieren ... done  $DATA 

#Schritt 2 fslmerge ueber die Zeitserie anstossen und in dem extrahierten Namen speichern
echo Merge Dateien ...
fslmerge -t $2.nii *.nii
echo Merge Dateien ... done

#Schritt 3 es entsteht eine ZIP Datei, in der das 4D Bild enthalten ist. Diese muss hier *nicht* extrahiert werden.
#echo Datei entpacken ...
#gzip -d $DATA.nii.gz
#echo Datei entpacken ... done
