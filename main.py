n = int(input("Введите общее количество журавликов: "))
nPetya = n // 6
nKatya = nPetya * 4
nSerg = n - nPetya - nKatya
print(f"Петя сделал {nPetya} журавликов, Катя сделала {nKatya} журавликов, Сергей сделал {nSerg} журавликов.")