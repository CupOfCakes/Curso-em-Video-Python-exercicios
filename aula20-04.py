def maior(*num):
    print("=" * 40)
    print("a analisando os valores passados...")
    print(f"{num} foram informados {len(num)} valores ao todo.\n"
          f"o maior valor informados foi {max(num)}")


maior(2, 7, 8, 9, 0, 1, 3)
maior(0, 2, 8)
maior(7, 1, 12, 6)
maior(1)
