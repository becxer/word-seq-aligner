# WordSequenceAligner

## Usage

        $./Aligner.py reference.txt target.txt

        ----------------------------------------------------
        REF : 겐지  가  함께  한다 (8)
        TRG : 겐지  가  함께  한다 (10)
        ED : 2
        WER : 0.25
        ----------------------------------------------------
        REF : 빽슨도쉐또무드게   (8)
        TRG : 빽선도쉐또무드갸하 (9)
        ED : 3
        WER : 0.375
        ----------------------------------------------------
        REF : 석양이  진다 (6)
        TRG : 석양이  진다 (5)
        ED : 1
        WER : 0.166666666667
        ----------------------------------------------------
        REF : 류진노  켄오  쿠라에 (10)
        TRG : 류승룡기모찌이       (7)
        ED : 9
        WER : 0.9
        ===========================================================
        Average ED : 3.75
        Average WER : 0.422916666667
        Average ERR : 1.0

