from functools import partial


a = {}

While True :
    x = input ( "(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: " )

    if x . lower () == 't' :
        print ( "Tambah Data" )
        nama = input ( "Nama : " )
        nim = int (input ( "NIM : " ))
        uts = int (input( "Nilai UTS :" ))
        tugas = int (input ( "Nilai Tugas : " ))
        n_akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a [ nama ] + nim , uts , uas , tugas , n_akhir
    
    elif x . lower () == 'u' :

        print ( "Data Ubah" )
        nama = input ( "Masukan nama : " )
        if nama in a . keys () :
            nim = int ( input ( "NIM : " ))
            uts = int ( input ( "Nilai UTS : " ))
            uas = int ( input ( "Nilai UAS : " ))
            tugas = int ( input ( "Nilai Tugas : " ))
            n_akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
            a [ nama ] = nim , uts , uas , tugas , n_akhir
        
        else :
            print ( "Nama{0} Tidak ditemukan" . format ( nama ))

        elif x . lower () == 'h' :
            print ( "Data Hapus" )
            nama = input ( "Masukan nama : " )
            if nama in a . keys ():
                del a [ nama ]
            else :
                print ( "Nama {0} Tidak ditemukan" . format ( nama ))
            
        elif x . lower () == 'c' :
            print ( "Data Cari" )
            nama = input ( "Masukan nama : ")
            if nama in a . keys ():
                print ( "=" * 73 )
                print ( "| Daftar Mahasiswa |" )
                print ( "=" * 73 )
                print ( "| Nama | NIM | UTS | UAS | TUGAS | Akhir |" )
                print ( "=" * 73 )
                print ( "|{0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                . format ( nama, nim, uts , uas , tugas , n_akhir ))
                print ( "=" * 73 )
            else :
                print ( "Nama {0} Tidak Ditemukan" . format ( nama ))

            elif x . lower ()  == '1' :
                if a . items ():
                    print ( "=" * 78 )
                    print ( "| Daftar Mahasiswa |" )
                    print ( "=" * 78 )
                    print ( "|No. | Nama | NIM | UTS | UAS | Tugas | Akhir |" )
                    print ( "=" * 78 )
                    i = 0
                    for y in a . items ():
                        1 += 1
                        print ( "| {no:2d} | {0:15s} | {1:15d | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                        . format ( y [ 0 ][: 13 ], y [ 1 ][ 0 ], y [ 1 ][ 1 ], y [ 1 ][ 2 ], y [ 1 ][ 3 ], y [ 1 ][ 4 ] .
                        no = i ))
                    print ( "=" * 78 )
                else :
                    print ( "=" * 78 )
                    print ( "|Daftar Mahasiswa |" )
                    print ( "=" * 78 )
                    print ( "| No. | Nama | NIM | UTS | UAS | Tugas | Akhir |" )
                    print ( "| TIDAK ADA DATA |" )
                    print ( "=" * 78)

                elif x . lower () == 'k' :
                    break
                else :
                    print ( "Pilih Mana Yang Tersedia" )