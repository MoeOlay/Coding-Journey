interstate_number = int(input("Please enter an interstate number:"))
auxiliary = interstate_number//100
primary = interstate_number%100
if primary == 0:
    print(f'{interstate_number} is not a valid interstate highway number.')
elif auxiliary == 0 and primary%10 == 5:
    print(f'I-{primary} is primary, going north/south.')
elif auxiliary == 0 and primary%10 == 0:
    print(f'I-{primary} is primary, going east/west.')
elif auxiliary > 0 and primary%10 == 5:
     print(f'I-{interstate_number} is auxiliary, serving I-{primary}, going north/south.')
elif auxiliary > 0 and primary%10 == 0:
     print(f'I-{interstate_number} is auxiliary, serving I-{primary}, going east/west.')
else:
    print(f'{interstate_number} is not a valid interstate highway number.')