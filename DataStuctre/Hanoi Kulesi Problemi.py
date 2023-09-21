def hanoi_kuleleri_tasi(n, kaynak, yardimci, hedef):
    if n == 1:
        print(f"{kaynak} çubuğundan {hedef} çubuğuna disk 1'i taşı")
        return
    hanoi_kuleleri_tasi(n-1, kaynak, hedef, yardimci)
    print(f"{kaynak} çubuğundan {hedef} çubuğuna disk {n} taşı")
    hanoi_kuleleri_tasi(n-1, yardimci, kaynak, hedef)


disk_sayisi = 3
hanoi_kuleleri_tasi(disk_sayisi, 'A', 'B', 'C')
